# Auto generated from bdfkb_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-27T19:49:05
# Schema: system-metadata-schema
#
# id: https://example.org/system-metadata-schema
# description: Schema for describing system metadata including LLM usage, cloud platform, inputs, outputs, collaborations, and funding information
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDateTime, string

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORCID = CurieNamespace('ORCID', 'http://identifiers.org/orcid/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SCHEMA


# Types
class Url(str):
    """ A valid HTTP or HTTPS URL """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "url"
    type_model_uri = SCHEMA.Url


class SemanticVersion(string):
    type_class_uri = URIRef(str(SCHEMA))
    type_class_curie = "schema:"
    type_name = "SemanticVersion"
    type_model_uri = SCHEMA.SemanticVersion


class DOIType(string):
    """ A Digital Object Identifier (DOI) """
    type_class_uri = LINKML["types/DOI"]
    type_class_curie = "linkml:types/DOI"
    type_name = "DOIType"
    type_model_uri = SCHEMA.DOIType


class DataStandardOrString(String):
    """ Type encompassing data standards or open strings """
    type_class_uri = URIRef(str(SCHEMA))
    type_class_curie = "schema:"
    type_name = "DataStandardOrString"
    type_model_uri = SCHEMA.DataStandardOrString


class SecondaryUserTypeOrString(String):
    """ Type for either SecondaryUser, or if other then specify string """
    type_class_uri = URIRef(str(SCHEMA))
    type_class_curie = "schema:"
    type_name = "SecondaryUserTypeOrString"
    type_model_uri = SCHEMA.SecondaryUserTypeOrString


class DataCategoryOrString(String):
    """ Type for either DataCategory, or if other then specify string """
    type_class_uri = URIRef(str(SCHEMA))
    type_class_curie = "schema:"
    type_name = "DataCategoryOrString"
    type_model_uri = SCHEMA.DataCategoryOrString


class DataTypeOrString(String):
    """ Type for either DataType, or if other then specify string """
    type_class_uri = URIRef(str(SCHEMA))
    type_class_curie = "schema:"
    type_name = "DataTypeOrString"
    type_model_uri = SCHEMA.DataTypeOrString


# Class references



@dataclass(repr=False)
class SystemMetadata(YAMLRoot):
    """
    Top level class representing system metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["SystemMetadata"]
    class_class_curie: ClassVar[str] = "schema:SystemMetadata"
    class_name: ClassVar[str] = "SystemMetadata"
    class_model_uri: ClassVar[URIRef] = SCHEMA.SystemMetadata

    version: string = None
    tool: Union[dict, "ToolInfo"] = None
    domains: Union[str, List[str]] = None
    llm: Union[dict, "LlmInfo"] = None
    input: Union[Union[dict, "DataSource"], List[Union[dict, "DataSource"]]] = None
    output: Union[Union[dict, "DataSource"], List[Union[dict, "DataSource"]]] = None
    collaborations: Union[Union[dict, "Collaboration"], List[Union[dict, "Collaboration"]]] = None
    maturity: Union[dict, "MaturityLevel"] = None
    license: Union[dict, "License"] = None
    credit: Union[Union[dict, "Credit"], List[Union[dict, "Credit"]]] = None
    target_users: Union[dict, "TargetUsers"] = None
    cloud: Optional[Union[dict, "CloudInfo"]] = None
    funding: Optional[Union[dict, "FundingInfo"]] = None
    publication: Optional[Union[Union[dict, "PublicationDetail"], List[Union[dict, "PublicationDetail"]]]] = empty_list()
    media: Optional[Union[Union[dict, "Media"], List[Union[dict, "Media"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, string):
            self.version = string(self.version)

        if self._is_empty(self.tool):
            self.MissingRequiredField("tool")
        if not isinstance(self.tool, ToolInfo):
            self.tool = ToolInfo(**as_dict(self.tool))

        if self._is_empty(self.domains):
            self.MissingRequiredField("domains")
        if not isinstance(self.domains, list):
            self.domains = [self.domains] if self.domains is not None else []
        self.domains = [v if isinstance(v, str) else str(v) for v in self.domains]

        if self._is_empty(self.llm):
            self.MissingRequiredField("llm")
        if not isinstance(self.llm, LlmInfo):
            self.llm = LlmInfo(**as_dict(self.llm))

        if self._is_empty(self.input):
            self.MissingRequiredField("input")
        self._normalize_inlined_as_dict(slot_name="input", slot_type=DataSource, key_name="name", keyed=False)

        if self._is_empty(self.output):
            self.MissingRequiredField("output")
        self._normalize_inlined_as_dict(slot_name="output", slot_type=DataSource, key_name="name", keyed=False)

        if self._is_empty(self.collaborations):
            self.MissingRequiredField("collaborations")
        self._normalize_inlined_as_dict(slot_name="collaborations", slot_type=Collaboration, key_name="name", keyed=False)

        if self._is_empty(self.maturity):
            self.MissingRequiredField("maturity")
        if not isinstance(self.maturity, MaturityLevel):
            self.maturity = MaturityLevel(**as_dict(self.maturity))

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self._is_empty(self.credit):
            self.MissingRequiredField("credit")
        if not isinstance(self.credit, list):
            self.credit = [self.credit] if self.credit is not None else []
        self.credit = [v if isinstance(v, Credit) else Credit(**as_dict(v)) for v in self.credit]

        if self._is_empty(self.target_users):
            self.MissingRequiredField("target_users")
        if not isinstance(self.target_users, TargetUsers):
            self.target_users = TargetUsers(**as_dict(self.target_users))

        if self.cloud is not None and not isinstance(self.cloud, CloudInfo):
            self.cloud = CloudInfo(**as_dict(self.cloud))

        if self.funding is not None and not isinstance(self.funding, FundingInfo):
            self.funding = FundingInfo(**as_dict(self.funding))

        if not isinstance(self.publication, list):
            self.publication = [self.publication] if self.publication is not None else []
        self.publication = [v if isinstance(v, PublicationDetail) else PublicationDetail(**as_dict(v)) for v in self.publication]

        if not isinstance(self.media, list):
            self.media = [self.media] if self.media is not None else []
        self.media = [v if isinstance(v, Media) else Media(**as_dict(v)) for v in self.media]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LlmInfo(YAMLRoot):
    """
    Information about LLM usage in the system
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["LlmInfo"]
    class_class_curie: ClassVar[str] = "schema:LlmInfo"
    class_name: ClassVar[str] = "LlmInfo"
    class_model_uri: ClassVar[URIRef] = SCHEMA.LlmInfo

    usesLlm: Union[bool, Bool] = None
    bringOwnKey: Union[bool, Bool] = None
    modelsSupported: Optional[Union[Union[str, "LLMModel"], List[Union[str, "LLMModel"]]]] = empty_list()
    modelsRequired: Optional[Union[Union[str, "LLMModel"], List[Union[str, "LLMModel"]]]] = empty_list()
    reasonsForRequirement: Optional[Union[Union[str, "LLMRequirementReason"], List[Union[str, "LLMRequirementReason"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.usesLlm):
            self.MissingRequiredField("usesLlm")
        if not isinstance(self.usesLlm, Bool):
            self.usesLlm = Bool(self.usesLlm)

        if self._is_empty(self.bringOwnKey):
            self.MissingRequiredField("bringOwnKey")
        if not isinstance(self.bringOwnKey, Bool):
            self.bringOwnKey = Bool(self.bringOwnKey)

        if not isinstance(self.modelsSupported, list):
            self.modelsSupported = [self.modelsSupported] if self.modelsSupported is not None else []
        self.modelsSupported = [v if isinstance(v, LLMModel) else LLMModel(v) for v in self.modelsSupported]

        if not isinstance(self.modelsRequired, list):
            self.modelsRequired = [self.modelsRequired] if self.modelsRequired is not None else []
        self.modelsRequired = [v if isinstance(v, LLMModel) else LLMModel(v) for v in self.modelsRequired]

        if not isinstance(self.reasonsForRequirement, list):
            self.reasonsForRequirement = [self.reasonsForRequirement] if self.reasonsForRequirement is not None else []
        self.reasonsForRequirement = [v if isinstance(v, LLMRequirementReason) else LLMRequirementReason(v) for v in self.reasonsForRequirement]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CloudInfo(YAMLRoot):
    """
    Information about cloud platform usage
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CloudInfo"]
    class_class_curie: ClassVar[str] = "schema:CloudInfo"
    class_name: ClassVar[str] = "CloudInfo"
    class_model_uri: ClassVar[URIRef] = SCHEMA.CloudInfo

    platform: Union[str, "CloudProvider"] = None
    lastAuditDate: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.platform):
            self.MissingRequiredField("platform")
        if not isinstance(self.platform, CloudProvider):
            self.platform = CloudProvider(self.platform)

        if self._is_empty(self.lastAuditDate):
            self.MissingRequiredField("lastAuditDate")
        if not isinstance(self.lastAuditDate, XSDDateTime):
            self.lastAuditDate = XSDDateTime(self.lastAuditDate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(YAMLRoot):
    """
    Information about data inputs or outputs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataSource"]
    class_class_curie: ClassVar[str] = "schema:DataSource"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = SCHEMA.DataSource

    name: str = None
    dataCategory: Union[str, DataCategoryOrString] = None
    dataClass: Union[str, "DataClass"] = None
    dataType: Union[str, DataTypeOrString] = None
    dataStandard: Union[Union[str, DataStandardOrString], List[Union[str, DataStandardOrString]]] = None
    format: Union[Union[str, "FileFormat"], List[Union[str, "FileFormat"]]] = None
    proprietary: Union[bool, Bool] = None
    dataSubType: Optional[str] = None
    source: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.dataCategory):
            self.MissingRequiredField("dataCategory")
        if not isinstance(self.dataCategory, DataCategoryOrString):
            self.dataCategory = DataCategoryOrString(self.dataCategory)

        if self._is_empty(self.dataClass):
            self.MissingRequiredField("dataClass")
        if not isinstance(self.dataClass, DataClass):
            self.dataClass = DataClass(self.dataClass)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, DataTypeOrString):
            self.dataType = DataTypeOrString(self.dataType)

        if self._is_empty(self.dataStandard):
            self.MissingRequiredField("dataStandard")
        if not isinstance(self.dataStandard, list):
            self.dataStandard = [self.dataStandard] if self.dataStandard is not None else []
        self.dataStandard = [v if isinstance(v, DataStandardOrString) else DataStandardOrString(v) for v in self.dataStandard]

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, FileFormat) else FileFormat(v) for v in self.format]

        if self._is_empty(self.proprietary):
            self.MissingRequiredField("proprietary")
        if not isinstance(self.proprietary, Bool):
            self.proprietary = Bool(self.proprietary)

        if self.dataSubType is not None and not isinstance(self.dataSubType, str):
            self.dataSubType = str(self.dataSubType)

        if self.source is not None and not isinstance(self.source, URI):
            self.source = URI(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Collaboration(YAMLRoot):
    """
    Information about tool collaborations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Collaboration"]
    class_class_curie: ClassVar[str] = "schema:Collaboration"
    class_name: ClassVar[str] = "Collaboration"
    class_model_uri: ClassVar[URIRef] = SCHEMA.Collaboration

    name: str = None
    description: str = None
    tools: Union[str, List[str]] = None
    collaboration_purpose: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.tools):
            self.MissingRequiredField("tools")
        if not isinstance(self.tools, list):
            self.tools = [self.tools] if self.tools is not None else []
        self.tools = [v if isinstance(v, str) else str(v) for v in self.tools]

        if self._is_empty(self.collaboration_purpose):
            self.MissingRequiredField("collaboration_purpose")
        if not isinstance(self.collaboration_purpose, str):
            self.collaboration_purpose = str(self.collaboration_purpose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FundingInfo(YAMLRoot):
    """
    Information about funding sources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["FundingInfo"]
    class_class_curie: ClassVar[str] = "schema:FundingInfo"
    class_name: ClassVar[str] = "FundingInfo"
    class_model_uri: ClassVar[URIRef] = SCHEMA.FundingInfo

    source: Optional[str] = None
    agreement: Optional[str] = None
    link: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.agreement is not None and not isinstance(self.agreement, str):
            self.agreement = str(self.agreement)

        if self.link is not None and not isinstance(self.link, URI):
            self.link = URI(self.link)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolInfo(YAMLRoot):
    """
    Metadata details about the tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["ToolInfo"]
    class_class_curie: ClassVar[str] = "schema:ToolInfo"
    class_name: ClassVar[str] = "ToolInfo"
    class_model_uri: ClassVar[URIRef] = SCHEMA.ToolInfo

    name: str = None
    repo_url: str = None
    tool_homepage: str = None
    documentation_url: str = None
    tool_type: Union[str, "ToolType"] = None
    tool_notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.repo_url):
            self.MissingRequiredField("repo_url")
        if not isinstance(self.repo_url, str):
            self.repo_url = str(self.repo_url)

        if self._is_empty(self.tool_homepage):
            self.MissingRequiredField("tool_homepage")
        if not isinstance(self.tool_homepage, str):
            self.tool_homepage = str(self.tool_homepage)

        if self._is_empty(self.documentation_url):
            self.MissingRequiredField("documentation_url")
        if not isinstance(self.documentation_url, str):
            self.documentation_url = str(self.documentation_url)

        if self._is_empty(self.tool_type):
            self.MissingRequiredField("tool_type")
        if not isinstance(self.tool_type, ToolType):
            self.tool_type = ToolType(self.tool_type)

        if self.tool_notes is not None and not isinstance(self.tool_notes, str):
            self.tool_notes = str(self.tool_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicationDetail(YAMLRoot):
    """
    Details regarding publication surrounding tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PublicationDetail"]
    class_class_curie: ClassVar[str] = "schema:PublicationDetail"
    class_name: ClassVar[str] = "PublicationDetail"
    class_model_uri: ClassVar[URIRef] = SCHEMA.PublicationDetail

    type: Optional[str] = None
    tool_version: Optional[string] = None
    doi: Optional[string] = None
    pmid: Optional[str] = None
    pmcid: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.tool_version is not None and not isinstance(self.tool_version, string):
            self.tool_version = string(self.tool_version)

        if self.doi is not None and not isinstance(self.doi, string):
            self.doi = string(self.doi)

        if self.pmid is not None and not isinstance(self.pmid, str):
            self.pmid = str(self.pmid)

        if self.pmcid is not None and not isinstance(self.pmcid, str):
            self.pmcid = str(self.pmcid)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class License(YAMLRoot):
    """
    Licensing details of tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["License"]
    class_class_curie: ClassVar[str] = "schema:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = SCHEMA.License

    license_type: Union[str, "LicenseType"] = None
    link: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.license_type):
            self.MissingRequiredField("license_type")
        if not isinstance(self.license_type, LicenseType):
            self.license_type = LicenseType(self.license_type)

        if self.link is not None and not isinstance(self.link, str):
            self.link = str(self.link)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Credit(YAMLRoot):
    """
    Credit details for tool creators
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Credit"]
    class_class_curie: ClassVar[str] = "schema:Credit"
    class_name: ClassVar[str] = "Credit"
    class_model_uri: ClassVar[URIRef] = SCHEMA.Credit

    name: Optional[str] = None
    email: Optional[Union[str, List[str]]] = empty_list()
    url: Optional[str] = None
    orcidid: Optional[str] = None
    role: Optional[Union[str, "ContributorRole"]] = None
    org: Optional[str] = None
    note: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.email, list):
            self.email = [self.email] if self.email is not None else []
        self.email = [v if isinstance(v, str) else str(v) for v in self.email]

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.orcidid is not None and not isinstance(self.orcidid, str):
            self.orcidid = str(self.orcidid)

        if self.role is not None and not isinstance(self.role, ContributorRole):
            self.role = ContributorRole(self.role)

        if self.org is not None and not isinstance(self.org, str):
            self.org = str(self.org)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaturityLevel(YAMLRoot):
    """
    Maturity level of application during development according to NASA TRL
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["MaturityLevel"]
    class_class_curie: ClassVar[str] = "schema:MaturityLevel"
    class_name: ClassVar[str] = "MaturityLevel"
    class_model_uri: ClassVar[URIRef] = SCHEMA.MaturityLevel

    beginning_maturity: int = None
    current_maturity: int = None
    final_maturity: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.beginning_maturity):
            self.MissingRequiredField("beginning_maturity")
        if not isinstance(self.beginning_maturity, int):
            self.beginning_maturity = int(self.beginning_maturity)

        if self._is_empty(self.current_maturity):
            self.MissingRequiredField("current_maturity")
        if not isinstance(self.current_maturity, int):
            self.current_maturity = int(self.current_maturity)

        if self.final_maturity is not None and not isinstance(self.final_maturity, int):
            self.final_maturity = int(self.final_maturity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrimaryUser(YAMLRoot):
    """
    Primary user of tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PrimaryUser"]
    class_class_curie: ClassVar[str] = "schema:PrimaryUser"
    class_name: ClassVar[str] = "PrimaryUser"
    class_model_uri: ClassVar[URIRef] = SCHEMA.PrimaryUser

    user_type: Union[str, "UserType"] = None
    technical_literacy_level: Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]] = None
    biomedical_literacy_level: Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.user_type):
            self.MissingRequiredField("user_type")
        if not isinstance(self.user_type, UserType):
            self.user_type = UserType(self.user_type)

        if self._is_empty(self.technical_literacy_level):
            self.MissingRequiredField("technical_literacy_level")
        if not isinstance(self.technical_literacy_level, list):
            self.technical_literacy_level = [self.technical_literacy_level] if self.technical_literacy_level is not None else []
        self.technical_literacy_level = [v if isinstance(v, LiteracyLevel) else LiteracyLevel(v) for v in self.technical_literacy_level]

        if self._is_empty(self.biomedical_literacy_level):
            self.MissingRequiredField("biomedical_literacy_level")
        if not isinstance(self.biomedical_literacy_level, list):
            self.biomedical_literacy_level = [self.biomedical_literacy_level] if self.biomedical_literacy_level is not None else []
        self.biomedical_literacy_level = [v if isinstance(v, LiteracyLevel) else LiteracyLevel(v) for v in self.biomedical_literacy_level]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecondaryUser(YAMLRoot):
    """
    Secondary user of tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["SecondaryUser"]
    class_class_curie: ClassVar[str] = "schema:SecondaryUser"
    class_name: ClassVar[str] = "SecondaryUser"
    class_model_uri: ClassVar[URIRef] = SCHEMA.SecondaryUser

    user_type: Union[str, SecondaryUserTypeOrString] = None
    technical_literacy_level: Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]] = None
    biomedical_literacy_level: Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.user_type):
            self.MissingRequiredField("user_type")
        if not isinstance(self.user_type, SecondaryUserTypeOrString):
            self.user_type = SecondaryUserTypeOrString(self.user_type)

        if self._is_empty(self.technical_literacy_level):
            self.MissingRequiredField("technical_literacy_level")
        if not isinstance(self.technical_literacy_level, list):
            self.technical_literacy_level = [self.technical_literacy_level] if self.technical_literacy_level is not None else []
        self.technical_literacy_level = [v if isinstance(v, LiteracyLevel) else LiteracyLevel(v) for v in self.technical_literacy_level]

        if self._is_empty(self.biomedical_literacy_level):
            self.MissingRequiredField("biomedical_literacy_level")
        if not isinstance(self.biomedical_literacy_level, list):
            self.biomedical_literacy_level = [self.biomedical_literacy_level] if self.biomedical_literacy_level is not None else []
        self.biomedical_literacy_level = [v if isinstance(v, LiteracyLevel) else LiteracyLevel(v) for v in self.biomedical_literacy_level]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TargetUsers(YAMLRoot):
    """
    Target users of application
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["TargetUsers"]
    class_class_curie: ClassVar[str] = "schema:TargetUsers"
    class_name: ClassVar[str] = "TargetUsers"
    class_model_uri: ClassVar[URIRef] = SCHEMA.TargetUsers

    primary_user: Union[dict, PrimaryUser] = None
    secondary_user: Optional[Union[dict, SecondaryUser]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.primary_user):
            self.MissingRequiredField("primary_user")
        if not isinstance(self.primary_user, PrimaryUser):
            self.primary_user = PrimaryUser(**as_dict(self.primary_user))

        if self.secondary_user is not None and not isinstance(self.secondary_user, SecondaryUser):
            self.secondary_user = SecondaryUser(**as_dict(self.secondary_user))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Media(YAMLRoot):
    """
    Media resources associated with your tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Media"]
    class_class_curie: ClassVar[str] = "schema:Media"
    class_name: ClassVar[str] = "Media"
    class_model_uri: ClassVar[URIRef] = SCHEMA.Media

    link: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.link is not None and not isinstance(self.link, str):
            self.link = str(self.link)

        super().__post_init__(**kwargs)


# Enumerations
class FileFormat(EnumDefinitionImpl):

    csv = PermissibleValue(
        text="csv",
        description="csv")
    tsv = PermissibleValue(
        text="tsv",
        description="tsv")
    xlsx = PermissibleValue(
        text="xlsx",
        description="xlsx")
    txt = PermissibleValue(
        text="txt",
        description="txt")
    json = PermissibleValue(
        text="json",
        description="json")
    none = PermissibleValue(
        text="none",
        description="none")
    dataframe = PermissibleValue(
        text="dataframe",
        description="dataframe")
    pdf = PermissibleValue(
        text="pdf",
        description="pdf")
    docx = PermissibleValue(
        text="docx",
        description="docx")
    various = PermissibleValue(
        text="various",
        description="various")
    dicom = PermissibleValue(
        text="dicom",
        description="dicom")
    images = PermissibleValue(
        text="images",
        description="images")
    markdown = PermissibleValue(
        text="markdown",
        description="markdown")

    _defn = EnumDefinition(
        name="FileFormat",
    )

class DataCategory(EnumDefinitionImpl):

    imaging = PermissibleValue(text="imaging")
    audio = PermissibleValue(text="audio")

    _defn = EnumDefinition(
        name="DataCategory",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "clinical-phenotype",
            PermissibleValue(text="clinical-phenotype"))
        setattr(cls, "omics-molecular",
            PermissibleValue(text="omics-molecular"))

class DataClass(EnumDefinitionImpl):

    tabular = PermissibleValue(text="tabular")
    image = PermissibleValue(text="image")
    matrix = PermissibleValue(text="matrix")
    sequence = PermissibleValue(text="sequence")
    structured = PermissibleValue(text="structured")
    document = PermissibleValue(text="document")
    other = PermissibleValue(text="other")
    text = PermissibleValue(text="text")

    _defn = EnumDefinition(
        name="DataClass",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unstructured-text",
            PermissibleValue(text="unstructured-text"))
        setattr(cls, "graph-or-network",
            PermissibleValue(text="graph-or-network"))
        setattr(cls, "text-and-dictionaries",
            PermissibleValue(text="text-and-dictionaries"))
        setattr(cls, "text-and-hyperlinks",
            PermissibleValue(text="text-and-hyperlinks"))
        setattr(cls, "data-viz",
            PermissibleValue(text="data-viz"))

class DataType(EnumDefinitionImpl):

    genomics = PermissibleValue(text="genomics")
    proteomics = PermissibleValue(text="proteomics")
    metabolomics = PermissibleValue(text="metabolomics")

    _defn = EnumDefinition(
        name="DataType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "clinical-ehr",
            PermissibleValue(text="clinical-ehr"))
        setattr(cls, "digital-pathology",
            PermissibleValue(text="digital-pathology"))

class DataStandard(EnumDefinitionImpl):

    FHIR = PermissibleValue(text="FHIR")
    OMOP = PermissibleValue(text="OMOP")
    DICOM = PermissibleValue(text="DICOM")
    GDC = PermissibleValue(text="GDC")
    PDC = PermissibleValue(text="PDC")
    Synapse = PermissibleValue(text="Synapse")
    JSONSchema = PermissibleValue(text="JSONSchema")

    _defn = EnumDefinition(
        name="DataStandard",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(text="None"))

class LLMRequirementReason(EnumDefinitionImpl):

    performance = PermissibleValue(text="performance")
    cost = PermissibleValue(text="cost")

    _defn = EnumDefinition(
        name="LLMRequirementReason",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "open-source",
            PermissibleValue(text="open-source"))

class LLMModel(EnumDefinitionImpl):

    gpt2 = PermissibleValue(text="gpt2")
    gpt3 = PermissibleValue(text="gpt3")
    gpt4 = PermissibleValue(text="gpt4")
    gpt4o = PermissibleValue(text="gpt4o")
    openai = PermissibleValue(text="openai")
    anthropic = PermissibleValue(text="anthropic")
    ollama = PermissibleValue(text="ollama")
    gemini = PermissibleValue(text="gemini")
    llama = PermissibleValue(text="llama")

    _defn = EnumDefinition(
        name="LLMModel",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gpt4o-mini",
            PermissibleValue(text="gpt4o-mini"))
        setattr(cls, "claude3-5sonnet",
            PermissibleValue(text="claude3-5sonnet"))
        setattr(cls, "claude3-7",
            PermissibleValue(text="claude3-7"))
        setattr(cls, "google-ai",
            PermissibleValue(text="google-ai"))
        setattr(cls, "gemini-flash",
            PermissibleValue(text="gemini-flash"))
        setattr(cls, "Meta-Llama-3.1-8B-Instruct",
            PermissibleValue(text="Meta-Llama-3.1-8B-Instruct"))

class CloudProvider(EnumDefinitionImpl):

    aws = PermissibleValue(text="aws")
    azure = PermissibleValue(text="azure")
    gcp = PermissibleValue(text="gcp")
    oracle = PermissibleValue(text="oracle")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="CloudProvider",
    )

class LicenseType(EnumDefinitionImpl):

    AAL = PermissibleValue(text="AAL")
    ADSL = PermissibleValue(text="ADSL")
    AMDPLPA = PermissibleValue(text="AMDPLPA")
    AML = PermissibleValue(text="AML")
    AMPAS = PermissibleValue(text="AMPAS")
    APAFML = PermissibleValue(text="APAFML")
    Abstyles = PermissibleValue(text="Abstyles")
    Afmparse = PermissibleValue(text="Afmparse")
    Aladdin = PermissibleValue(text="Aladdin")
    Bahyph = PermissibleValue(text="Bahyph")
    Barr = PermissibleValue(text="Barr")
    Beerware = PermissibleValue(text="Beerware")
    Borceux = PermissibleValue(text="Borceux")
    Caldera = PermissibleValue(text="Caldera")
    ClArtistic = PermissibleValue(text="ClArtistic")
    Crossword = PermissibleValue(text="Crossword")
    CrystalStacker = PermissibleValue(text="CrystalStacker")
    Cube = PermissibleValue(text="Cube")
    DOC = PermissibleValue(text="DOC")
    DSDP = PermissibleValue(text="DSDP")
    Dotseqn = PermissibleValue(text="Dotseqn")
    EUDatagrid = PermissibleValue(text="EUDatagrid")
    Entessa = PermissibleValue(text="Entessa")
    Eurosym = PermissibleValue(text="Eurosym")
    FSFAP = PermissibleValue(text="FSFAP")
    FSFUL = PermissibleValue(text="FSFUL")
    FSFULLR = PermissibleValue(text="FSFULLR")
    FTL = PermissibleValue(text="FTL")
    Fair = PermissibleValue(text="Fair")
    FreeImage = PermissibleValue(text="FreeImage")
    GL2PS = PermissibleValue(text="GL2PS")
    Giftware = PermissibleValue(text="Giftware")
    Glide = PermissibleValue(text="Glide")
    Glulxe = PermissibleValue(text="Glulxe")
    HPND = PermissibleValue(text="HPND")
    HaskellReport = PermissibleValue(text="HaskellReport")
    ICU = PermissibleValue(text="ICU")
    IJG = PermissibleValue(text="IJG")
    IPA = PermissibleValue(text="IPA")
    ISC = PermissibleValue(text="ISC")
    ImageMagick = PermissibleValue(text="ImageMagick")
    Imlib2 = PermissibleValue(text="Imlib2")
    Intel = PermissibleValue(text="Intel")
    JSON = PermissibleValue(text="JSON")
    LGPLLR = PermissibleValue(text="LGPLLR")
    Latex2e = PermissibleValue(text="Latex2e")
    Leptonica = PermissibleValue(text="Leptonica")
    Libpng = PermissibleValue(text="Libpng")
    MIT = PermissibleValue(text="MIT")
    MITNFA = PermissibleValue(text="MITNFA")
    MTLL = PermissibleValue(text="MTLL")
    MakeIndex = PermissibleValue(text="MakeIndex")
    MirOS = PermissibleValue(text="MirOS")
    Motosoto = PermissibleValue(text="Motosoto")
    Multics = PermissibleValue(text="Multics")
    Mup = PermissibleValue(text="Mup")
    NCSA = PermissibleValue(text="NCSA")
    NGPL = PermissibleValue(text="NGPL")
    NLPL = PermissibleValue(text="NLPL")
    NOSL = PermissibleValue(text="NOSL")
    NRL = PermissibleValue(text="NRL")
    NTP = PermissibleValue(text="NTP")
    Naumen = PermissibleValue(text="Naumen")
    NetCDF = PermissibleValue(text="NetCDF")
    Newsletr = PermissibleValue(text="Newsletr")
    Nokia = PermissibleValue(text="Nokia")
    Noweb = PermissibleValue(text="Noweb")
    Nunit = PermissibleValue(text="Nunit")
    OGTSL = PermissibleValue(text="OGTSL")
    OML = PermissibleValue(text="OML")
    OpenSSL = PermissibleValue(text="OpenSSL")
    Plexus = PermissibleValue(text="Plexus")
    PostgreSQL = PermissibleValue(text="PostgreSQL")
    Qhull = PermissibleValue(text="Qhull")
    RSCPL = PermissibleValue(text="RSCPL")
    Rdisc = PermissibleValue(text="Rdisc")
    Ruby = PermissibleValue(text="Ruby")
    SCEA = PermissibleValue(text="SCEA")
    SISSL = PermissibleValue(text="SISSL")
    SMLNJ = PermissibleValue(text="SMLNJ")
    SMPPL = PermissibleValue(text="SMPPL")
    SNIA = PermissibleValue(text="SNIA")
    SWL = PermissibleValue(text="SWL")
    Saxpath = PermissibleValue(text="Saxpath")
    Sendmail = PermissibleValue(text="Sendmail")
    Sleepycat = PermissibleValue(text="Sleepycat")
    TCL = PermissibleValue(text="TCL")
    TMate = PermissibleValue(text="TMate")
    TOSL = PermissibleValue(text="TOSL")
    Unlicense = PermissibleValue(text="Unlicense")
    VOSTROM = PermissibleValue(text="VOSTROM")
    Vim = PermissibleValue(text="Vim")
    W3C = PermissibleValue(text="W3C")
    WTFPL = PermissibleValue(text="WTFPL")
    Wsuipa = PermissibleValue(text="Wsuipa")
    X11 = PermissibleValue(text="X11")
    XSkat = PermissibleValue(text="XSkat")
    Xerox = PermissibleValue(text="Xerox")
    Xnet = PermissibleValue(text="Xnet")
    Zed = PermissibleValue(text="Zed")
    Zlib = PermissibleValue(text="Zlib")
    curl = PermissibleValue(text="curl")
    diffmark = PermissibleValue(text="diffmark")
    dvipdfm = PermissibleValue(text="dvipdfm")
    eGenix = PermissibleValue(text="eGenix")
    gnuplot = PermissibleValue(text="gnuplot")
    iMatix = PermissibleValue(text="iMatix")
    libtiff = PermissibleValue(text="libtiff")
    mpich2 = PermissibleValue(text="mpich2")
    psfrag = PermissibleValue(text="psfrag")
    psutils = PermissibleValue(text="psutils")
    xinetd = PermissibleValue(text="xinetd")
    xpp = PermissibleValue(text="xpp")
    Proprietary = PermissibleValue(text="Proprietary")
    Other = PermissibleValue(text="Other")
    Freeware = PermissibleValue(text="Freeware")

    _defn = EnumDefinition(
        name="LicenseType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0BSD",
            PermissibleValue(text="0BSD"))
        setattr(cls, "AFL-1.1",
            PermissibleValue(text="AFL-1.1"))
        setattr(cls, "AFL-1.2",
            PermissibleValue(text="AFL-1.2"))
        setattr(cls, "AFL-2.0",
            PermissibleValue(text="AFL-2.0"))
        setattr(cls, "AFL-2.1",
            PermissibleValue(text="AFL-2.1"))
        setattr(cls, "AFL-3.0",
            PermissibleValue(text="AFL-3.0"))
        setattr(cls, "AGPL-1.0",
            PermissibleValue(text="AGPL-1.0"))
        setattr(cls, "AGPL-3.0",
            PermissibleValue(text="AGPL-3.0"))
        setattr(cls, "ANTLR-PD",
            PermissibleValue(text="ANTLR-PD"))
        setattr(cls, "APL-1.0",
            PermissibleValue(text="APL-1.0"))
        setattr(cls, "APSL-1.0",
            PermissibleValue(text="APSL-1.0"))
        setattr(cls, "APSL-1.1",
            PermissibleValue(text="APSL-1.1"))
        setattr(cls, "APSL-1.2",
            PermissibleValue(text="APSL-1.2"))
        setattr(cls, "APSL-2.0",
            PermissibleValue(text="APSL-2.0"))
        setattr(cls, "Adobe-2006",
            PermissibleValue(text="Adobe-2006"))
        setattr(cls, "Adobe-Glyph",
            PermissibleValue(text="Adobe-Glyph"))
        setattr(cls, "Apache-1.0",
            PermissibleValue(text="Apache-1.0"))
        setattr(cls, "Apache-1.1",
            PermissibleValue(text="Apache-1.1"))
        setattr(cls, "Apache-2.0",
            PermissibleValue(text="Apache-2.0"))
        setattr(cls, "Artistic-1.0",
            PermissibleValue(text="Artistic-1.0"))
        setattr(cls, "Artistic-1.0-Perl",
            PermissibleValue(text="Artistic-1.0-Perl"))
        setattr(cls, "Artistic-1.0-cl8",
            PermissibleValue(text="Artistic-1.0-cl8"))
        setattr(cls, "Artistic-2.0",
            PermissibleValue(text="Artistic-2.0"))
        setattr(cls, "BSD-2-Clause",
            PermissibleValue(text="BSD-2-Clause"))
        setattr(cls, "BSD-2-Clause-FreeBSD",
            PermissibleValue(text="BSD-2-Clause-FreeBSD"))
        setattr(cls, "BSD-2-Clause-NetBSD",
            PermissibleValue(text="BSD-2-Clause-NetBSD"))
        setattr(cls, "BSD-3-Clause",
            PermissibleValue(text="BSD-3-Clause"))
        setattr(cls, "BSD-3-Clause-Attribution",
            PermissibleValue(text="BSD-3-Clause-Attribution"))
        setattr(cls, "BSD-3-Clause-Clear",
            PermissibleValue(text="BSD-3-Clause-Clear"))
        setattr(cls, "BSD-3-Clause-LBNL",
            PermissibleValue(text="BSD-3-Clause-LBNL"))
        setattr(cls, "BSD-3-Clause-No-Nuclear-License",
            PermissibleValue(text="BSD-3-Clause-No-Nuclear-License"))
        setattr(cls, "BSD-3-Clause-No-Nuclear-License-2014",
            PermissibleValue(text="BSD-3-Clause-No-Nuclear-License-2014"))
        setattr(cls, "BSD-3-Clause-No-Nuclear-Warranty",
            PermissibleValue(text="BSD-3-Clause-No-Nuclear-Warranty"))
        setattr(cls, "BSD-4-Clause",
            PermissibleValue(text="BSD-4-Clause"))
        setattr(cls, "BSD-4-Clause-UC",
            PermissibleValue(text="BSD-4-Clause-UC"))
        setattr(cls, "BSD-Protection",
            PermissibleValue(text="BSD-Protection"))
        setattr(cls, "BSD-Source-Code",
            PermissibleValue(text="BSD-Source-Code"))
        setattr(cls, "BSL-1.0",
            PermissibleValue(text="BSL-1.0"))
        setattr(cls, "BitTorrent-1.0",
            PermissibleValue(text="BitTorrent-1.0"))
        setattr(cls, "BitTorrent-1.1",
            PermissibleValue(text="BitTorrent-1.1"))
        setattr(cls, "CATOSL-1.1",
            PermissibleValue(text="CATOSL-1.1"))
        setattr(cls, "CC-BY-1.0",
            PermissibleValue(text="CC-BY-1.0"))
        setattr(cls, "CC-BY-2.0",
            PermissibleValue(text="CC-BY-2.0"))
        setattr(cls, "CC-BY-2.5",
            PermissibleValue(text="CC-BY-2.5"))
        setattr(cls, "CC-BY-3.0",
            PermissibleValue(text="CC-BY-3.0"))
        setattr(cls, "CC-BY-4.0",
            PermissibleValue(text="CC-BY-4.0"))
        setattr(cls, "CC-BY-NC-1.0",
            PermissibleValue(text="CC-BY-NC-1.0"))
        setattr(cls, "CC-BY-NC-2.0",
            PermissibleValue(text="CC-BY-NC-2.0"))
        setattr(cls, "CC-BY-NC-2.5",
            PermissibleValue(text="CC-BY-NC-2.5"))
        setattr(cls, "CC-BY-NC-3.0",
            PermissibleValue(text="CC-BY-NC-3.0"))
        setattr(cls, "CC-BY-NC-4.0",
            PermissibleValue(text="CC-BY-NC-4.0"))
        setattr(cls, "CC-BY-NC-ND-1.0",
            PermissibleValue(text="CC-BY-NC-ND-1.0"))
        setattr(cls, "CC-BY-NC-ND-2.0",
            PermissibleValue(text="CC-BY-NC-ND-2.0"))
        setattr(cls, "CC-BY-NC-ND-2.5",
            PermissibleValue(text="CC-BY-NC-ND-2.5"))
        setattr(cls, "CC-BY-NC-ND-3.0",
            PermissibleValue(text="CC-BY-NC-ND-3.0"))
        setattr(cls, "CC-BY-NC-ND-4.0",
            PermissibleValue(text="CC-BY-NC-ND-4.0"))
        setattr(cls, "CC-BY-NC-SA-1.0",
            PermissibleValue(text="CC-BY-NC-SA-1.0"))
        setattr(cls, "CC-BY-NC-SA-2.0",
            PermissibleValue(text="CC-BY-NC-SA-2.0"))
        setattr(cls, "CC-BY-NC-SA-2.5",
            PermissibleValue(text="CC-BY-NC-SA-2.5"))
        setattr(cls, "CC-BY-NC-SA-3.0",
            PermissibleValue(text="CC-BY-NC-SA-3.0"))
        setattr(cls, "CC-BY-NC-SA-4.0",
            PermissibleValue(text="CC-BY-NC-SA-4.0"))
        setattr(cls, "CC-BY-ND-1.0",
            PermissibleValue(text="CC-BY-ND-1.0"))
        setattr(cls, "CC-BY-ND-2.0",
            PermissibleValue(text="CC-BY-ND-2.0"))
        setattr(cls, "CC-BY-ND-2.5",
            PermissibleValue(text="CC-BY-ND-2.5"))
        setattr(cls, "CC-BY-ND-3.0",
            PermissibleValue(text="CC-BY-ND-3.0"))
        setattr(cls, "CC-BY-ND-4.0",
            PermissibleValue(text="CC-BY-ND-4.0"))
        setattr(cls, "CC-BY-SA-1.0",
            PermissibleValue(text="CC-BY-SA-1.0"))
        setattr(cls, "CC-BY-SA-2.0",
            PermissibleValue(text="CC-BY-SA-2.0"))
        setattr(cls, "CC-BY-SA-2.5",
            PermissibleValue(text="CC-BY-SA-2.5"))
        setattr(cls, "CC-BY-SA-3.0",
            PermissibleValue(text="CC-BY-SA-3.0"))
        setattr(cls, "CC-BY-SA-4.0",
            PermissibleValue(text="CC-BY-SA-4.0"))
        setattr(cls, "CC0-1.0",
            PermissibleValue(text="CC0-1.0"))
        setattr(cls, "CDDL-1.0",
            PermissibleValue(text="CDDL-1.0"))
        setattr(cls, "CDDL-1.1",
            PermissibleValue(text="CDDL-1.1"))
        setattr(cls, "CECILL-1.0",
            PermissibleValue(text="CECILL-1.0"))
        setattr(cls, "CECILL-1.1",
            PermissibleValue(text="CECILL-1.1"))
        setattr(cls, "CECILL-2.0",
            PermissibleValue(text="CECILL-2.0"))
        setattr(cls, "CECILL-2.1",
            PermissibleValue(text="CECILL-2.1"))
        setattr(cls, "CECILL-B",
            PermissibleValue(text="CECILL-B"))
        setattr(cls, "CECILL-C",
            PermissibleValue(text="CECILL-C"))
        setattr(cls, "CNRI-Jython",
            PermissibleValue(text="CNRI-Jython"))
        setattr(cls, "CNRI-Python",
            PermissibleValue(text="CNRI-Python"))
        setattr(cls, "CNRI-Python-GPL-Compatible",
            PermissibleValue(text="CNRI-Python-GPL-Compatible"))
        setattr(cls, "CPAL-1.0",
            PermissibleValue(text="CPAL-1.0"))
        setattr(cls, "CPL-1.0",
            PermissibleValue(text="CPL-1.0"))
        setattr(cls, "CPOL-1.02",
            PermissibleValue(text="CPOL-1.02"))
        setattr(cls, "CUA-OPL-1.0",
            PermissibleValue(text="CUA-OPL-1.0"))
        setattr(cls, "Condor-1.1",
            PermissibleValue(text="Condor-1.1"))
        setattr(cls, "D-FSL-1.0",
            PermissibleValue(text="D-FSL-1.0"))
        setattr(cls, "ECL-1.0",
            PermissibleValue(text="ECL-1.0"))
        setattr(cls, "ECL-2.0",
            PermissibleValue(text="ECL-2.0"))
        setattr(cls, "EFL-1.0",
            PermissibleValue(text="EFL-1.0"))
        setattr(cls, "EFL-2.0",
            PermissibleValue(text="EFL-2.0"))
        setattr(cls, "EPL-1.0",
            PermissibleValue(text="EPL-1.0"))
        setattr(cls, "EUPL-1.0",
            PermissibleValue(text="EUPL-1.0"))
        setattr(cls, "EUPL-1.1",
            PermissibleValue(text="EUPL-1.1"))
        setattr(cls, "ErlPL-1.1",
            PermissibleValue(text="ErlPL-1.1"))
        setattr(cls, "Frameworx-1.0",
            PermissibleValue(text="Frameworx-1.0"))
        setattr(cls, "GFDL-1.1",
            PermissibleValue(text="GFDL-1.1"))
        setattr(cls, "GFDL-1.2",
            PermissibleValue(text="GFDL-1.2"))
        setattr(cls, "GFDL-1.3",
            PermissibleValue(text="GFDL-1.3"))
        setattr(cls, "GPL-1.0",
            PermissibleValue(text="GPL-1.0"))
        setattr(cls, "GPL-2.0",
            PermissibleValue(text="GPL-2.0"))
        setattr(cls, "GPL-3.0",
            PermissibleValue(text="GPL-3.0"))
        setattr(cls, "IBM-pibs",
            PermissibleValue(text="IBM-pibs"))
        setattr(cls, "IPL-1.0",
            PermissibleValue(text="IPL-1.0"))
        setattr(cls, "Info-ZIP",
            PermissibleValue(text="Info-ZIP"))
        setattr(cls, "Intel-ACPI",
            PermissibleValue(text="Intel-ACPI"))
        setattr(cls, "Interbase-1.0",
            PermissibleValue(text="Interbase-1.0"))
        setattr(cls, "JasPer-2.0",
            PermissibleValue(text="JasPer-2.0"))
        setattr(cls, "LAL-1.2",
            PermissibleValue(text="LAL-1.2"))
        setattr(cls, "LAL-1.3",
            PermissibleValue(text="LAL-1.3"))
        setattr(cls, "LGPL-2.0",
            PermissibleValue(text="LGPL-2.0"))
        setattr(cls, "LGPL-2.1",
            PermissibleValue(text="LGPL-2.1"))
        setattr(cls, "LGPL-3.0",
            PermissibleValue(text="LGPL-3.0"))
        setattr(cls, "LPL-1.0",
            PermissibleValue(text="LPL-1.0"))
        setattr(cls, "LPL-1.02",
            PermissibleValue(text="LPL-1.02"))
        setattr(cls, "LPPL-1.0",
            PermissibleValue(text="LPPL-1.0"))
        setattr(cls, "LPPL-1.1",
            PermissibleValue(text="LPPL-1.1"))
        setattr(cls, "LPPL-1.2",
            PermissibleValue(text="LPPL-1.2"))
        setattr(cls, "LPPL-1.3a",
            PermissibleValue(text="LPPL-1.3a"))
        setattr(cls, "LPPL-1.3c",
            PermissibleValue(text="LPPL-1.3c"))
        setattr(cls, "LiLiQ-P-1.1",
            PermissibleValue(text="LiLiQ-P-1.1"))
        setattr(cls, "LiLiQ-R-1.1",
            PermissibleValue(text="LiLiQ-R-1.1"))
        setattr(cls, "LiLiQ-Rplus-1.1",
            PermissibleValue(text="LiLiQ-Rplus-1.1"))
        setattr(cls, "MIT-CMU",
            PermissibleValue(text="MIT-CMU"))
        setattr(cls, "MIT-advertising",
            PermissibleValue(text="MIT-advertising"))
        setattr(cls, "MIT-enna",
            PermissibleValue(text="MIT-enna"))
        setattr(cls, "MIT-feh",
            PermissibleValue(text="MIT-feh"))
        setattr(cls, "MPL-1.0",
            PermissibleValue(text="MPL-1.0"))
        setattr(cls, "MPL-1.1",
            PermissibleValue(text="MPL-1.1"))
        setattr(cls, "MPL-2.0",
            PermissibleValue(text="MPL-2.0"))
        setattr(cls, "MPL-2.0-no-copyleft-exception",
            PermissibleValue(text="MPL-2.0-no-copyleft-exception"))
        setattr(cls, "MS-PL",
            PermissibleValue(text="MS-PL"))
        setattr(cls, "MS-RL",
            PermissibleValue(text="MS-RL"))
        setattr(cls, "NASA-1.3",
            PermissibleValue(text="NASA-1.3"))
        setattr(cls, "NBPL-1.0",
            PermissibleValue(text="NBPL-1.0"))
        setattr(cls, "NLOD-1.0",
            PermissibleValue(text="NLOD-1.0"))
        setattr(cls, "NPL-1.0",
            PermissibleValue(text="NPL-1.0"))
        setattr(cls, "NPL-1.1",
            PermissibleValue(text="NPL-1.1"))
        setattr(cls, "NPOSL-3.0",
            PermissibleValue(text="NPOSL-3.0"))
        setattr(cls, "OCCT-PL",
            PermissibleValue(text="OCCT-PL"))
        setattr(cls, "OCLC-2.0",
            PermissibleValue(text="OCLC-2.0"))
        setattr(cls, "ODbL-1.0",
            PermissibleValue(text="ODbL-1.0"))
        setattr(cls, "OFL-1.0",
            PermissibleValue(text="OFL-1.0"))
        setattr(cls, "OFL-1.1",
            PermissibleValue(text="OFL-1.1"))
        setattr(cls, "OLDAP-1.1",
            PermissibleValue(text="OLDAP-1.1"))
        setattr(cls, "OLDAP-1.2",
            PermissibleValue(text="OLDAP-1.2"))
        setattr(cls, "OLDAP-1.3",
            PermissibleValue(text="OLDAP-1.3"))
        setattr(cls, "OLDAP-1.4",
            PermissibleValue(text="OLDAP-1.4"))
        setattr(cls, "OLDAP-2.0",
            PermissibleValue(text="OLDAP-2.0"))
        setattr(cls, "OLDAP-2.0.1",
            PermissibleValue(text="OLDAP-2.0.1"))
        setattr(cls, "OLDAP-2.1",
            PermissibleValue(text="OLDAP-2.1"))
        setattr(cls, "OLDAP-2.2",
            PermissibleValue(text="OLDAP-2.2"))
        setattr(cls, "OLDAP-2.2.1",
            PermissibleValue(text="OLDAP-2.2.1"))
        setattr(cls, "OLDAP-2.2.2",
            PermissibleValue(text="OLDAP-2.2.2"))
        setattr(cls, "OLDAP-2.3",
            PermissibleValue(text="OLDAP-2.3"))
        setattr(cls, "OLDAP-2.4",
            PermissibleValue(text="OLDAP-2.4"))
        setattr(cls, "OLDAP-2.5",
            PermissibleValue(text="OLDAP-2.5"))
        setattr(cls, "OLDAP-2.6",
            PermissibleValue(text="OLDAP-2.6"))
        setattr(cls, "OLDAP-2.7",
            PermissibleValue(text="OLDAP-2.7"))
        setattr(cls, "OLDAP-2.8",
            PermissibleValue(text="OLDAP-2.8"))
        setattr(cls, "OPL-1.0",
            PermissibleValue(text="OPL-1.0"))
        setattr(cls, "OSET-PL-2.1",
            PermissibleValue(text="OSET-PL-2.1"))
        setattr(cls, "OSL-1.0",
            PermissibleValue(text="OSL-1.0"))
        setattr(cls, "OSL-1.1",
            PermissibleValue(text="OSL-1.1"))
        setattr(cls, "OSL-2.0",
            PermissibleValue(text="OSL-2.0"))
        setattr(cls, "OSL-2.1",
            PermissibleValue(text="OSL-2.1"))
        setattr(cls, "OSL-3.0",
            PermissibleValue(text="OSL-3.0"))
        setattr(cls, "PDDL-1.0",
            PermissibleValue(text="PDDL-1.0"))
        setattr(cls, "PHP-3.0",
            PermissibleValue(text="PHP-3.0"))
        setattr(cls, "PHP-3.01",
            PermissibleValue(text="PHP-3.01"))
        setattr(cls, "Python-2.0",
            PermissibleValue(text="Python-2.0"))
        setattr(cls, "QPL-1.0",
            PermissibleValue(text="QPL-1.0"))
        setattr(cls, "RHeCos-1.1",
            PermissibleValue(text="RHeCos-1.1"))
        setattr(cls, "RPL-1.1",
            PermissibleValue(text="RPL-1.1"))
        setattr(cls, "RPL-1.5",
            PermissibleValue(text="RPL-1.5"))
        setattr(cls, "RPSL-1.0",
            PermissibleValue(text="RPSL-1.0"))
        setattr(cls, "RSA-MD",
            PermissibleValue(text="RSA-MD"))
        setattr(cls, "SAX-PD",
            PermissibleValue(text="SAX-PD"))
        setattr(cls, "SGI-B-1.0",
            PermissibleValue(text="SGI-B-1.0"))
        setattr(cls, "SGI-B-1.1",
            PermissibleValue(text="SGI-B-1.1"))
        setattr(cls, "SGI-B-2.0",
            PermissibleValue(text="SGI-B-2.0"))
        setattr(cls, "SISSL-1.2",
            PermissibleValue(text="SISSL-1.2"))
        setattr(cls, "SPL-1.0",
            PermissibleValue(text="SPL-1.0"))
        setattr(cls, "SimPL-2.0",
            PermissibleValue(text="SimPL-2.0"))
        setattr(cls, "Spencer-86",
            PermissibleValue(text="Spencer-86"))
        setattr(cls, "Spencer-94",
            PermissibleValue(text="Spencer-94"))
        setattr(cls, "Spencer-99",
            PermissibleValue(text="Spencer-99"))
        setattr(cls, "SugarCRM-1.1.3",
            PermissibleValue(text="SugarCRM-1.1.3"))
        setattr(cls, "TORQUE-1.1",
            PermissibleValue(text="TORQUE-1.1"))
        setattr(cls, "UPL-1.0",
            PermissibleValue(text="UPL-1.0"))
        setattr(cls, "Unicode-TOU",
            PermissibleValue(text="Unicode-TOU"))
        setattr(cls, "VSL-1.0",
            PermissibleValue(text="VSL-1.0"))
        setattr(cls, "W3C-19980720",
            PermissibleValue(text="W3C-19980720"))
        setattr(cls, "Watcom-1.0",
            PermissibleValue(text="Watcom-1.0"))
        setattr(cls, "XFree86-1.1",
            PermissibleValue(text="XFree86-1.1"))
        setattr(cls, "YPL-1.0",
            PermissibleValue(text="YPL-1.0"))
        setattr(cls, "YPL-1.1",
            PermissibleValue(text="YPL-1.1"))
        setattr(cls, "ZPL-1.1",
            PermissibleValue(text="ZPL-1.1"))
        setattr(cls, "ZPL-2.0",
            PermissibleValue(text="ZPL-2.0"))
        setattr(cls, "ZPL-2.1",
            PermissibleValue(text="ZPL-2.1"))
        setattr(cls, "Zend-2.0",
            PermissibleValue(text="Zend-2.0"))
        setattr(cls, "Zimbra-1.3",
            PermissibleValue(text="Zimbra-1.3"))
        setattr(cls, "Zimbra-1.4",
            PermissibleValue(text="Zimbra-1.4"))
        setattr(cls, "bzip2-1.0.5",
            PermissibleValue(text="bzip2-1.0.5"))
        setattr(cls, "bzip2-1.0.6",
            PermissibleValue(text="bzip2-1.0.6"))
        setattr(cls, "gSOAP-1.3b",
            PermissibleValue(text="gSOAP-1.3b"))
        setattr(cls, "zlib-acknowledgement",
            PermissibleValue(text="zlib-acknowledgement"))
        setattr(cls, "Not licensed",
            PermissibleValue(text="Not licensed"))

class ContributorRole(EnumDefinitionImpl):

    Developer = PermissibleValue(text="Developer")
    Maintainer = PermissibleValue(text="Maintainer")
    Provider = PermissibleValue(text="Provider")
    Documentor = PermissibleValue(text="Documentor")
    Contributor = PermissibleValue(text="Contributor")
    Support = PermissibleValue(text="Support")
    PrimaryContact = PermissibleValue(text="PrimaryContact")

    _defn = EnumDefinition(
        name="ContributorRole",
    )

class UserType(EnumDefinitionImpl):

    patient = PermissibleValue(text="patient")
    clinician = PermissibleValue(text="clinician")
    researcher = PermissibleValue(text="researcher")

    _defn = EnumDefinition(
        name="UserType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "site-admin-prepping-ehr-extracts",
            PermissibleValue(text="site-admin-prepping-ehr-extracts"))

class LiteracyLevel(EnumDefinitionImpl):

    novice = PermissibleValue(text="novice")
    intermediate = PermissibleValue(text="intermediate")
    advanced = PermissibleValue(text="advanced")
    expert = PermissibleValue(text="expert")

    _defn = EnumDefinition(
        name="LiteracyLevel",
    )

class ToolType(EnumDefinitionImpl):

    CLI = PermissibleValue(text="CLI")
    DatabasePortal = PermissibleValue(text="DatabasePortal")
    DesktopApp = PermissibleValue(text="DesktopApp")
    Library = PermissibleValue(text="Library")
    Ontology = PermissibleValue(text="Ontology")
    Plugin = PermissibleValue(text="Plugin")
    Script = PermissibleValue(text="Script")
    SPARQLEndpoint = PermissibleValue(text="SPARQLEndpoint")
    Suite = PermissibleValue(text="Suite")
    WebApp = PermissibleValue(text="WebApp")
    WebAPI = PermissibleValue(text="WebAPI")
    WebServiceSOAP = PermissibleValue(text="WebServiceSOAP")
    Workbench = PermissibleValue(text="Workbench")
    Workflow = PermissibleValue(text="Workflow")
    Notebook = PermissibleValue(text="Notebook")
    KnowledgeGraph = PermissibleValue(text="KnowledgeGraph")

    _defn = EnumDefinition(
        name="ToolType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AI/MLModel",
            PermissibleValue(text="AI/MLModel"))

# Slots
class slots:
    pass

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=SCHEMA.version, domain=None, range=str)

slots.usesLlm = Slot(uri=SCHEMA.usesLlm, name="usesLlm", curie=SCHEMA.curie('usesLlm'),
                   model_uri=SCHEMA.usesLlm, domain=None, range=Union[bool, Bool])

slots.platform = Slot(uri=SCHEMA.platform, name="platform", curie=SCHEMA.curie('platform'),
                   model_uri=SCHEMA.platform, domain=None, range=Optional[str])

slots.lastAuditDate = Slot(uri=SCHEMA.lastAuditDate, name="lastAuditDate", curie=SCHEMA.curie('lastAuditDate'),
                   model_uri=SCHEMA.lastAuditDate, domain=None, range=Union[str, XSDDateTime])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=SCHEMA.name, domain=None, range=Optional[str])

slots.format = Slot(uri=SCHEMA.format, name="format", curie=SCHEMA.curie('format'),
                   model_uri=SCHEMA.format, domain=None, range=Optional[str])

slots.proprietary = Slot(uri=SCHEMA.proprietary, name="proprietary", curie=SCHEMA.curie('proprietary'),
                   model_uri=SCHEMA.proprietary, domain=None, range=Optional[Union[bool, Bool]])

slots.source = Slot(uri=SCHEMA.source, name="source", curie=SCHEMA.curie('source'),
                   model_uri=SCHEMA.source, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=SCHEMA.description, domain=None, range=Optional[str])

slots.tools = Slot(uri=SCHEMA.tools, name="tools", curie=SCHEMA.curie('tools'),
                   model_uri=SCHEMA.tools, domain=None, range=Optional[Union[str, List[str]]])

slots.collaboration_purpose = Slot(uri=SCHEMA.collaboration_purpose, name="collaboration_purpose", curie=SCHEMA.curie('collaboration_purpose'),
                   model_uri=SCHEMA.collaboration_purpose, domain=None, range=Optional[str])

slots.agreement = Slot(uri=SCHEMA.agreement, name="agreement", curie=SCHEMA.curie('agreement'),
                   model_uri=SCHEMA.agreement, domain=None, range=Optional[str])

slots.link = Slot(uri=SCHEMA.link, name="link", curie=SCHEMA.curie('link'),
                   model_uri=SCHEMA.link, domain=None, range=Optional[Union[str, URI]])

slots.systemMetadata__version = Slot(uri=SCHEMA.version, name="systemMetadata__version", curie=SCHEMA.curie('version'),
                   model_uri=SCHEMA.systemMetadata__version, domain=None, range=string)

slots.systemMetadata__tool = Slot(uri=SCHEMA.tool, name="systemMetadata__tool", curie=SCHEMA.curie('tool'),
                   model_uri=SCHEMA.systemMetadata__tool, domain=None, range=Union[dict, ToolInfo])

slots.systemMetadata__domains = Slot(uri=SCHEMA.domains, name="systemMetadata__domains", curie=SCHEMA.curie('domains'),
                   model_uri=SCHEMA.systemMetadata__domains, domain=None, range=Union[str, List[str]])

slots.systemMetadata__llm = Slot(uri=SCHEMA.llm, name="systemMetadata__llm", curie=SCHEMA.curie('llm'),
                   model_uri=SCHEMA.systemMetadata__llm, domain=None, range=Union[dict, LlmInfo])

slots.systemMetadata__cloud = Slot(uri=SCHEMA.cloud, name="systemMetadata__cloud", curie=SCHEMA.curie('cloud'),
                   model_uri=SCHEMA.systemMetadata__cloud, domain=None, range=Optional[Union[dict, CloudInfo]])

slots.systemMetadata__input = Slot(uri=SCHEMA.input, name="systemMetadata__input", curie=SCHEMA.curie('input'),
                   model_uri=SCHEMA.systemMetadata__input, domain=None, range=Union[Union[dict, DataSource], List[Union[dict, DataSource]]])

slots.systemMetadata__output = Slot(uri=SCHEMA.output, name="systemMetadata__output", curie=SCHEMA.curie('output'),
                   model_uri=SCHEMA.systemMetadata__output, domain=None, range=Union[Union[dict, DataSource], List[Union[dict, DataSource]]])

slots.systemMetadata__collaborations = Slot(uri=SCHEMA.collaborations, name="systemMetadata__collaborations", curie=SCHEMA.curie('collaborations'),
                   model_uri=SCHEMA.systemMetadata__collaborations, domain=None, range=Union[Union[dict, Collaboration], List[Union[dict, Collaboration]]])

slots.systemMetadata__funding = Slot(uri=SCHEMA.funding, name="systemMetadata__funding", curie=SCHEMA.curie('funding'),
                   model_uri=SCHEMA.systemMetadata__funding, domain=None, range=Optional[Union[dict, FundingInfo]])

slots.systemMetadata__maturity = Slot(uri=SCHEMA.maturity, name="systemMetadata__maturity", curie=SCHEMA.curie('maturity'),
                   model_uri=SCHEMA.systemMetadata__maturity, domain=None, range=Union[dict, MaturityLevel])

slots.systemMetadata__license = Slot(uri=SCHEMA.license, name="systemMetadata__license", curie=SCHEMA.curie('license'),
                   model_uri=SCHEMA.systemMetadata__license, domain=None, range=Union[dict, License])

slots.systemMetadata__publication = Slot(uri=SCHEMA.publication, name="systemMetadata__publication", curie=SCHEMA.curie('publication'),
                   model_uri=SCHEMA.systemMetadata__publication, domain=None, range=Optional[Union[Union[dict, PublicationDetail], List[Union[dict, PublicationDetail]]]])

slots.systemMetadata__credit = Slot(uri=SCHEMA.credit, name="systemMetadata__credit", curie=SCHEMA.curie('credit'),
                   model_uri=SCHEMA.systemMetadata__credit, domain=None, range=Union[Union[dict, Credit], List[Union[dict, Credit]]])

slots.systemMetadata__target_users = Slot(uri=SCHEMA.target_users, name="systemMetadata__target_users", curie=SCHEMA.curie('target_users'),
                   model_uri=SCHEMA.systemMetadata__target_users, domain=None, range=Union[dict, TargetUsers])

slots.systemMetadata__media = Slot(uri=SCHEMA.media, name="systemMetadata__media", curie=SCHEMA.curie('media'),
                   model_uri=SCHEMA.systemMetadata__media, domain=None, range=Optional[Union[Union[dict, Media], List[Union[dict, Media]]]])

slots.llmInfo__usesLlm = Slot(uri=SCHEMA.usesLlm, name="llmInfo__usesLlm", curie=SCHEMA.curie('usesLlm'),
                   model_uri=SCHEMA.llmInfo__usesLlm, domain=None, range=Union[bool, Bool])

slots.llmInfo__modelsSupported = Slot(uri=SCHEMA.modelsSupported, name="llmInfo__modelsSupported", curie=SCHEMA.curie('modelsSupported'),
                   model_uri=SCHEMA.llmInfo__modelsSupported, domain=None, range=Optional[Union[Union[str, "LLMModel"], List[Union[str, "LLMModel"]]]])

slots.llmInfo__modelsRequired = Slot(uri=SCHEMA.modelsRequired, name="llmInfo__modelsRequired", curie=SCHEMA.curie('modelsRequired'),
                   model_uri=SCHEMA.llmInfo__modelsRequired, domain=None, range=Optional[Union[Union[str, "LLMModel"], List[Union[str, "LLMModel"]]]])

slots.llmInfo__reasonsForRequirement = Slot(uri=SCHEMA.reasonsForRequirement, name="llmInfo__reasonsForRequirement", curie=SCHEMA.curie('reasonsForRequirement'),
                   model_uri=SCHEMA.llmInfo__reasonsForRequirement, domain=None, range=Optional[Union[Union[str, "LLMRequirementReason"], List[Union[str, "LLMRequirementReason"]]]])

slots.llmInfo__bringOwnKey = Slot(uri=SCHEMA.bringOwnKey, name="llmInfo__bringOwnKey", curie=SCHEMA.curie('bringOwnKey'),
                   model_uri=SCHEMA.llmInfo__bringOwnKey, domain=None, range=Union[bool, Bool])

slots.cloudInfo__platform = Slot(uri=SCHEMA.platform, name="cloudInfo__platform", curie=SCHEMA.curie('platform'),
                   model_uri=SCHEMA.cloudInfo__platform, domain=None, range=Union[str, "CloudProvider"])

slots.cloudInfo__lastAuditDate = Slot(uri=SCHEMA.lastAuditDate, name="cloudInfo__lastAuditDate", curie=SCHEMA.curie('lastAuditDate'),
                   model_uri=SCHEMA.cloudInfo__lastAuditDate, domain=None, range=Union[str, XSDDateTime])

slots.dataSource__name = Slot(uri=SCHEMA.name, name="dataSource__name", curie=SCHEMA.curie('name'),
                   model_uri=SCHEMA.dataSource__name, domain=None, range=str)

slots.dataSource__dataCategory = Slot(uri=SCHEMA.dataCategory, name="dataSource__dataCategory", curie=SCHEMA.curie('dataCategory'),
                   model_uri=SCHEMA.dataSource__dataCategory, domain=None, range=Union[str, DataCategoryOrString])

slots.dataSource__dataClass = Slot(uri=SCHEMA.dataClass, name="dataSource__dataClass", curie=SCHEMA.curie('dataClass'),
                   model_uri=SCHEMA.dataSource__dataClass, domain=None, range=Union[str, "DataClass"])

slots.dataSource__dataType = Slot(uri=SCHEMA.dataType, name="dataSource__dataType", curie=SCHEMA.curie('dataType'),
                   model_uri=SCHEMA.dataSource__dataType, domain=None, range=Union[str, DataTypeOrString])

slots.dataSource__dataSubType = Slot(uri=SCHEMA.dataSubType, name="dataSource__dataSubType", curie=SCHEMA.curie('dataSubType'),
                   model_uri=SCHEMA.dataSource__dataSubType, domain=None, range=Optional[str])

slots.dataSource__dataStandard = Slot(uri=SCHEMA.dataStandard, name="dataSource__dataStandard", curie=SCHEMA.curie('dataStandard'),
                   model_uri=SCHEMA.dataSource__dataStandard, domain=None, range=Union[Union[str, DataStandardOrString], List[Union[str, DataStandardOrString]]])

slots.dataSource__format = Slot(uri=SCHEMA.format, name="dataSource__format", curie=SCHEMA.curie('format'),
                   model_uri=SCHEMA.dataSource__format, domain=None, range=Union[Union[str, "FileFormat"], List[Union[str, "FileFormat"]]])

slots.dataSource__proprietary = Slot(uri=SCHEMA.proprietary, name="dataSource__proprietary", curie=SCHEMA.curie('proprietary'),
                   model_uri=SCHEMA.dataSource__proprietary, domain=None, range=Union[bool, Bool])

slots.dataSource__source = Slot(uri=SCHEMA.source, name="dataSource__source", curie=SCHEMA.curie('source'),
                   model_uri=SCHEMA.dataSource__source, domain=None, range=Optional[Union[str, URI]])

slots.collaboration__name = Slot(uri=SCHEMA.name, name="collaboration__name", curie=SCHEMA.curie('name'),
                   model_uri=SCHEMA.collaboration__name, domain=None, range=str)

slots.collaboration__description = Slot(uri=SCHEMA.description, name="collaboration__description", curie=SCHEMA.curie('description'),
                   model_uri=SCHEMA.collaboration__description, domain=None, range=str)

slots.collaboration__tools = Slot(uri=SCHEMA.tools, name="collaboration__tools", curie=SCHEMA.curie('tools'),
                   model_uri=SCHEMA.collaboration__tools, domain=None, range=Union[str, List[str]])

slots.collaboration__collaboration_purpose = Slot(uri=SCHEMA.collaboration_purpose, name="collaboration__collaboration_purpose", curie=SCHEMA.curie('collaboration_purpose'),
                   model_uri=SCHEMA.collaboration__collaboration_purpose, domain=None, range=str)

slots.fundingInfo__source = Slot(uri=SCHEMA.source, name="fundingInfo__source", curie=SCHEMA.curie('source'),
                   model_uri=SCHEMA.fundingInfo__source, domain=None, range=Optional[str])

slots.fundingInfo__agreement = Slot(uri=SCHEMA.agreement, name="fundingInfo__agreement", curie=SCHEMA.curie('agreement'),
                   model_uri=SCHEMA.fundingInfo__agreement, domain=None, range=Optional[str])

slots.fundingInfo__link = Slot(uri=SCHEMA.link, name="fundingInfo__link", curie=SCHEMA.curie('link'),
                   model_uri=SCHEMA.fundingInfo__link, domain=None, range=Optional[Union[str, URI]])

slots.toolInfo__name = Slot(uri=SCHEMA.name, name="toolInfo__name", curie=SCHEMA.curie('name'),
                   model_uri=SCHEMA.toolInfo__name, domain=None, range=str)

slots.toolInfo__repo_url = Slot(uri=SCHEMA.repo_url, name="toolInfo__repo_url", curie=SCHEMA.curie('repo_url'),
                   model_uri=SCHEMA.toolInfo__repo_url, domain=None, range=str)

slots.toolInfo__tool_homepage = Slot(uri=SCHEMA.tool_homepage, name="toolInfo__tool_homepage", curie=SCHEMA.curie('tool_homepage'),
                   model_uri=SCHEMA.toolInfo__tool_homepage, domain=None, range=str)

slots.toolInfo__documentation_url = Slot(uri=SCHEMA.documentation_url, name="toolInfo__documentation_url", curie=SCHEMA.curie('documentation_url'),
                   model_uri=SCHEMA.toolInfo__documentation_url, domain=None, range=str)

slots.toolInfo__tool_type = Slot(uri=SCHEMA.tool_type, name="toolInfo__tool_type", curie=SCHEMA.curie('tool_type'),
                   model_uri=SCHEMA.toolInfo__tool_type, domain=None, range=Union[str, "ToolType"])

slots.toolInfo__tool_notes = Slot(uri=SCHEMA.tool_notes, name="toolInfo__tool_notes", curie=SCHEMA.curie('tool_notes'),
                   model_uri=SCHEMA.toolInfo__tool_notes, domain=None, range=Optional[str])

slots.publicationDetail__type = Slot(uri=SCHEMA.type, name="publicationDetail__type", curie=SCHEMA.curie('type'),
                   model_uri=SCHEMA.publicationDetail__type, domain=None, range=Optional[str])

slots.publicationDetail__tool_version = Slot(uri=SCHEMA.tool_version, name="publicationDetail__tool_version", curie=SCHEMA.curie('tool_version'),
                   model_uri=SCHEMA.publicationDetail__tool_version, domain=None, range=Optional[string])

slots.publicationDetail__doi = Slot(uri=SCHEMA.doi, name="publicationDetail__doi", curie=SCHEMA.curie('doi'),
                   model_uri=SCHEMA.publicationDetail__doi, domain=None, range=Optional[string])

slots.publicationDetail__pmid = Slot(uri=SCHEMA.pmid, name="publicationDetail__pmid", curie=SCHEMA.curie('pmid'),
                   model_uri=SCHEMA.publicationDetail__pmid, domain=None, range=Optional[str])

slots.publicationDetail__pmcid = Slot(uri=SCHEMA.pmcid, name="publicationDetail__pmcid", curie=SCHEMA.curie('pmcid'),
                   model_uri=SCHEMA.publicationDetail__pmcid, domain=None, range=Optional[str])

slots.publicationDetail__url = Slot(uri=SCHEMA.url, name="publicationDetail__url", curie=SCHEMA.curie('url'),
                   model_uri=SCHEMA.publicationDetail__url, domain=None, range=Optional[str])

slots.license__license_type = Slot(uri=SCHEMA.license_type, name="license__license_type", curie=SCHEMA.curie('license_type'),
                   model_uri=SCHEMA.license__license_type, domain=None, range=Union[str, "LicenseType"])

slots.license__link = Slot(uri=SCHEMA.link, name="license__link", curie=SCHEMA.curie('link'),
                   model_uri=SCHEMA.license__link, domain=None, range=Optional[str])

slots.license__notes = Slot(uri=SCHEMA.notes, name="license__notes", curie=SCHEMA.curie('notes'),
                   model_uri=SCHEMA.license__notes, domain=None, range=Optional[str])

slots.credit__name = Slot(uri=SCHEMA.name, name="credit__name", curie=SCHEMA.curie('name'),
                   model_uri=SCHEMA.credit__name, domain=None, range=Optional[str])

slots.credit__email = Slot(uri=SCHEMA.email, name="credit__email", curie=SCHEMA.curie('email'),
                   model_uri=SCHEMA.credit__email, domain=None, range=Optional[Union[str, List[str]]])

slots.credit__url = Slot(uri=SCHEMA.url, name="credit__url", curie=SCHEMA.curie('url'),
                   model_uri=SCHEMA.credit__url, domain=None, range=Optional[str])

slots.credit__orcidid = Slot(uri=SCHEMA.identifier, name="credit__orcidid", curie=SCHEMA.curie('identifier'),
                   model_uri=SCHEMA.credit__orcidid, domain=None, range=Optional[str],
                   pattern=re.compile(r'^ORCID:[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'))

slots.credit__role = Slot(uri=SCHEMA.role, name="credit__role", curie=SCHEMA.curie('role'),
                   model_uri=SCHEMA.credit__role, domain=None, range=Optional[Union[str, "ContributorRole"]])

slots.credit__org = Slot(uri=SCHEMA.org, name="credit__org", curie=SCHEMA.curie('org'),
                   model_uri=SCHEMA.credit__org, domain=None, range=Optional[str])

slots.credit__note = Slot(uri=SCHEMA.note, name="credit__note", curie=SCHEMA.curie('note'),
                   model_uri=SCHEMA.credit__note, domain=None, range=Optional[str])

slots.maturityLevel__beginning_maturity = Slot(uri=SCHEMA.beginning_maturity, name="maturityLevel__beginning_maturity", curie=SCHEMA.curie('beginning_maturity'),
                   model_uri=SCHEMA.maturityLevel__beginning_maturity, domain=None, range=int)

slots.maturityLevel__current_maturity = Slot(uri=SCHEMA.current_maturity, name="maturityLevel__current_maturity", curie=SCHEMA.curie('current_maturity'),
                   model_uri=SCHEMA.maturityLevel__current_maturity, domain=None, range=int)

slots.maturityLevel__final_maturity = Slot(uri=SCHEMA.final_maturity, name="maturityLevel__final_maturity", curie=SCHEMA.curie('final_maturity'),
                   model_uri=SCHEMA.maturityLevel__final_maturity, domain=None, range=Optional[int])

slots.primaryUser__user_type = Slot(uri=SCHEMA.user_type, name="primaryUser__user_type", curie=SCHEMA.curie('user_type'),
                   model_uri=SCHEMA.primaryUser__user_type, domain=None, range=Union[str, "UserType"])

slots.primaryUser__technical_literacy_level = Slot(uri=SCHEMA.technical_literacy_level, name="primaryUser__technical_literacy_level", curie=SCHEMA.curie('technical_literacy_level'),
                   model_uri=SCHEMA.primaryUser__technical_literacy_level, domain=None, range=Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]])

slots.primaryUser__biomedical_literacy_level = Slot(uri=SCHEMA.biomedical_literacy_level, name="primaryUser__biomedical_literacy_level", curie=SCHEMA.curie('biomedical_literacy_level'),
                   model_uri=SCHEMA.primaryUser__biomedical_literacy_level, domain=None, range=Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]])

slots.secondaryUser__user_type = Slot(uri=SCHEMA.user_type, name="secondaryUser__user_type", curie=SCHEMA.curie('user_type'),
                   model_uri=SCHEMA.secondaryUser__user_type, domain=None, range=Union[str, SecondaryUserTypeOrString])

slots.secondaryUser__technical_literacy_level = Slot(uri=SCHEMA.technical_literacy_level, name="secondaryUser__technical_literacy_level", curie=SCHEMA.curie('technical_literacy_level'),
                   model_uri=SCHEMA.secondaryUser__technical_literacy_level, domain=None, range=Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]])

slots.secondaryUser__biomedical_literacy_level = Slot(uri=SCHEMA.biomedical_literacy_level, name="secondaryUser__biomedical_literacy_level", curie=SCHEMA.curie('biomedical_literacy_level'),
                   model_uri=SCHEMA.secondaryUser__biomedical_literacy_level, domain=None, range=Union[Union[str, "LiteracyLevel"], List[Union[str, "LiteracyLevel"]]])

slots.targetUsers__primary_user = Slot(uri=SCHEMA.primary_user, name="targetUsers__primary_user", curie=SCHEMA.curie('primary_user'),
                   model_uri=SCHEMA.targetUsers__primary_user, domain=None, range=Union[dict, PrimaryUser])

slots.targetUsers__secondary_user = Slot(uri=SCHEMA.secondary_user, name="targetUsers__secondary_user", curie=SCHEMA.curie('secondary_user'),
                   model_uri=SCHEMA.targetUsers__secondary_user, domain=None, range=Optional[Union[dict, SecondaryUser]])

slots.media__link = Slot(uri=SCHEMA.link, name="media__link", curie=SCHEMA.curie('link'),
                   model_uri=SCHEMA.media__link, domain=None, range=Optional[str])