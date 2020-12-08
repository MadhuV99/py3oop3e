# media_loader.py
import abc

class MediaLoader(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def play(self):
        pass
    
    @abc.abstractproperty
    def ext(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        print("this will play an ogg file")

class Wav(MediaLoader):
    pass        

def main():
    # x = Wav()
    # pass 

    o = Ogg()
    print('Object o instantiated from class Ogg!')
    print('Is o an instance of  MediaLoader? ', isinstance(o, MediaLoader))

    print('Is Ogg a subclass of  MediaLoader? ', issubclass(Ogg, MediaLoader))
    print('Is Ogg() an instance of  MediaLoader? ', isinstance(Ogg(), MediaLoader))

if __name__ == '__main__':
    main()  

