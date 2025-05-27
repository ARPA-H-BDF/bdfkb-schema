# bdfkb-schema

Schema to describe content of the BDF Knowledgebase (BDFKB), including tools and related entities as well as the relationships between them.

## Website

[https://ARPA-H-BDF.github.io/bdfkb-schema](https://ARPA-H-BDF.github.io/bdfkb-schema)

## Repository Structure

* [src/](src/) - source files (edit these)
  * [bdfkb_schema](src/bdfkb_schema)
    * [schema](src/bdfkb_schema/schema) -- LinkML schema
      (edit this)
* [draft/](draft/) - draft / working versions of LinkML sub-schemas
  * [biotoolsSchema_schema](src/bdfkb_schema/schema/biotoolsSchema_schema/) -- Independent biotoolsSchema LinkML rep
    * Modular schema in yaml
    * LinkML rep created using [schema-automator](https://github.com/linkml/schema-automator)
    * Uses [JSON Schema version](https://github.com/bio-tools/biotoolsSchema/tree/main/jsonschema) of biotoolsSchema
    * Example validation script: `linkml-validate -s src/bdfkb_schema/schema/biotoolsSchema_schema/biotoolsSchema_schema.yaml src/data/examples/bioTools-Tool-001.yaml --target-class Tool`
  * [bdftoolbox_schema](src/bdfkb_schema/schema/bdftoolbox_schema/) -- BDF opinionated schema for describing tools in the BDF toolbox
    * Profiles schemas for different tool classifications


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
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter), however much of what the cookie cutter provides is not needed here and thus removed. We opted to \[mostly\] stick with cookiecutter template so this would be familiar to someone already familiar with the LinkML project (and template).
