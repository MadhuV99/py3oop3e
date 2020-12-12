# document_1.py

class Document:
    
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''
    
    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1
    
    def delete(self):
        del self.characters[self.cursor]
    
    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))
    
    def forward(self):
        self.cursor += 1
    
    def back(self):
        self.cursor -= 1 

def main():
    doc = Document()
    doc.filename = "test_document1"
    doc.insert('h')
    doc.insert('e')
    doc.insert('l')
    doc.insert('l')
    doc.insert('o')
    print("".join(doc.characters))
    doc.back()
    doc.delete()
    doc.insert('p')
    print("".join(doc.characters)) 
    # doc.save()

if __name__ == '__main__':
    main() 
