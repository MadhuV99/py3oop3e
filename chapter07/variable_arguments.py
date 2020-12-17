# variable_arguments.py

def get_pages(*links):
    for link in links:
        #download the link with urllib
        print(link) 

class Options:
    default_options = {
    'port': 21,
    'host': 'localhost',
    'username': None,
    'password': None,
    'debug': False,
    }
    
    def __init__(self, **kwargs):
        # self.options = dict(Options.default_options)
        # self.options.update(kwargs)
        self.options = {**Options.default_options, **kwargs}

    def __getitem__(self, key):
        return self.options[key]

def main():
    # get_pages()
    # get_pages('http://www.archlinux.org')
    # get_pages('http://www.archlinux.org',
    #             'http://ccphillips.net/')

    options = Options(username="dusty", password="drowssap", debug=True)
    print(options['debug'])
    print(options['port'])
    print(options['username'])

if __name__ == '__main__':
    main() 