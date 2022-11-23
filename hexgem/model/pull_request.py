'''
File: pull_request.py
Project: Hexgem
File Created: Wednesday, 23rd November 2022 4:25:00 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Wednesday, 23rd November 2022 4:34:36 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

from datetime import date
from typing import Union

from pydantic import BaseModel

from .user import User

__all__ = ['PullRequest']


class PullRequest(BaseModel):
    """
    This is a model class for a GitHub pull request.

    Args:
        number (int): the number assigned to this PR
        url (str): the link to the PR
        title (title): the title of the PR
        author (User): the user who created this PR
        state (str): the current state of the PR
        creation_date (date): when this PR was created
        close_date (Union[date, None]): when this PR was closed, it should be None when the PR is still open
        comment_count (int): the number of comments in the discussion section
    """
    number: int
    url: str
    title: str
    author: User
    state: str
    creation_date: date
    close_date: Union[date, None]
    comment_count: int
