import os
import sys
import logging

from linkml.validator import validate_file

# from linkml_runtime.loaders import yaml_loader
# from linkml_runtime.utils.schemaview import SchemaView


# Custom formatter with emojis and better visual structure
class ColoredFormatter(logging.Formatter):
    """Custom formatter with emojis and indentation for better readability"""

    # ANSI color codes
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Format strings with emojis and colors
    FORMATS = {
        logging.INFO: f"{BLUE}ℹ️  INFO:{RESET} %(message)s",
        logging.WARNING: f"{YELLOW}⚠️  WARNING:{RESET} %(message)s",
        logging.ERROR: f"{RED}❌ ERROR:{RESET} %(message)s",
        logging.CRITICAL: f"{RED}{BOLD}🔥 CRITICAL:{RESET} %(message)s",
        logging.DEBUG: f"{GREEN}🔍 DEBUG:{RESET} %(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# Configure logger with custom formatter
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Clear any existing handlers
if logger.handlers:
    logger.handlers.clear()

# Console handler with custom formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(ColoredFormatter())
logger.addHandler(console_handler)


def validate_directory(directory_path, schema_path, target_class):
    """
    Validates all bdf.yaml or bdf.yml files in a directory against a LinkML schema.

    Args:
        directory_path: Path to the directory containing bdf.yaml or bdf.yml files
        schema_path: Path to the LinkML schema file
        target_class: Target class to validate against

    Raises:
        ValueError: If any file fails validation
    """
    logger.info("=" * 80)
    logger.info("🔍 Starting validation process")
    logger.info(f"📁 Directory: {directory_path}")
    logger.info(f"📜 Schema: {schema_path}")
    logger.info(f"🎯 Target class: {target_class}")
    logger.info("=" * 80)

    # Get list of bdf.yaml or bdf.yml files in the directory
    supported_files = [
        f for f in os.listdir(directory_path) if f in ("bdf.yaml", "bdf.yml")
    ]

    if not supported_files:
        logger.warning(f"📂 No bdf.yaml or bdf.yml files found in {directory_path}")
        return

    logger.info(f"📊 Found {len(supported_files)} files to validate")
    logger.info("-" * 60)

    # Track validation statistics
    valid_count = 0

    # Validate each file
    for idx, schema_file in enumerate(supported_files, 1):
        file_path = os.path.join(directory_path, schema_file)
        logger.info(f"🔄 [{idx}/{len(supported_files)}] Validating: {schema_file}")

        # Validate the file
        try:
            report = validate_file(file_path, schema_path, target_class)

            # Check if validation failed
            if report.results:
                logger.error(f"  ❌ Validation FAILED for {schema_file}")
                logger.error("  📋 Error details:")

                # Print errors with indentation for better readability
                for i, result in enumerate(report.results, 1):
                    logger.error(f"    {i}. {result.message}")

                logger.error("-" * 60)
                raise ValueError(
                    f"🛑 Validation process stopped due to errors in {schema_file}"
                )
            else:
                valid_count += 1
                logger.info(f"  ✅ {schema_file} is VALID")
                logger.info("-" * 60)
        except Exception as e:
            if "Validation failed" not in str(e):
                logger.error(f"  💥 Exception processing {schema_file}: {str(e)}")
                logger.error("-" * 60)
                raise

    # Summary
    logger.info("=" * 80)
    logger.info(f"🎉 Validation complete! All {valid_count} files are valid")
    logger.info("=" * 80)


# Example usage
if __name__ == "__main__":
    DATA_DIRECTORY = "."
    SCHEMA_PATH = (
        sys.argv[1]
        if sys.argv[1]
        else "https://raw.githubusercontent.com/ARPA-H-BDF/bdfkb-schema/refs/heads/main/src/bdfkb_schema/schema/bdfkb_schema.yaml"
    )
    TARGET_CLASS = "SystemMetadata"

    validate_directory(DATA_DIRECTORY, SCHEMA_PATH, TARGET_CLASS)
