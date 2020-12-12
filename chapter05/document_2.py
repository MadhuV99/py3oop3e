# document_2.py

class Document:
    
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''
    
    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        del self.characters[self.cursor.position]
    
    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join(self.characters))

    @property
    def string(self):
        return "".join(self.characters)

class Cursor:
    
    def __init__(self, document):
        self.document = document
        self.position = 0
    
    def forward(self):
        self.position += 1
    
    def back(self):
        self.position -= 1
    
    def home(self):
        while self.document.characters[self.position - 1] != "\n":
            self.position -= 1
            if self.position == 0:
            # Got to beginning of file before newline
                break
    
    def end(self):
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position] != "\n"
            ):
            self.position += 1 


def main():
    d = Document()
    d.insert('h')
    d.insert('e')
    d.insert('l')
    d.insert('l')
    d.insert('o')
    d.insert('\n')
    d.insert('w')
    d.insert('o')
    d.insert('r')
    d.insert('l')
    d.insert('d')
    d.cursor.home()
    d.insert("*")
    print("".join(d.characters))

    print(d.string)

    d.filename = "test_document2"
    # d.save()

if __name__ == '__main__':
    main() 
