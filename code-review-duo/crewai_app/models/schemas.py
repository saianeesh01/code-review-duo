# Pydantic schemas for strict JSON
from pydantic import BaseModel
from typing import List

class ReviewComment(BaseModel):
    file: str
    line: int
    comment: str

class DiffPatch(BaseModel):
    file: str
    diff: str
