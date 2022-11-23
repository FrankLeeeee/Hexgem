'''
File: repository.py
Project: Hexgem
File Created: Wednesday, 23rd November 2022 4:21:22 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Wednesday, 23rd November 2022 4:33:05 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

from datetime import date
from typing import List, Optional

from pydantic import BaseModel

from .commit import Commit
from .issue import Issue
from .pull_request import PullRequest

__all__ = ['Repository']


class Repository(BaseModel):
    """
    This is a model class for a GitHub repository.

    Args:
        name (str): the name of the repository
        url (str): the link to the repository page
        owner (str): the owner of this repository
        creation_date (date): when the repository was created
        is_private (bool): whether the repository is private
        star_count (int): the number of stars given to this repository
        commits (Optional[List[Commit]]): optional, the list of commits for this repository
        pull_requests (Optional[List[PullRequest]]): optional, the list of pull requests for this repository
        issues (Optional[List[Issue]]): optional, the list of issues for this repository
    """
    name: str
    url: str
    owner: str
    creation_date: date
    is_private: bool = False
    star_count: int = -1
    commits: Optional[List[Commit]] = None
    pull_requests: Optional[List[PullRequest]] = None
    issues: Optional[List[Issue]] = None
