from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'schema',
     'default_range': 'string',
     'description': 'Schema for describing system metadata including LLM usage, '
                    'cloud platform, inputs, outputs, collaborations, and funding '
                    'information',
     'id': 'https://example.org/system-metadata-schema',
     'imports': ['linkml:types'],
     'name': 'system-metadata-schema',
     'prefixes': {'ORCID': {'prefix_prefix': 'ORCID',
                            'prefix_reference': 'http://identifiers.org/orcid/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'settings': {'doi_pattern': {'setting_key': 'doi_pattern',
                                  'setting_value': '^10\\.{doi_prefix}/{doi_suffix}$'},
                  'doi_prefix': {'setting_key': 'doi_prefix',
                                 'setting_value': '\\d{4,9}'},
                  'doi_suffix': {'setting_key': 'doi_suffix',
                                 'setting_value': '[-._;()/:A-Z0-9-]+'}},
     'source_file': 'src/bdfkb_schema/schema/bdfkb_schema.yaml',
     'title': 'System Metadata Schema',
     'types': {'DOIType': {'base': 'string',
                           'description': 'A Digital Object Identifier (DOI)',
                           'from_schema': 'https://example.org/system-metadata-schema',
                           'name': 'DOIType',
                           'structured_pattern': {'interpolated': True,
                                                  'partial_match': False,
                                                  'syntax': '{doi_pattern}'},
                           'uri': 'https://w3id.org/linkml/types/DOI'},
               'DataCategoryOrString': {'description': 'Type for either '
                                                       'DataCategory, or if other '
                                                       'then specify string',
                                        'from_schema': 'https://example.org/system-metadata-schema',
                                        'name': 'DataCategoryOrString',
                                        'typeof': 'string',
                                        'union_of': ["{'range': 'DataCategory'}",
                                                     "{'range': 'string'}"],
                                        'uri': 'http://schema.org/'},
               'DataStandardOrString': {'description': 'Type encompassing data '
                                                       'standards or open strings',
                                        'from_schema': 'https://example.org/system-metadata-schema',
                                        'name': 'DataStandardOrString',
                                        'typeof': 'string',
                                        'union_of': ["{'range': 'DataStandard'}",
                                                     "{'range': 'string'}"],
                                        'uri': 'http://schema.org/'},
               'DataTypeOrString': {'description': 'Type for either DataType, or '
                                                   'if other then specify string',
                                    'from_schema': 'https://example.org/system-metadata-schema',
                                    'name': 'DataTypeOrString',
                                    'typeof': 'string',
                                    'union_of': ["{'range': 'DataType'}",
                                                 "{'range': 'string'}"],
                                    'uri': 'http://schema.org/'},
               'SecondaryUserTypeOrString': {'description': 'Type for either '
                                                            'SecondaryUser, or if '
                                                            'other then specify '
                                                            'string',
                                             'from_schema': 'https://example.org/system-metadata-schema',
                                             'name': 'SecondaryUserTypeOrString',
                                             'typeof': 'string',
                                             'union_of': ["{'range': 'UserType'}",
                                                          "{'range': 'string'}"],
                                             'uri': 'http://schema.org/'},
               'SemanticVersion': {'base': 'string',
                                   'from_schema': 'https://example.org/system-metadata-schema',
                                   'name': 'SemanticVersion',
                                   'pattern': '^v?(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)(?:-[\\da-z-]+(?:\\.[\\da-z-]+)*)?(?:\\+[^\\s]*)?$',
                                   'uri': 'http://schema.org/'},
               'url': {'base': 'str',
                       'description': 'A valid HTTP or HTTPS URL',
                       'from_schema': 'https://example.org/system-metadata-schema',
                       'name': 'url',
                       'pattern': '^https?://.*$',
                       'uri': 'xsd:string'}}} )

class FileFormat(str, Enum):
    # csv
    csv = "csv"
    # tsv
    tsv = "tsv"
    # xlsx
    xlsx = "xlsx"
    # txt
    txt = "txt"
    # json
    json = "json"
    # none
    none = "none"
    # dataframe
    dataframe = "dataframe"
    # pdf
    pdf = "pdf"
    # docx
    docx = "docx"
    # various
    various = "various"
    # dicom
    dicom = "dicom"
    # images
    images = "images"
    # markdown
    markdown = "markdown"


class DataCategory(str, Enum):
    clinical_phenotype = "clinical-phenotype"
    omics_molecular = "omics-molecular"
    imaging = "imaging"
    audio = "audio"


class DataClass(str, Enum):
    unstructured_text = "unstructured-text"
    tabular = "tabular"
    image = "image"
    graph_or_network = "graph-or-network"
    matrix = "matrix"
    sequence = "sequence"
    structured = "structured"
    document = "document"
    other = "other"
    text_and_dictionaries = "text-and-dictionaries"
    text_and_hyperlinks = "text-and-hyperlinks"
    text = "text"
    data_viz = "data-viz"


class DataType(str, Enum):
    clinical_ehr = "clinical-ehr"
    genomics = "genomics"
    proteomics = "proteomics"
    metabolomics = "metabolomics"
    digital_pathology = "digital-pathology"


class DataStandard(str, Enum):
    FHIR = "FHIR"
    OMOP = "OMOP"
    DICOM = "DICOM"
    GDC = "GDC"
    PDC = "PDC"
    Synapse = "Synapse"
    None = "None"
    JSONSchema = "JSONSchema"


class LLMRequirementReason(str, Enum):
    performance = "performance"
    cost = "cost"
    open_source = "open-source"


class LLMModel(str, Enum):
    gpt2 = "gpt2"
    gpt3 = "gpt3"
    gpt4 = "gpt4"
    gpt4o = "gpt4o"
    gpt4o_mini = "gpt4o-mini"
    claude3_5sonnet = "claude3-5sonnet"
    claude3_7 = "claude3-7"
    openai = "openai"
    anthropic = "anthropic"
    google_ai = "google-ai"
    ollama = "ollama"
    gemini = "gemini"
    gemini_flash = "gemini-flash"
    llama = "llama"
    Meta_Llama_3FULL_STOP1_8B_Instruct = "Meta-Llama-3.1-8B-Instruct"


class CloudProvider(str, Enum):
    aws = "aws"
    azure = "azure"
    gcp = "gcp"
    oracle = "oracle"
    other = "other"


class LicenseType(str, Enum):
    number_0BSD = "0BSD"
    AAL = "AAL"
    ADSL = "ADSL"
    AFL_1FULL_STOP1 = "AFL-1.1"
    AFL_1FULL_STOP2 = "AFL-1.2"
    AFL_2FULL_STOP0 = "AFL-2.0"
    AFL_2FULL_STOP1 = "AFL-2.1"
    AFL_3FULL_STOP0 = "AFL-3.0"
    AGPL_1FULL_STOP0 = "AGPL-1.0"
    AGPL_3FULL_STOP0 = "AGPL-3.0"
    AMDPLPA = "AMDPLPA"
    AML = "AML"
    AMPAS = "AMPAS"
    ANTLR_PD = "ANTLR-PD"
    APAFML = "APAFML"
    APL_1FULL_STOP0 = "APL-1.0"
    APSL_1FULL_STOP0 = "APSL-1.0"
    APSL_1FULL_STOP1 = "APSL-1.1"
    APSL_1FULL_STOP2 = "APSL-1.2"
    APSL_2FULL_STOP0 = "APSL-2.0"
    Abstyles = "Abstyles"
    Adobe_2006 = "Adobe-2006"
    Adobe_Glyph = "Adobe-Glyph"
    Afmparse = "Afmparse"
    Aladdin = "Aladdin"
    Apache_1FULL_STOP0 = "Apache-1.0"
    Apache_1FULL_STOP1 = "Apache-1.1"
    Apache_2FULL_STOP0 = "Apache-2.0"
    Artistic_1FULL_STOP0 = "Artistic-1.0"
    Artistic_1FULL_STOP0_Perl = "Artistic-1.0-Perl"
    Artistic_1FULL_STOP0_cl8 = "Artistic-1.0-cl8"
    Artistic_2FULL_STOP0 = "Artistic-2.0"
    BSD_2_Clause = "BSD-2-Clause"
    BSD_2_Clause_FreeBSD = "BSD-2-Clause-FreeBSD"
    BSD_2_Clause_NetBSD = "BSD-2-Clause-NetBSD"
    BSD_3_Clause = "BSD-3-Clause"
    BSD_3_Clause_Attribution = "BSD-3-Clause-Attribution"
    BSD_3_Clause_Clear = "BSD-3-Clause-Clear"
    BSD_3_Clause_LBNL = "BSD-3-Clause-LBNL"
    BSD_3_Clause_No_Nuclear_License = "BSD-3-Clause-No-Nuclear-License"
    BSD_3_Clause_No_Nuclear_License_2014 = "BSD-3-Clause-No-Nuclear-License-2014"
    BSD_3_Clause_No_Nuclear_Warranty = "BSD-3-Clause-No-Nuclear-Warranty"
    BSD_4_Clause = "BSD-4-Clause"
    BSD_4_Clause_UC = "BSD-4-Clause-UC"
    BSD_Protection = "BSD-Protection"
    BSD_Source_Code = "BSD-Source-Code"
    BSL_1FULL_STOP0 = "BSL-1.0"
    Bahyph = "Bahyph"
    Barr = "Barr"
    Beerware = "Beerware"
    BitTorrent_1FULL_STOP0 = "BitTorrent-1.0"
    BitTorrent_1FULL_STOP1 = "BitTorrent-1.1"
    Borceux = "Borceux"
    CATOSL_1FULL_STOP1 = "CATOSL-1.1"
    CC_BY_1FULL_STOP0 = "CC-BY-1.0"
    CC_BY_2FULL_STOP0 = "CC-BY-2.0"
    CC_BY_2FULL_STOP5 = "CC-BY-2.5"
    CC_BY_3FULL_STOP0 = "CC-BY-3.0"
    CC_BY_4FULL_STOP0 = "CC-BY-4.0"
    CC_BY_NC_1FULL_STOP0 = "CC-BY-NC-1.0"
    CC_BY_NC_2FULL_STOP0 = "CC-BY-NC-2.0"
    CC_BY_NC_2FULL_STOP5 = "CC-BY-NC-2.5"
    CC_BY_NC_3FULL_STOP0 = "CC-BY-NC-3.0"
    CC_BY_NC_4FULL_STOP0 = "CC-BY-NC-4.0"
    CC_BY_NC_ND_1FULL_STOP0 = "CC-BY-NC-ND-1.0"
    CC_BY_NC_ND_2FULL_STOP0 = "CC-BY-NC-ND-2.0"
    CC_BY_NC_ND_2FULL_STOP5 = "CC-BY-NC-ND-2.5"
    CC_BY_NC_ND_3FULL_STOP0 = "CC-BY-NC-ND-3.0"
    CC_BY_NC_ND_4FULL_STOP0 = "CC-BY-NC-ND-4.0"
    CC_BY_NC_SA_1FULL_STOP0 = "CC-BY-NC-SA-1.0"
    CC_BY_NC_SA_2FULL_STOP0 = "CC-BY-NC-SA-2.0"
    CC_BY_NC_SA_2FULL_STOP5 = "CC-BY-NC-SA-2.5"
    CC_BY_NC_SA_3FULL_STOP0 = "CC-BY-NC-SA-3.0"
    CC_BY_NC_SA_4FULL_STOP0 = "CC-BY-NC-SA-4.0"
    CC_BY_ND_1FULL_STOP0 = "CC-BY-ND-1.0"
    CC_BY_ND_2FULL_STOP0 = "CC-BY-ND-2.0"
    CC_BY_ND_2FULL_STOP5 = "CC-BY-ND-2.5"
    CC_BY_ND_3FULL_STOP0 = "CC-BY-ND-3.0"
    CC_BY_ND_4FULL_STOP0 = "CC-BY-ND-4.0"
    CC_BY_SA_1FULL_STOP0 = "CC-BY-SA-1.0"
    CC_BY_SA_2FULL_STOP0 = "CC-BY-SA-2.0"
    CC_BY_SA_2FULL_STOP5 = "CC-BY-SA-2.5"
    CC_BY_SA_3FULL_STOP0 = "CC-BY-SA-3.0"
    CC_BY_SA_4FULL_STOP0 = "CC-BY-SA-4.0"
    CC0_1FULL_STOP0 = "CC0-1.0"
    CDDL_1FULL_STOP0 = "CDDL-1.0"
    CDDL_1FULL_STOP1 = "CDDL-1.1"
    CECILL_1FULL_STOP0 = "CECILL-1.0"
    CECILL_1FULL_STOP1 = "CECILL-1.1"
    CECILL_2FULL_STOP0 = "CECILL-2.0"
    CECILL_2FULL_STOP1 = "CECILL-2.1"
    CECILL_B = "CECILL-B"
    CECILL_C = "CECILL-C"
    CNRI_Jython = "CNRI-Jython"
    CNRI_Python = "CNRI-Python"
    CNRI_Python_GPL_Compatible = "CNRI-Python-GPL-Compatible"
    CPAL_1FULL_STOP0 = "CPAL-1.0"
    CPL_1FULL_STOP0 = "CPL-1.0"
    CPOL_1FULL_STOP02 = "CPOL-1.02"
    CUA_OPL_1FULL_STOP0 = "CUA-OPL-1.0"
    Caldera = "Caldera"
    ClArtistic = "ClArtistic"
    Condor_1FULL_STOP1 = "Condor-1.1"
    Crossword = "Crossword"
    CrystalStacker = "CrystalStacker"
    Cube = "Cube"
    D_FSL_1FULL_STOP0 = "D-FSL-1.0"
    DOC = "DOC"
    DSDP = "DSDP"
    Dotseqn = "Dotseqn"
    ECL_1FULL_STOP0 = "ECL-1.0"
    ECL_2FULL_STOP0 = "ECL-2.0"
    EFL_1FULL_STOP0 = "EFL-1.0"
    EFL_2FULL_STOP0 = "EFL-2.0"
    EPL_1FULL_STOP0 = "EPL-1.0"
    EUDatagrid = "EUDatagrid"
    EUPL_1FULL_STOP0 = "EUPL-1.0"
    EUPL_1FULL_STOP1 = "EUPL-1.1"
    Entessa = "Entessa"
    ErlPL_1FULL_STOP1 = "ErlPL-1.1"
    Eurosym = "Eurosym"
    FSFAP = "FSFAP"
    FSFUL = "FSFUL"
    FSFULLR = "FSFULLR"
    FTL = "FTL"
    Fair = "Fair"
    Frameworx_1FULL_STOP0 = "Frameworx-1.0"
    FreeImage = "FreeImage"
    GFDL_1FULL_STOP1 = "GFDL-1.1"
    GFDL_1FULL_STOP2 = "GFDL-1.2"
    GFDL_1FULL_STOP3 = "GFDL-1.3"
    GL2PS = "GL2PS"
    GPL_1FULL_STOP0 = "GPL-1.0"
    GPL_2FULL_STOP0 = "GPL-2.0"
    GPL_3FULL_STOP0 = "GPL-3.0"
    Giftware = "Giftware"
    Glide = "Glide"
    Glulxe = "Glulxe"
    HPND = "HPND"
    HaskellReport = "HaskellReport"
    IBM_pibs = "IBM-pibs"
    ICU = "ICU"
    IJG = "IJG"
    IPA = "IPA"
    IPL_1FULL_STOP0 = "IPL-1.0"
    ISC = "ISC"
    ImageMagick = "ImageMagick"
    Imlib2 = "Imlib2"
    Info_ZIP = "Info-ZIP"
    Intel = "Intel"
    Intel_ACPI = "Intel-ACPI"
    Interbase_1FULL_STOP0 = "Interbase-1.0"
    JSON = "JSON"
    JasPer_2FULL_STOP0 = "JasPer-2.0"
    LAL_1FULL_STOP2 = "LAL-1.2"
    LAL_1FULL_STOP3 = "LAL-1.3"
    LGPL_2FULL_STOP0 = "LGPL-2.0"
    LGPL_2FULL_STOP1 = "LGPL-2.1"
    LGPL_3FULL_STOP0 = "LGPL-3.0"
    LGPLLR = "LGPLLR"
    LPL_1FULL_STOP0 = "LPL-1.0"
    LPL_1FULL_STOP02 = "LPL-1.02"
    LPPL_1FULL_STOP0 = "LPPL-1.0"
    LPPL_1FULL_STOP1 = "LPPL-1.1"
    LPPL_1FULL_STOP2 = "LPPL-1.2"
    LPPL_1FULL_STOP3a = "LPPL-1.3a"
    LPPL_1FULL_STOP3c = "LPPL-1.3c"
    Latex2e = "Latex2e"
    Leptonica = "Leptonica"
    LiLiQ_P_1FULL_STOP1 = "LiLiQ-P-1.1"
    LiLiQ_R_1FULL_STOP1 = "LiLiQ-R-1.1"
    LiLiQ_Rplus_1FULL_STOP1 = "LiLiQ-Rplus-1.1"
    Libpng = "Libpng"
    MIT = "MIT"
    MIT_CMU = "MIT-CMU"
    MIT_advertising = "MIT-advertising"
    MIT_enna = "MIT-enna"
    MIT_feh = "MIT-feh"
    MITNFA = "MITNFA"
    MPL_1FULL_STOP0 = "MPL-1.0"
    MPL_1FULL_STOP1 = "MPL-1.1"
    MPL_2FULL_STOP0 = "MPL-2.0"
    MPL_2FULL_STOP0_no_copyleft_exception = "MPL-2.0-no-copyleft-exception"
    MS_PL = "MS-PL"
    MS_RL = "MS-RL"
    MTLL = "MTLL"
    MakeIndex = "MakeIndex"
    MirOS = "MirOS"
    Motosoto = "Motosoto"
    Multics = "Multics"
    Mup = "Mup"
    NASA_1FULL_STOP3 = "NASA-1.3"
    NBPL_1FULL_STOP0 = "NBPL-1.0"
    NCSA = "NCSA"
    NGPL = "NGPL"
    NLOD_1FULL_STOP0 = "NLOD-1.0"
    NLPL = "NLPL"
    NOSL = "NOSL"
    NPL_1FULL_STOP0 = "NPL-1.0"
    NPL_1FULL_STOP1 = "NPL-1.1"
    NPOSL_3FULL_STOP0 = "NPOSL-3.0"
    NRL = "NRL"
    NTP = "NTP"
    Naumen = "Naumen"
    NetCDF = "NetCDF"
    Newsletr = "Newsletr"
    Nokia = "Nokia"
    Noweb = "Noweb"
    Nunit = "Nunit"
    OCCT_PL = "OCCT-PL"
    OCLC_2FULL_STOP0 = "OCLC-2.0"
    ODbL_1FULL_STOP0 = "ODbL-1.0"
    OFL_1FULL_STOP0 = "OFL-1.0"
    OFL_1FULL_STOP1 = "OFL-1.1"
    OGTSL = "OGTSL"
    OLDAP_1FULL_STOP1 = "OLDAP-1.1"
    OLDAP_1FULL_STOP2 = "OLDAP-1.2"
    OLDAP_1FULL_STOP3 = "OLDAP-1.3"
    OLDAP_1FULL_STOP4 = "OLDAP-1.4"
    OLDAP_2FULL_STOP0 = "OLDAP-2.0"
    OLDAP_2FULL_STOP0FULL_STOP1 = "OLDAP-2.0.1"
    OLDAP_2FULL_STOP1 = "OLDAP-2.1"
    OLDAP_2FULL_STOP2 = "OLDAP-2.2"
    OLDAP_2FULL_STOP2FULL_STOP1 = "OLDAP-2.2.1"
    OLDAP_2FULL_STOP2FULL_STOP2 = "OLDAP-2.2.2"
    OLDAP_2FULL_STOP3 = "OLDAP-2.3"
    OLDAP_2FULL_STOP4 = "OLDAP-2.4"
    OLDAP_2FULL_STOP5 = "OLDAP-2.5"
    OLDAP_2FULL_STOP6 = "OLDAP-2.6"
    OLDAP_2FULL_STOP7 = "OLDAP-2.7"
    OLDAP_2FULL_STOP8 = "OLDAP-2.8"
    OML = "OML"
    OPL_1FULL_STOP0 = "OPL-1.0"
    OSET_PL_2FULL_STOP1 = "OSET-PL-2.1"
    OSL_1FULL_STOP0 = "OSL-1.0"
    OSL_1FULL_STOP1 = "OSL-1.1"
    OSL_2FULL_STOP0 = "OSL-2.0"
    OSL_2FULL_STOP1 = "OSL-2.1"
    OSL_3FULL_STOP0 = "OSL-3.0"
    OpenSSL = "OpenSSL"
    PDDL_1FULL_STOP0 = "PDDL-1.0"
    PHP_3FULL_STOP0 = "PHP-3.0"
    PHP_3FULL_STOP01 = "PHP-3.01"
    Plexus = "Plexus"
    PostgreSQL = "PostgreSQL"
    Python_2FULL_STOP0 = "Python-2.0"
    QPL_1FULL_STOP0 = "QPL-1.0"
    Qhull = "Qhull"
    RHeCos_1FULL_STOP1 = "RHeCos-1.1"
    RPL_1FULL_STOP1 = "RPL-1.1"
    RPL_1FULL_STOP5 = "RPL-1.5"
    RPSL_1FULL_STOP0 = "RPSL-1.0"
    RSA_MD = "RSA-MD"
    RSCPL = "RSCPL"
    Rdisc = "Rdisc"
    Ruby = "Ruby"
    SAX_PD = "SAX-PD"
    SCEA = "SCEA"
    SGI_B_1FULL_STOP0 = "SGI-B-1.0"
    SGI_B_1FULL_STOP1 = "SGI-B-1.1"
    SGI_B_2FULL_STOP0 = "SGI-B-2.0"
    SISSL = "SISSL"
    SISSL_1FULL_STOP2 = "SISSL-1.2"
    SMLNJ = "SMLNJ"
    SMPPL = "SMPPL"
    SNIA = "SNIA"
    SPL_1FULL_STOP0 = "SPL-1.0"
    SWL = "SWL"
    Saxpath = "Saxpath"
    Sendmail = "Sendmail"
    SimPL_2FULL_STOP0 = "SimPL-2.0"
    Sleepycat = "Sleepycat"
    Spencer_86 = "Spencer-86"
    Spencer_94 = "Spencer-94"
    Spencer_99 = "Spencer-99"
    SugarCRM_1FULL_STOP1FULL_STOP3 = "SugarCRM-1.1.3"
    TCL = "TCL"
    TMate = "TMate"
    TORQUE_1FULL_STOP1 = "TORQUE-1.1"
    TOSL = "TOSL"
    UPL_1FULL_STOP0 = "UPL-1.0"
    Unicode_TOU = "Unicode-TOU"
    Unlicense = "Unlicense"
    VOSTROM = "VOSTROM"
    VSL_1FULL_STOP0 = "VSL-1.0"
    Vim = "Vim"
    W3C = "W3C"
    W3C_19980720 = "W3C-19980720"
    WTFPL = "WTFPL"
    Watcom_1FULL_STOP0 = "Watcom-1.0"
    Wsuipa = "Wsuipa"
    X11 = "X11"
    XFree86_1FULL_STOP1 = "XFree86-1.1"
    XSkat = "XSkat"
    Xerox = "Xerox"
    Xnet = "Xnet"
    YPL_1FULL_STOP0 = "YPL-1.0"
    YPL_1FULL_STOP1 = "YPL-1.1"
    ZPL_1FULL_STOP1 = "ZPL-1.1"
    ZPL_2FULL_STOP0 = "ZPL-2.0"
    ZPL_2FULL_STOP1 = "ZPL-2.1"
    Zed = "Zed"
    Zend_2FULL_STOP0 = "Zend-2.0"
    Zimbra_1FULL_STOP3 = "Zimbra-1.3"
    Zimbra_1FULL_STOP4 = "Zimbra-1.4"
    Zlib = "Zlib"
    bzip2_1FULL_STOP0FULL_STOP5 = "bzip2-1.0.5"
    bzip2_1FULL_STOP0FULL_STOP6 = "bzip2-1.0.6"
    curl = "curl"
    diffmark = "diffmark"
    dvipdfm = "dvipdfm"
    eGenix = "eGenix"
    gSOAP_1FULL_STOP3b = "gSOAP-1.3b"
    gnuplot = "gnuplot"
    iMatix = "iMatix"
    libtiff = "libtiff"
    mpich2 = "mpich2"
    psfrag = "psfrag"
    psutils = "psutils"
    xinetd = "xinetd"
    xpp = "xpp"
    zlib_acknowledgement = "zlib-acknowledgement"
    Proprietary = "Proprietary"
    Other = "Other"
    Not_licensed = "Not licensed"
    Freeware = "Freeware"


class ContributorRole(str, Enum):
    Developer = "Developer"
    Maintainer = "Maintainer"
    Provider = "Provider"
    Documentor = "Documentor"
    Contributor = "Contributor"
    Support = "Support"
    PrimaryContact = "PrimaryContact"


class UserType(str, Enum):
    patient = "patient"
    clinician = "clinician"
    researcher = "researcher"
    site_admin_prepping_ehr_extracts = "site-admin-prepping-ehr-extracts"


class LiteracyLevel(str, Enum):
    novice = "novice"
    intermediate = "intermediate"
    advanced = "advanced"
    expert = "expert"


class ToolType(str, Enum):
    CLI = "CLI"
    DatabasePortal = "DatabasePortal"
    DesktopApp = "DesktopApp"
    Library = "Library"
    Ontology = "Ontology"
    Plugin = "Plugin"
    Script = "Script"
    SPARQLEndpoint = "SPARQLEndpoint"
    Suite = "Suite"
    WebApp = "WebApp"
    WebAPI = "WebAPI"
    WebServiceSOAP = "WebServiceSOAP"
    Workbench = "Workbench"
    Workflow = "Workflow"
    Notebook = "Notebook"
    AISOLIDUSMLModel = "AI/MLModel"
    KnowledgeGraph = "KnowledgeGraph"



class SystemMetadata(ConfiguredBaseModel):
    """
    Top level class representing system metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema', 'tree_root': True})

    version: string = Field(..., description="""Version of the system""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['SystemMetadata']} })
    tool: ToolInfo = Field(..., description="""Metadata details about the tool""", json_schema_extra = { "linkml_meta": {'alias': 'tool', 'domain_of': ['SystemMetadata']} })
    domains: List[str] = Field(..., description="""Domains in which the application is leveraged""", json_schema_extra = { "linkml_meta": {'alias': 'domains', 'domain_of': ['SystemMetadata']} })
    llm: LlmInfo = Field(..., description="""Information about LLM usage in the system""", json_schema_extra = { "linkml_meta": {'alias': 'llm', 'domain_of': ['SystemMetadata']} })
    cloud: Optional[CloudInfo] = Field(None, description="""Information about cloud platform usage""", json_schema_extra = { "linkml_meta": {'alias': 'cloud', 'domain_of': ['SystemMetadata']} })
    input: List[DataSource] = Field(..., description="""List of input data sources""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'input', 'domain_of': ['SystemMetadata']} })
    output: List[DataSource] = Field(..., description="""List of output data formats""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'output', 'domain_of': ['SystemMetadata']} })
    collaborations: List[Collaboration] = Field(..., description="""List of tool collaborations""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'collaborations', 'domain_of': ['SystemMetadata']} })
    funding: Optional[FundingInfo] = Field(None, description="""Information about funding sources""", json_schema_extra = { "linkml_meta": {'alias': 'funding', 'domain_of': ['SystemMetadata']} })
    maturity: MaturityLevel = Field(..., description="""Tool maturity level""", json_schema_extra = { "linkml_meta": {'alias': 'maturity', 'domain_of': ['SystemMetadata']} })
    license: License = Field(..., description="""Licensing of tool""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['SystemMetadata']} })
    publication: Optional[List[PublicationDetail]] = Field(None, description="""Publications about the software""", json_schema_extra = { "linkml_meta": {'alias': 'publication', 'domain_of': ['SystemMetadata']} })
    credit: List[Credit] = Field(..., description="""Credit for tool""", json_schema_extra = { "linkml_meta": {'alias': 'credit', 'domain_of': ['SystemMetadata']} })
    target_users: TargetUsers = Field(..., description="""Target primary and secondary users of tool""", json_schema_extra = { "linkml_meta": {'alias': 'target_users', 'domain_of': ['SystemMetadata']} })
    media: Optional[List[Media]] = Field(None, description="""Multi-media link pertaining to a tool (images, video, etc)""", json_schema_extra = { "linkml_meta": {'alias': 'media', 'domain_of': ['SystemMetadata']} })


class LlmInfo(ConfiguredBaseModel):
    """
    Information about LLM usage in the system
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    usesLlm: bool = Field(..., description="""Whether the system uses LLMs""", json_schema_extra = { "linkml_meta": {'alias': 'usesLlm', 'domain_of': ['LlmInfo']} })
    modelsSupported: Optional[List[LLMModel]] = Field(None, description="""List of LLM models supported by the system""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'modelsSupported', 'domain_of': ['LlmInfo']} })
    modelsRequired: Optional[List[LLMModel]] = Field(None, description="""List of LLM models required by the system""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'modelsRequired', 'domain_of': ['LlmInfo']} })
    reasonsForRequirement: Optional[List[LLMRequirementReason]] = Field(None, description="""Reasons why specific models are required""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'reasonsForRequirement', 'domain_of': ['LlmInfo']} })
    bringOwnKey: bool = Field(..., description="""Do users need to bring their own API key?""", json_schema_extra = { "linkml_meta": {'alias': 'bringOwnKey', 'domain_of': ['LlmInfo']} })


class CloudInfo(ConfiguredBaseModel):
    """
    Information about cloud platform usage
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    platform: CloudProvider = Field(..., description="""Cloud platform used by the system""", json_schema_extra = { "linkml_meta": {'alias': 'platform', 'domain_of': ['CloudInfo']} })
    lastAuditDate: datetime  = Field(..., description="""Date of the last security audit""", json_schema_extra = { "linkml_meta": {'alias': 'lastAuditDate', 'domain_of': ['CloudInfo']} })


class DataSource(ConfiguredBaseModel):
    """
    Information about data inputs or outputs
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    name: str = Field(..., description="""Name of the data source""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['DataSource', 'Collaboration', 'ToolInfo', 'Credit']} })
    dataCategory: str = Field(..., description="""Data category""", json_schema_extra = { "linkml_meta": {'alias': 'dataCategory', 'domain_of': ['DataSource']} })
    dataClass: DataClass = Field(..., description="""Data class""", json_schema_extra = { "linkml_meta": {'alias': 'dataClass', 'domain_of': ['DataSource']} })
    dataType: str = Field(..., description="""Data Type""", json_schema_extra = { "linkml_meta": {'alias': 'dataType', 'domain_of': ['DataSource']} })
    dataSubType: Optional[str] = Field(None, description="""Data Subtype""", json_schema_extra = { "linkml_meta": {'alias': 'dataSubType', 'domain_of': ['DataSource']} })
    dataStandard: List[str] = Field(..., description="""Data Standard""", json_schema_extra = { "linkml_meta": {'alias': 'dataStandard', 'domain_of': ['DataSource']} })
    format: List[FileFormat] = Field(..., description="""Format of the data""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['DataSource']} })
    proprietary: bool = Field(..., description="""Whether the data format is proprietary""", json_schema_extra = { "linkml_meta": {'alias': 'proprietary', 'domain_of': ['DataSource']} })
    source: Optional[str] = Field(None, description="""URL or identifier for the data source""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['DataSource', 'FundingInfo']} })


class Collaboration(ConfiguredBaseModel):
    """
    Information about tool collaborations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    name: str = Field(..., description="""Name of the collaboration""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['DataSource', 'Collaboration', 'ToolInfo', 'Credit']} })
    description: str = Field(..., description="""Description of the collaboration""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['Collaboration']} })
    tools: List[str] = Field(..., description="""List of tools used in the collaboration""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'tools', 'domain_of': ['Collaboration']} })
    collaboration_purpose: str = Field(..., description="""Purpose of the collaboration""", json_schema_extra = { "linkml_meta": {'alias': 'collaboration_purpose', 'domain_of': ['Collaboration']} })


class FundingInfo(ConfiguredBaseModel):
    """
    Information about funding sources
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    source: Optional[str] = Field(None, description="""Name of the funding source""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['DataSource', 'FundingInfo']} })
    agreement: Optional[str] = Field(None, description="""Agreement identifier""", json_schema_extra = { "linkml_meta": {'alias': 'agreement', 'domain_of': ['FundingInfo']} })
    link: Optional[str] = Field(None, description="""Link to funding information""", json_schema_extra = { "linkml_meta": {'alias': 'link', 'domain_of': ['FundingInfo', 'License', 'Media']} })


class ToolInfo(ConfiguredBaseModel):
    """
    Metadata details about the tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    name: str = Field(..., description="""Name of tool""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['DataSource', 'Collaboration', 'ToolInfo', 'Credit']} })
    repo_url: str = Field(..., description="""Public repository URL""", json_schema_extra = { "linkml_meta": {'alias': 'repo_url', 'domain_of': ['ToolInfo']} })
    tool_homepage: str = Field(..., description="""Public homepage URL""", json_schema_extra = { "linkml_meta": {'alias': 'tool_homepage', 'domain_of': ['ToolInfo']} })
    documentation_url: str = Field(..., description="""Public documentation URL""", json_schema_extra = { "linkml_meta": {'alias': 'documentation_url', 'domain_of': ['ToolInfo']} })
    tool_type: ToolType = Field(..., description="""Type of tool""", json_schema_extra = { "linkml_meta": {'alias': 'tool_type', 'domain_of': ['ToolInfo']} })
    tool_notes: Optional[str] = Field(None, description="""Top level notes""", json_schema_extra = { "linkml_meta": {'alias': 'tool_notes', 'domain_of': ['ToolInfo']} })


class PublicationDetail(ConfiguredBaseModel):
    """
    Details regarding publication surrounding tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    type: Optional[str] = Field(None, description="""Type of publication""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['PublicationDetail']} })
    tool_version: Optional[string] = Field(None, description="""Version of tool the publication references""", json_schema_extra = { "linkml_meta": {'alias': 'tool_version', 'domain_of': ['PublicationDetail']} })
    doi: Optional[string] = Field(None, description="""DOI of publication""", json_schema_extra = { "linkml_meta": {'alias': 'doi', 'domain_of': ['PublicationDetail']} })
    pmid: Optional[str] = Field(None, description="""PubMed Identifier of publication""", json_schema_extra = { "linkml_meta": {'alias': 'pmid', 'domain_of': ['PublicationDetail']} })
    pmcid: Optional[str] = Field(None, description="""PubMed Central Identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pmcid', 'domain_of': ['PublicationDetail']} })
    url: Optional[str] = Field(None, description="""URL to publication if no DOI available""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['PublicationDetail', 'Credit']} })


class License(ConfiguredBaseModel):
    """
    Licensing details of tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    license_type: LicenseType = Field(..., description="""Core license type""", json_schema_extra = { "linkml_meta": {'alias': 'license_type', 'domain_of': ['License']} })
    link: Optional[str] = Field(None, description="""Link to license""", json_schema_extra = { "linkml_meta": {'alias': 'link', 'domain_of': ['FundingInfo', 'License', 'Media']} })
    notes: Optional[str] = Field(None, description="""Notes about license""", json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['License']} })


class Credit(ConfiguredBaseModel):
    """
    Credit details for tool creators
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    name: Optional[str] = Field(None, description="""Name of creditee""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['DataSource', 'Collaboration', 'ToolInfo', 'Credit']} })
    email: Optional[List[str]] = Field(None, description="""Email of creditee""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['Credit']} })
    url: Optional[str] = Field(None, description="""URL or link of creditee""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['PublicationDetail', 'Credit']} })
    orcidid: Optional[str] = Field(None, description="""ORCID ID of creditee""", json_schema_extra = { "linkml_meta": {'alias': 'orcidid', 'domain_of': ['Credit'], 'slot_uri': 'schema:identifier'} })
    role: Optional[ContributorRole] = Field(None, description="""Role of creditee""", json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['Credit']} })
    org: Optional[str] = Field(None, description="""Organization associated with creditee""", json_schema_extra = { "linkml_meta": {'alias': 'org', 'domain_of': ['Credit']} })
    note: Optional[str] = Field(None, description="""Notes about creditee""", json_schema_extra = { "linkml_meta": {'alias': 'note', 'domain_of': ['Credit']} })

    @field_validator('orcidid')
    def pattern_orcidid(cls, v):
        pattern=re.compile(r"^ORCID:[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid orcidid format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid orcidid format: {v}")
        return v


class MaturityLevel(ConfiguredBaseModel):
    """
    Maturity level of application during development according to NASA TRL
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    beginning_maturity: int = Field(..., description="""Maturity at the beginning of the BDF program""", ge=1, le=9, json_schema_extra = { "linkml_meta": {'alias': 'beginning_maturity', 'domain_of': ['MaturityLevel']} })
    current_maturity: int = Field(..., description="""Current level of maturity""", ge=1, le=9, json_schema_extra = { "linkml_meta": {'alias': 'current_maturity', 'domain_of': ['MaturityLevel']} })
    final_maturity: Optional[int] = Field(None, description="""Final maturity of the tool""", ge=1, le=9, json_schema_extra = { "linkml_meta": {'alias': 'final_maturity', 'domain_of': ['MaturityLevel']} })


class PrimaryUser(ConfiguredBaseModel):
    """
    Primary user of tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    user_type: UserType = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'user_type', 'domain_of': ['PrimaryUser', 'SecondaryUser']} })
    technical_literacy_level: List[LiteracyLevel] = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'technical_literacy_level',
         'domain_of': ['PrimaryUser', 'SecondaryUser']} })
    biomedical_literacy_level: List[LiteracyLevel] = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'biomedical_literacy_level',
         'domain_of': ['PrimaryUser', 'SecondaryUser']} })


class SecondaryUser(ConfiguredBaseModel):
    """
    Secondary user of tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    user_type: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'user_type', 'domain_of': ['PrimaryUser', 'SecondaryUser']} })
    technical_literacy_level: List[LiteracyLevel] = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'technical_literacy_level',
         'domain_of': ['PrimaryUser', 'SecondaryUser']} })
    biomedical_literacy_level: List[LiteracyLevel] = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'biomedical_literacy_level',
         'domain_of': ['PrimaryUser', 'SecondaryUser']} })


class TargetUsers(ConfiguredBaseModel):
    """
    Target users of application
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    primary_user: PrimaryUser = Field(..., description="""Primary user details""", json_schema_extra = { "linkml_meta": {'alias': 'primary_user', 'domain_of': ['TargetUsers']} })
    secondary_user: Optional[SecondaryUser] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'secondary_user', 'domain_of': ['TargetUsers']} })


class Media(ConfiguredBaseModel):
    """
    Media resources associated with your tool
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://example.org/system-metadata-schema'})

    link: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'link', 'domain_of': ['FundingInfo', 'License', 'Media']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SystemMetadata.model_rebuild()
LlmInfo.model_rebuild()
CloudInfo.model_rebuild()
DataSource.model_rebuild()
Collaboration.model_rebuild()
FundingInfo.model_rebuild()
ToolInfo.model_rebuild()
PublicationDetail.model_rebuild()
License.model_rebuild()
Credit.model_rebuild()
MaturityLevel.model_rebuild()
PrimaryUser.model_rebuild()
SecondaryUser.model_rebuild()
TargetUsers.model_rebuild()
Media.model_rebuild()

