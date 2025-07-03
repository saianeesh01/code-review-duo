from pydantic import BaseModel, Field
from typing import Literal, List

class ReviewComment(BaseModel):
    file: str
    line: int
    severity: Literal["INFO", "SUGGESTION", "WARNING", "ERROR"]
    message: str = Field(..., max_length=400)

class DiffPatch(BaseModel):
    diff: str                       # unified-diff
    applies_cleanly: bool
    # optional: list[ReviewComment] inline references

class ReviewBundle(BaseModel):
    comments: List[ReviewComment]
    patch: DiffPatch
