'''
File: user.py
Project: Hexgem
File Created: Tuesday, 22nd November 2022 5:35:44 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Wednesday, 23rd November 2022 4:33:37 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

from datetime import date
from typing import List, Optional

from pydantic import BaseModel

__all__ = ['User']


class User(BaseModel):
    """
    This is a model class for a GitHub user.

    Args:
        id (str): the GitHub ID of the user
        username (str): the name of the user
        email (str): the email of the user
        url (str): the profile page of the user
        organization (List[str]): the list of organizations in which the user is involved
        is_contributor (bool): whether the user is a contributor of the repository, default is False
        star_date (Optional[date]): the date on which the user starred the repository, default is None
    """
    id: str
    username: str
    email: str
    url: str
    organization: List[str] = []
    is_contributor: bool = False
    star_date: Optional[date] = None
