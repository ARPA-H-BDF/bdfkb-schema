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
    * [datamodel](src/bdfkb_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
