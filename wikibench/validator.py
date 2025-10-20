#Wikipeda checker - establish if we have a valid path
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "wikibench-validator/0.1 (contact@example.com)"
}

def check_link_exists(source_page, target_page):
    #check if source contains a link to target page
    url = f"https://en.wikipedia.org/wiki/{source_page}"
    #print(url)
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    #find all links in article content
    content = soup.find('div', {'id': 'mw-content-text'})
    if content is None:
        return False
    links = content.find_all('a', href=True)

    #check if source contains link to target
    for link in links:
        href = link['href']
        if f"/wiki/{target_page}" in href:
            return True

    return False

def get_all_links(page):
    url = f"https://en.wikipedia.org/wiki/{page}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    #find all links in article content
    content = soup.find('div', {'id': 'mw-content-text'})
    if content is None:
        return False
    links = content.find_all('a', href=True)
    links_ret = [link.get('href') for link in links]
    return links_ret

def check_mentions(source, target):
    url = f"https://en.wikipedia.org/wiki/{source}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    #get plaintext in article content
    content = soup.get_text()
    if content is None:
        return False
    
    #find mentions of target in source
    if target not in content:
        return False

    return True


def validate_path(path_list):
    #validate each step in the path by scraping wikipedia
    for i in range(0, len(path_list) - 1):
        source = path_list[i]
        target = path_list[i + 1]
        if not check_link_exists(source, target):
            if check_mentions(source, target):
                return False, True
            
            return False, False

    return True, True

def validate_mentions(path_list):
    #validate each step in the path by scraping wikipedia
    for i in range(0, len(path_list) - 1):
        source = path_list[i]
        target = path_list[i + 1]
        if not check_mentions(source, target):
            return False, f"No mention of {source} and {target}"
    return True


"""def validate_path(path_list):
    #validate each step in the path by scraping wikipedia
    for i in range(0, len(path_list) - 1):
        source = path_list[i]
        target = path_list[i + 1]
        if not check_link_exists(source, target):
            if check_mentions(source, target):
                return 5
            return 10
    return 0
"""

print(check_link_exists("Bradawl", "Screwdriver"))  # Should be True
print(validate_path(["Bradawl", "Screwdriver", "Tool", "Concept"]))
print(validate_path(["Bradawl", "Screwdriver", "Tool", "Bradawl"]))
#rint(get_all_links("Bradawl"))
print(check_mentions("Bradawl", "Screwdriver"))
