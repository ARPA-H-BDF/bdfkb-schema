# bdfkb-schema

Schema to describe BDF Toolbox entities and the relationships between them.

## Website

[https://ARPA-H-BDF.github.io/bdfkb-schema](https://ARPA-H-BDF.github.io/bdfkb-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [bdfkb_schema](src/bdfkb_schema)
    * [schema](src/bdfkb_schema/schema) -- LinkML schema
      (edit this)
      * [biotoolsSchema_schema](src/bdfkb_schema/schema/biotoolsSchema_schema/) -- Independent biotoolsSchema LinkML rep
        * Modular schema in yaml
        * LinkML rep created using [schema-automator](https://github.com/linkml/schema-automator)
        * Uses [JSON Schema version](https://github.com/bio-tools/biotoolsSchema/tree/main/jsonschema) of biotoolsSchema
        * Example validation script: `linkml-validate -s src/bdfkb_schema/schema/biotoolsSchema_schema/biotoolsSchema_schema.yaml src/data/examples/bioTools-Tool-001.yaml --target-class Tool`
      * [bdftoolbox_schema](src/bdfkb_schema/schema/bdftoolbox_schema/) -- BDF opinionated schema for describing tools in the BDF toolbox
        * Profiles schemas for different tool classifications
    * [datamodel](src/bdfkb_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

<details>
<summary>uv setup</summary>

Installation:
* With uv installed, run `uv run main.py`
  * This will install all dependencies & use required Python version
* Install linkml tools (if not already installed): `uv tool install linkml`

</details>

<details>
<summary>ER Diagram Generation</summary>

Create ER Diagram with Mermaid:
* `gen-erdiagram ./src/bdfkb_schema/schema/sample_import_schema/custom-llm-tool.yaml > mermaid.md`

</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
