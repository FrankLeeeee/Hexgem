'''
File: user_stat_collector.py
Project: Hexgem
File Created: Tuesday, 22nd November 2022 4:27:56 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Tuesday, 16th December 2022 17:34:00 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

__all__ = ['UserStatsCollector']


class UserStatsCollector:
    """
    This is a class to handle the data retrieval from GitHub for a user.


    """

    def __init__(self, userID: str, token: str = None) -> None:
        self._user_id = userID
        self._token = token
