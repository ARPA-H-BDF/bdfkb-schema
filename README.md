# bdfkb-schema

Schema to describe content of the BDF Knowledgebase (BDFKB), including tools and related entities as well as the relationships between them.

## Website

[https://ARPA-H-BDF.github.io/bdfkb-schema](https://ARPA-H-BDF.github.io/bdfkb-schema)

## Repository Structure

* [src/](src/) - source files (edit these)
  * [bdfkb_schema](src/bdfkb_schema)
    * [schema](src/bdfkb_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/bdfkb_schema/datamodel) -- Python classes. Located here to conform with python conventions so users can, for example `from bdfkb_schema.datamodel.bdfkb_schema import ToolInfo`
    * [docs](src/docs/) - Files for customizing Markdown docs
    * [data](src/data/) - Data files used for testing
* [project/](project/) Auto generated by LinkML tools, typically these are committed to source control, but they are ignored here until there is a specific use for them. 
* [docs/](docs/) - Auto generated Markdown using `GenDoc` and files in `project/docs`
* [wip/](wip/) - Work in progress, including sub-schemas


## Developer Documentation

### Quick-start setup:
<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

<details>
<summary>poetry setup (recommended)</summary>

Create virtual env and install dependencies:

* `poetry install`

</details>

<details>
<summary>uv setup</summary>

Installation:
* `uv run main.py`
  * This will install all dependencies & use required Python version
* Install linkml tools (if not already installed): 
  * `uv tool install linkml`

</details>

<details>
<summary>conda setup</summary>

1. Create conda venv:

  - `conda create -n "venv" python=3.9`

2. Activate venv:

  - `conda activate venv`

3. Install dependencies:

  - `pip install .`

</details>

<details>
<summary>ER Diagram Generation</summary>

Create ER Diagram with Mermaid:
* `gen-erdiagram ./src/bdfkb_schema/schema/sample_import_schema/custom-llm-tool.yaml > mermaid.md`

</details>

### Using `make`

The LinkML cookiecutter uses `make` so this is the easiest way to get started. Here are some examples: 

- Test all things `make test`
- Test schema `make test-schema`
- Generate pydantic classes `make gen-pydantic`
- And more! 

### Using `poetry` & `linkml` tools

Under the hood, the Makefile is basically running python and using the `linkml` generator tools. So you can run the same commands directly if you choose. 

- Run tests `poetry run python -m unittest discover`
- Generate mermaid diagram of schema `gen-erdiagram -f mermaid src/bdfkb_schema/schema/bdfkb_schema.yaml > mermaid.md`
- And more! 
  
### Using `uv`

`uv` is a modern tool for python that aims to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more. Learn more here https://github.com/astral-sh/uv

Some of team uses `uv`, so you might find `uv` bits scattered around this project. However, since the LinkML cookiecutter project still uses poetry, this project is not yet fully embracing `uv`. Install `uv` and then `uv tool install linkml` and explore at your own risk.

## Testing for Schema Developers
### Testing via Remote URL
In order to test a schema change on the existing dataset, one recommended approach is:
1. Push your branch of changes from `bdfkb-schema` to GitHub
2. Go online and copy the raw file url for `bdfkb-schema.yaml` on your feature branch
3. Move to the `bdfkb-data` repository. In `main.py`, update the `SCHEMA_PATH` url to the url you just copied.
4. Run the `main.py` file using whichever runtime you prefer (uv, poetry, conda)

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter), however much of what the cookie cutter provides is not needed here and thus removed. We opted to \[mostly\] stick with cookiecutter template so this would be familiar to someone already familiar with the LinkML project (and template).
