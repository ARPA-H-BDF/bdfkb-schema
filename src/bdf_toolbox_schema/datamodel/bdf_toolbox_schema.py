# Auto generated from bdf_toolbox_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-17T10:02:19
# Schema: bdf-toolbox-schema
#
# id: https://w3id.org/ARPA-H-BDF/bdf-toolbox-schema
# description: Schema to describe BDF Toolbox entities and the relationships between them.
# license: Apache Software License 2.0

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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BDFT = CurieNamespace('BDFT', 'https://w3id.org/ARPA-H-BDF/bdf-toolbox-schema/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = BDFT


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ToolId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = BDFT.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(NamedThing):
    """
    Represents a Tool
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDFT["Tool"]
    class_class_curie: ClassVar[str] = "BDFT:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = BDFT.Tool

    id: Union[str, ToolId] = None
    developer_team: Optional[Union[str, "BDFPerformerTeam"]] = None
    technical_area: Optional[Union[str, "BDFTechnicalArea"]] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolId):
            self.id = ToolId(self.id)

        if self.developer_team is not None and not isinstance(self.developer_team, BDFPerformerTeam):
            self.developer_team = BDFPerformerTeam(self.developer_team)

        if self.technical_area is not None and not isinstance(self.technical_area, BDFTechnicalArea):
            self.technical_area = BDFTechnicalArea(self.technical_area)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ToolCollection(YAMLRoot):
    """
    A holder for Tool objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDFT["ToolCollection"]
    class_class_curie: ClassVar[str] = "BDFT:ToolCollection"
    class_name: ClassVar[str] = "ToolCollection"
    class_model_uri: ClassVar[URIRef] = BDFT.ToolCollection

    entries: Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Tool, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class BDFPerformerTeam(EnumDefinitionImpl):

    ASKEM_NEU = PermissibleValue(
        text="ASKEM_NEU",
        description="ASKEM - NEU")
    ASKEM_MIT = PermissibleValue(
        text="ASKEM_MIT",
        description="ASKEM - MIT")
    ASKEM_NYU = PermissibleValue(
        text="ASKEM_NYU",
        description="ASKEM - NYU")
    ASKEM_Jataware = PermissibleValue(
        text="ASKEM_Jataware",
        description="ASKEM - Jataware")
    Netrias = PermissibleValue(
        text="Netrias",
        description="Netrias")
    N3C = PermissibleValue(
        text="N3C",
        description="N3C")
    BDC = PermissibleValue(
        text="BDC",
        description="BDC")
    CRA = PermissibleValue(
        text="CRA",
        description="CRA")
    DNAHIVE = PermissibleValue(
        text="DNAHIVE",
        description="DNAHIVE")
    HMS = PermissibleValue(
        text="HMS",
        description="HMS")
    Stanford = PermissibleValue(
        text="Stanford",
        description="Stanford")
    UAB = PermissibleValue(
        text="UAB",
        description="UAB")
    ICF = PermissibleValue(
        text="ICF",
        description="ICF")
    SageBio = PermissibleValue(
        text="SageBio",
        description="SageBio")
    Insilicom = PermissibleValue(
        text="Insilicom",
        description="Insilicom")

    _defn = EnumDefinition(
        name="BDFPerformerTeam",
    )

class BDFTechnicalArea(EnumDefinitionImpl):

    TA1 = PermissibleValue(
        text="TA1",
        description="BDF Technical Area 1")
    TA2 = PermissibleValue(
        text="TA2",
        description="BDF Technical Area 2")
    TA3 = PermissibleValue(
        text="TA3",
        description="BDF Technical Area 3")

    _defn = EnumDefinition(
        name="BDFTechnicalArea",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=BDFT.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=BDFT.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=BDFT.description, domain=None, range=Optional[str])

slots.developer_team = Slot(uri=BDFT.developer_team, name="developer_team", curie=BDFT.curie('developer_team'),
                   model_uri=BDFT.developer_team, domain=None, range=Optional[Union[str, "BDFPerformerTeam"]])

slots.technical_area = Slot(uri=BDFT.technical_area, name="technical_area", curie=BDFT.curie('technical_area'),
                   model_uri=BDFT.technical_area, domain=None, range=Optional[Union[str, "BDFTechnicalArea"]])

slots.keywords = Slot(uri=BDFT.keywords, name="keywords", curie=BDFT.curie('keywords'),
                   model_uri=BDFT.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.url = Slot(uri=BDFT.url, name="url", curie=BDFT.curie('url'),
                   model_uri=BDFT.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.toolCollection__entries = Slot(uri=BDFT.entries, name="toolCollection__entries", curie=BDFT.curie('entries'),
                   model_uri=BDFT.toolCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]])