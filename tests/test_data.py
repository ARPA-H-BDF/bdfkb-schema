"""Data test."""
import os
import glob
import unittest

from linkml.validator import validate_file

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples", "valid")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))
SCHEMA_FILE = os.path.join(ROOT, "src", "bdfkb_schema", "schema", "bdfkb_schema.yaml") 
TARGET_CLASS = "SystemMetadata"

class TestData(unittest.TestCase):
    """Test all schema files validate with schema"""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            
            report = validate_file(path, SCHEMA_FILE, TARGET_CLASS)
            
            # Check if validation failed
            if report.results:
                print(f"INVALID - Found validation errors in {SCHEMA_FILE}:")
                for result in report.results:
                    print(f"- {result.message}")
                raise ValueError(f'Validation failed for {SCHEMA_FILE} - see errors above')
            else:
                print(f"VALID - {SCHEMA_FILE} passed validation")
            
            assert report.results == []
