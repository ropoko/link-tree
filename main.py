import sys
import re
import time
import requests
from bs4 import BeautifulSoup


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add(self, child):
        child.parent = self
        self.children.append(child)


def timer(func):
    def timer(*args, **kwargs):
        """a decorator which prints execution time of the decorated function"""
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("\n -- executed in %.4f seconds" % (t2 - t1))
        return result
    return timer

@timer
def main(url: str) -> None:
    tree = Tree(url)

    links = get_link(url)    

    for link in links:
        tree.add(Tree(link))

    show(tree)


def get_link(url: str) -> [str]:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a')

    links = [result['href'] for result in results]

    return links


def show(tree: Tree):
    print(f'\n -> {tree.data}')

    levels = '| --'

    for link in tree.children:
        print(f'{levels} {link.data}')

if __name__ == '__main__':
    if re.search('https?:\/\/(www\.)?([a-zA-Z0-9]*)\.([a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?)\/?', sys.argv[1]) == None:
       print('Insert a valid URL.')
       exit(1)
    
    main(sys.argv[1])

# https://ropoko.net/
# |
# | -- https://ropoko.net/projects
# | -- https://ropoko.net/about
# | -- https://ropoko.net/tags
# | -- https://ropoko.net/posts/firstPost
# | -- | -- https://ropoko.net/posts/firstPost
# | -- | -- https://ropoko.net/posts/firstPost
# | -- | -- https://ropoko.net/posts/firstPost
# | -- | -- | -- https://ropoko.net/posts/firstPost
