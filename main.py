import sys
import re
import time
import requests
from bs4 import BeautifulSoup

LINKS_SHOWED = ['#']

def timer(func):
    def timer(*args, **kwargs):
        """a decorator which prints execution time of the decorated function"""
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("-- executed %s in %.4f seconds" % (func, (t2 - t1)))
        return result
    return timer

# @timer
def get_a(url: str, limit: int = 0):
    LINKS_SHOWED.append(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a')

    for result in results:
        new_url: str = result['href']

        if new_url.startswith('/'):
            new_url = LINKS_SHOWED[1] + new_url

        if new_url not in LINKS_SHOWED:
            print(f"|-- {new_url}")
            LINKS_SHOWED.append(new_url)

            #cont: int = 0
            #while cont <= limit:
            #    cont += 1
            get_a(new_url)


if __name__ == '__main__':
    #if re.search('https?:\/\/(www\.)?([a-zA-Z0-9]*)\.([a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?)\/?', sys.argv[1]) == None:
    #    print('Insert a valid URL.')
    #    exit(1)
    #get_a(sys.argv[1], int(sys.argv[2]))
    get_a('https://ropoko.net', 5)

# https://ropoko.net/
# |
# | -- https://ropoko.net/projects
# | -- https://ropoko.net/about
# | -- https://ropoko.net/tags
# | -- https://ropoko.net/posts/firstPost