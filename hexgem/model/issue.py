'''
File: issue.py
Project: Hexgem
File Created: Wednesday, 23rd November 2022 4:24:55 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Wednesday, 23rd November 2022 4:33:43 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

from datetime import date
from typing import Union

from pydantic import BaseModel

from .user import User


class Issue(BaseModel):
    """
    This is a model class for a GitHub issue.

    Args:
        number (int): the issue number assigned to this issue
        url (str): the link to the issue
        title (title): the title of the issue
        author (User): the user who created this issue
        state (str): the current state of the issue
        creation_date (date): when this issue was created
        close_date (Union[date, None]): when this issue was closed, it should be None when the issue is still open
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
