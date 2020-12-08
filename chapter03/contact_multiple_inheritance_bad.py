# contact_multiple_inheritabce.py

class Contact:
    
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code 

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone 

def main():        
    f = Friend('myname', 'myemail', 'myphone', 'mystreet', 'mycity', 'mystate', 'mycode')
    print(f.phone) 
    print(f.name, f.email, f.phone, f.street, f.city, f.state, f.code) 

if __name__ == '__main__':
    main()            
