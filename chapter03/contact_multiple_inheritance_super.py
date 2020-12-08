# contact_multiple_inheritabce.py

class Contact:
    
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code 

class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
    # def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone 

def main():        
    f = Friend(name='myname', email='myemail', phone='myphone', street='mystreet', city='mycity', state='mystate', code='mycode')
    # f = Friend(name='myname', email='myemail', street='mystreet', city='mycity', state='mystate', code='mycode')
    print(f.phone) 
    print(f.name, f.email, f.phone, f.street, f.city, f.state, f.code) 

if __name__ == '__main__':
    main()            
