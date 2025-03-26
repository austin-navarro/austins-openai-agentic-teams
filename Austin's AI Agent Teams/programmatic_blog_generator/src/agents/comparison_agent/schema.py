"""
Schema definitions for the comparison blog post using Pydantic models.
"""
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from datetime import date

class Author(BaseModel):
    name: Literal["Moso Panda"] = "Moso Panda"
    role: Literal["Web3 Specialist"] = "Web3 Specialist"

class Media(BaseModel):
    term_a: str
    term_b: str

class Background(BaseModel):
    heading: str
    content: str

class KeyDifferenceItem(BaseModel):
    feature_title: str
    a_description: str
    b_description: str

class KeyDifferences(BaseModel):
    heading: str
    items: List[KeyDifferenceItem]

class ComparisonFeature(BaseModel):
    label: str
    a_value: str
    b_value: str

class IdealFor(BaseModel):
    a: str
    b: str

class ComparisonTable(BaseModel):
    heading: str
    features: List[ComparisonFeature]
    ideal_for: IdealFor

class Conclusion(BaseModel):
    heading: str
    summary_paragraphs: List[str]

class ComparisonBlogPost(BaseModel):
    title: str
    slug: str
    published_date: str
    read_time: str
    author: Author
    media: Optional[Media] = None
    introduction: str
    jump_link_text: Optional[str] = None
    background: Background
    key_differences: KeyDifferences
    comparison_table: ComparisonTable
    conclusion: Conclusion 