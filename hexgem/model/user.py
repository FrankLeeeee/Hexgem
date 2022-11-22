from datetime import date
from typing import List, Optional

from pydantic import BaseModel

__all__ = ['User']


class User(BaseModel):
    id: int
    email: str
    username: str
    github_page: str
    organization: List[str] = []
    is_contributor: bool = False
    star_date: Optional[date] = None
