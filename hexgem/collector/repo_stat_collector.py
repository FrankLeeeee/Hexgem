'''
File: repo_stat_collector.py
Project: Hexgem
File Created: Tuesday, 22nd November 2022 4:27:56 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Tuesday, 22nd November 2022 4:36:48 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''

__all__ = ['RepositoryStatsCollector']


class RepositoryStatsCollector:
    """
    This is a class to handle the data retrieval from GitHub.


    """

    def __init__(self, repository: str, token: str = None) -> None:
        pass

    def get_star_history(self, start_date, end_date):
        pass

    def get_commit_history(self, start_date, end_date, branch: str = None):
        pass

    def get_issue_history(self, start_date, end_date, branch: str = None):
        pass

    def get_pull_request_history(self, start_date, end_date, branch: str = None):
        pass

    def get_daily_pull_request_count(self, start_date, end_date, branch: str):
        pass

    def get_daily_issue_count(self, start_date, end_date):
        pass

    def get_major_contributors(self, top_k: int):
        pass
