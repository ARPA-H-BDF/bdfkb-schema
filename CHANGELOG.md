This covers the changes made to bdfkb_schema starting in version 0.1.0, with the most recent version at the top.

## bdfkb_schema 0.5.5 (Nick Alico on 25 Aug-26)
- Add optional `linked_resources` attribute
    - Allows listing of assoicated repos that are not standalong tools, but instead serve as associated repos that contribute to the primary tool.
    - Allows ENHANCE V&V to perform a scopes sanity check on linked_resource repos, surfacing results in the scorecard for best practices and general awareness.

## bdfkb_schema 0.5.4 (Nick Alico on 20 Aug-26)

- Add monorepo demarcation support
    - If `monorepo` attribute listed with at least 1 package listed, root bdf.yaml passes as listed packages will be evaled as tools instead.
    - If `monorepo` not listed, or listed but there are no entries, then all expected attributes remain required.
- Fix CI action versions for updated runtimes (Node v24+)

## bdfkb_schema 0.5.3 (Nick Alico on 08 October-25)

- Add Google Vertex AI as llm model

## bdfkb_schema 0.5.2 (Nick Alico on 08 October-25)

- Enum updates for Stanford tools

## bdfkb_schema 0.5.1 (Nick Alico on 01 October-25)

- Added data-curator as permissible UserType

## bdfkb_schema 0.5.0 (Isaac Chan on 12 August-25)

- Added data-curator as permissible UserType

## bdfkb_schema 0.4.9 (Nick Alico on 12 August-25)

- Added yaml validation CI stage

## bdfkb_schema 0.4.8 (Isaac Chan on 6 August-25)

- Added avro file format
- Added serialized data class
- Added uc-ctds and llama-data-model-generator LLM

## bdfkb_schema 0.4.7 (Nick Alico on 30 July-25)

- Added Gemma LLM

## bdfkb_schema 0.4.6 (Nick Alico on 30 July-25)

- Added SDRF proteomics File Format

## bdfkb_schema 0.4.5 (Nick Alico on 30 July-25)

- Added Data Manager as valid User Type

## bdfkb_schema 0.4.4 (Nick Alico on 30 July-25)

- Added JSONSchema as a valid input File Format

## bdfkb_schema 0.4.3 (Nick Alico on 30 July-25)

- Added Amazon Nova as a permissible field in LLMModel

## bdfkb_schema 0.4.2 (Isaac Chan on 18 July-25)

- Added together.ai as a permissible field in LLMModel

## bdfkb_schema 0.4.1 (Isaac Chan on 18 July-25)

- Added new field for FileFormat enum

## bdfkb_schema 0.4.0 (Isaac Chan on 23 June-25)

- Added fields for API tool

## bdfkb_schema 0.3.1 (Isaac Chan, Nick Alico on 11 June-25)

- Migrated added schema field from bdfkb-data to achieve parity post-migration
- Migrate https://github.com/ARPA-H-BDF/bdfkb-data/pull/10 hotfix
- Added README details for how schema developers can test against existing tool suite

## bdfkb_schema 0.3.0 (Nick Alico on 11 June-25)

- Updated package manager setup details in readme

## bdfkb_schema 0.2.0 (Isaac Chan on 10 June-25)

- Updated schema to include package url

## bdfkb_schema 0.1.0 (Matt Miller on 28 May-25)

- Initial version of the schema, merging the ARPA-H and CRA work into this repo