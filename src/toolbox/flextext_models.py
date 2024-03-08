from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class AnalysisStatusTypes(Enum):
    HUMAN_APPROVED = "humanApproved"
    GUESS = "guess"
    GUESS_BY_HUMAN_APPROVED = "guessByHumanApproved"
    GUESS_BY_STATISTICAL_ANALYSIS = "guessByStatisticalAnalysis"


class KnownItemTypes(Enum):
    TXT = "txt"
    CF = "cf"
    HN = "hn"
    VARIANT_TYPES = "variantTypes"
    GLS = "gls"
    MSA = "msa"
    POS = "pos"
    TITLE = "title"
    TITLE_ABBREVIATION = "title-abbreviation"
    SOURCE = "source"
    COMMENT = "comment"
    TEXT_IS_TRANSLATION = "text-is-translation"
    DESCRIPTION = "description"
    PUNCT = "punct"


class MorphTypes(Enum):
    PARTICLE = "particle"
    INFIX = "infix"
    PREFIX = "prefix"
    SIMULFIX = "simulfix"
    SUFFIX = "suffix"
    SUPRAFIX = "suprafix"
    CIRCUMFIX = "circumfix"
    CLITIC = "clitic"
    ENCLITIC = "enclitic"
    PROCLITIC = "proclitic"
    BOUND_ROOT = "bound root"
    ROOT = "root"
    BOUND_STEM = "bound stem"
    STEM = "stem"
    INFIXING_INTERFIX = "infixing interfix"
    PREFIXING_INTERFIX = "prefixing interfix"
    SUFFIXING_INTERFIX = "suffixing interfix"
    PHRASE = "phrase"
    DISCONTIGUOUS_PHRASE = "discontiguous phrase"


class ScrSectionTypes(Enum):
    TITLE = "title"
    HEADING = "heading"
    VERSE_TEXT = "verseText"


@dataclass
class Item:
    class Meta:
        name = "item"
        nillable = True

    value: Optional[str] = field(
        default="",
        metadata={
            "nillable": True,
        },
    )
    type_value: Optional[Union[KnownItemTypes, str]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    analysis_status: Optional[AnalysisStatusTypes] = field(
        default=None,
        metadata={
            "name": "analysisStatus",
            "type": "Attribute",
        },
    )


@dataclass
class Document:
    class Meta:
        name = "document"

    interlinear_text: List["Document.InterlinearText"] = field(
        default_factory=list,
        metadata={
            "name": "interlinear-text",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    export_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "exportSource",
            "type": "Attribute",
        },
    )
    export_target: Optional[str] = field(
        default=None,
        metadata={
            "name": "exportTarget",
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class InterlinearText:
        item: List[Item] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "nillable": True,
                "sequence": 1,
            },
        )
        paragraphs: List["Document.InterlinearText.Paragraphs"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "sequence": 1,
            },
        )
        languages: List["Document.InterlinearText.Languages"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "sequence": 1,
            },
        )
        media_files: List["Document.InterlinearText.MediaFiles"] = field(
            default_factory=list,
            metadata={
                "name": "media-files",
                "type": "Element",
                "namespace": "",
                "sequence": 1,
            },
        )
        guid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        scr_section_type: Optional[ScrSectionTypes] = field(
            default=None,
            metadata={
                "name": "scrSectionType",
                "type": "Attribute",
            },
        )
        scr_book: Optional[str] = field(
            default=None,
            metadata={
                "name": "scrBook",
                "type": "Attribute",
            },
        )

        @dataclass
        class Paragraphs:
            paragraph: List["Document.InterlinearText.Paragraphs.Paragraph"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Paragraph:
                phrases: Optional[
                    "Document.InterlinearText.Paragraphs.Paragraph.Phrases"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    },
                )
                guid: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass
                class Phrases:
                    phrase: List[
                        "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "",
                        },
                    )

                    @dataclass
                    class Phrase:
                        item: List[Item] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        words: Optional[
                            "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "",
                                "required": True,
                            },
                        )
                        media_file: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "media-file",
                                "type": "Attribute",
                            },
                        )
                        begin_time_offset: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "begin-time-offset",
                                "type": "Attribute",
                            },
                        )
                        end_time_offset: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "end-time-offset",
                                "type": "Attribute",
                            },
                        )
                        guid: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        speaker: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )

                        @dataclass
                        class Words:
                            scr_milestone: List[
                                "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words.ScrMilestone"
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "name": "scrMilestone",
                                    "type": "Element",
                                    "namespace": "",
                                },
                            )
                            word: List[
                                "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words.Word"
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "namespace": "",
                                },
                            )

                            @dataclass
                            class ScrMilestone:
                                chapter: Optional[int] = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                        "required": True,
                                    },
                                )
                                verse: Optional[int] = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                        "required": True,
                                    },
                                )

                            @dataclass
                            class Word:
                                item: List[Item] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "nillable": True,
                                    },
                                )
                                morphemes: List[
                                    "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words.Word.Morphemes"
                                ] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "namespace": "",
                                    },
                                )
                                guid: Optional[str] = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                    },
                                )
                                type_value: str = field(
                                    init=False,
                                    default="phrase",
                                    metadata={
                                        "name": "type",
                                        "type": "Attribute",
                                    },
                                )

                                @dataclass
                                class Morphemes:
                                    morph: List[
                                        "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words.Word.Morphemes.Morph"
                                    ] = field(
                                        default_factory=list,
                                        metadata={
                                            "type": "Element",
                                            "namespace": "",
                                        },
                                    )
                                    analysis_status: Optional[AnalysisStatusTypes] = (
                                        field(
                                            default=None,
                                            metadata={
                                                "name": "analysisStatus",
                                                "type": "Attribute",
                                            },
                                        )
                                    )

                                    @dataclass
                                    class Morph:
                                        item: List[Item] = field(
                                            default_factory=list,
                                            metadata={
                                                "type": "Element",
                                                "nillable": True,
                                            },
                                        )
                                        type_value: Optional[MorphTypes] = field(
                                            default=None,
                                            metadata={
                                                "name": "type",
                                                "type": "Attribute",
                                            },
                                        )
                                        guid: Optional[str] = field(
                                            default=None,
                                            metadata={
                                                "type": "Attribute",
                                            },
                                        )

        @dataclass
        class Languages:
            language: List["Document.InterlinearText.Languages.Language"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Language:
                lang: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )
                encoding: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                font: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                vernacular: Optional[bool] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

        @dataclass
        class MediaFiles:
            media: List["Document.InterlinearText.MediaFiles.Media"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            offset_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "offset-type",
                    "type": "Attribute",
                },
            )

            @dataclass
            class Media:
                guid: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )
                location: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )
