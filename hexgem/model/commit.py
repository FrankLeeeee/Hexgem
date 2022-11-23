'''
File: commit.py
Project: Hexgem
File Created: Wednesday, 23rd November 2022 4:24:49 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Wednesday, 23rd November 2022 4:38:21 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

from datetime import date

from pydantic import BaseModel

from .user import User

__all__ = ['Commit']


class Commit(BaseModel):
    """
    This is a data class for a GitHub commit.

    Args:
        author (User): the author of the commit
        message (str): the commit message
        creation_date (date): the date when this commit was created
    """
    author: User
    message: str
    creation_date: date
