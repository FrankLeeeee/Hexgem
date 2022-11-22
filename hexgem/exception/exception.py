'''
File: exception.py
Project: Hex
File Created: Tuesday, 22nd November 2022 4:53:52 pm
Author: Li Shenggui (somerlee.9@gmail)
-----
Last Modified: Tuesday, 22nd November 2022 4:54:09 pm
Modified By: Li Shenggui (somerlee.9@gmail>)
-----
'''


class TokenNotFound(Exception):
    """
    This is an exception raised when a token is not given to query github API.
    """
    pass
