from .GitHubCardsState import GitHubCardsState
from typing import TypedDict

class GitHubCardsRequest(TypedDict):
    '''
    column_id parameter

    in: path
    '''
    column_id: int
    '''
    Filters the project cards that are returned by the card's state. @see GitHubCardsState.

    in: query
    '''
    archived_state: GitHubCardsState
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
