# cached_webpage.py
from urllib.request import urlopen

class WebPage:
    
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content

def main():
    import time
    webpage = WebPage("http://ccphillips.net/")
    now = time.time()
    content1 = webpage.content
    print(time.time() - now)
    now = time.time()
    content2 = webpage.content
    print(time.time() - now)
    print('Same content? ', content2 == content1)
    print('http://ccphillips.net/\n')
    print(content2)


if __name__ == '__main__':
    main()     