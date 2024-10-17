# bdf-toolbox-schema

Schema to describe BDF Toolbox entities and the relationships between them.

## Website

[https://ARPA-H-BDF.github.io/bdf-toolbox-schema](https://ARPA-H-BDF.github.io/bdf-toolbox-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [bdf_toolbox_schema](src/bdf_toolbox_schema)
    * [schema](src/bdf_toolbox_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/bdf_toolbox_schema/datamodel) -- generated
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
