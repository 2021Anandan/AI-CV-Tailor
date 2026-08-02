"""
Custom exceptions for resume parsing.
"""


class ResumeParserError(Exception):
    """Base exception for parser errors."""
    pass


class UnsupportedFileTypeError(ResumeParserError):
    """Raised when an unsupported file type is uploaded."""
    pass


class EmptyResumeError(ResumeParserError):
    """Raised when no readable text is found in the resume."""
    pass