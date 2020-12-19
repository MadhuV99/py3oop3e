# update_url.py
from threading import Timer
import datetime
from urllib.request import urlopen
import pickle

class UpdatedURL:
    
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()
    
    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()
    
    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        new_state = self.__dict__.copy()
        if "timer" in new_state:
            del new_state["timer"]
        return new_state

    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()

def main():
    web_url = "http://dusty.phillips.codes"
    web_file = "pickled_web"
    upd_web = UpdatedURL(web_url)

    with open(web_file, 'wb') as file:
        pickle.dump(upd_web, file)

    with open(web_file, 'rb') as file:
        loaded_data = pickle.load(file)

    # assert loaded_data == upd_web
    print(f"Successfully pickled {web_url} as {web_file}.")

if __name__ == '__main__':
    main()
