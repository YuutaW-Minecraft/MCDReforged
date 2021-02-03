from typing import TypedDict


class GitHubColumnsRequest(TypedDict):
    '''
    in: path
    '''
    project_id: int
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
