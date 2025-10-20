import requests
from bs4 import BeautifulSoup
from validator import check_link_exists, validate_path, get_all_links, check_mentions


def score_path(path_list):
    score = 0
    
    #validation + mentions -- +10 for invalid path, +5 for invalid path with exact word mention
    valid_path, valid_mention = validate_path(path_list)
    if not valid_path: 
        score += 10
        if valid_mention:
            score -= 5

    #+7 for invalid path, conceptually related but not mentioned
    #+6 for length limit/LLM timeout

    #+15 for giving up
    #+20 for cheating
    #-1 for particularly creative connection(?)

    return
