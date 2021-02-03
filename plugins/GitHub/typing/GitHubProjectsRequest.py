from typing import TypedDict


class GitHubProjectsRequest(TypedDict):
    '''
    in: path
    '''
    org: str
    '''
    Results per page (max 100)

    in: query
    '''
    per_page: int
    '''
    Page number of the results to fetch.

    in: query
    '''
    page: int
