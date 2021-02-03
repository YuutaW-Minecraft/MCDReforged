from .typing.GitHubUserInfo import GitHubUserInfo
import requests

class GitHub:
    api_root: str

    def __init__(self):
        self.api_root = "https://api.github.com"
    
    def build_uri(self, method: str) -> str:
        return f"{self.api_root}{method}"

    def get_user(self, id: str) -> GitHubUserInfo:
        r = requests.get(self.build_uri(f'/users/{id}'))

        if r.status_code == 200:
            return r.json()
        else:
            raise Exception("Something went wrong when getting users.")
