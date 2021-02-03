from typing import TypedDict


class GitHubUserInfo(TypedDict):
    id: str
    name: str
    url: str
    html_url: str
    avatar_url: str
    bio: str