"""
Comparison Page Generator

A tool for automatically generating structured comparison content for marketing purposes.
This package uses the OpenAI Agents framework to create detailed comparison pages
between any two topics that can be easily imported into a CMS.
"""

from .comparison_generator import (
    ComparisonSection,
    ComparisonPage,
    generate_comparison,
    output_comparison_json,
    create_comparison_content
)

__all__ = [
    "ComparisonSection",
    "ComparisonPage",
    "generate_comparison",
    "output_comparison_json",
    "create_comparison_content"
] 