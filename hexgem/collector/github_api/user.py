import requests


def get_starred_repos(username: str, per_page: int, page: int, token):
    API = f'/users/{username}/starred?per_page={per_page}&page={page}'
    headers = {'Authorization': 'token ' + token}
    response = requests.get(API, headers=headers)
    print(response.json())


if __name__ == '__main__':
    get_starred_repos('frankleeeee', 10, 0)
