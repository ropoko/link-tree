import time
import re
import requests
from bs4 import BeautifulSoup

class Tree:
    def __init__(self, dad: str, son: []):
        self.dad = dad
        self.son = son
        self.build()

    def build(self):
        pass
        # print(self)

def timer(func):
    def timer(*args, **kwargs):
        """a decorator which prints execution time of the decorated function"""
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("-- executed %s in %.4f seconds" % (func, (t2 - t1)))
        return result
    return timer

@timer
def get_a(url = 'https://ropoko.net'):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a')

    dads = []

    for result in results:
        if re.search('https?:\/\/(www\.)?([a-zA-Z0-9]*)\.([a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?)\/?', result['href']):
            print(result['href'])
        else:
            print('child', result['href'])
        # for relative url -> generate an absolute one
        # if result['href'].find('http') == -1:
        #    new_url = url + result['href']
    # print(dads)



#     if new_url.startswith(url):
#         # tree = Tree(url, new_url)

if __name__ == '__main__':
    get_a()

# https://ropoko.net/
# |
# | -- https://ropoko.net/projects
# | -- https://ropoko.net/about
# | -- https://ropoko.net/tags
# | -- https://ropoko.net/posts/firstPost