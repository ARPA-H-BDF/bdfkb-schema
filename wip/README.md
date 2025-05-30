# WIP

* [wip/](wip/) - Work in progress / working versions of LinkML sub-schemas
  * [biotoolsSchema_schema](wip/biotoolsSchema_schema/) -- Independent biotoolsSchema LinkML rep
    * Modular schema in yaml
    * LinkML rep created using [schema-automator](https://github.com/linkml/schema-automator)
    * Uses [JSON Schema version](https://github.com/bio-tools/biotoolsSchema/tree/main/jsonschema) of biotoolsSchema
    * Example validation script: `linkml-validate -s wip/biotoolsSchema_schema/biotoolsSchema_schema.yaml src/data/examples/bioTools-Tool-001.yaml --target-class Tool`
  * [bdftoolbox_schema](wip/bdftoolbox_schema/) -- BDF opinionated schema for describing tools in the BDF toolbox
    * Profiles schemas for different tool classifications