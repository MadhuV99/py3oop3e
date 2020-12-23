# list_comp_read_file.py
# import sys
# filename = sys.argv[1]
# header = ['S-No', 'email', 'last', 'first']
# line1 = ['sunday', 'sunday@example.com', 'sun', 'day']
# print(dict(zip(header, line1)))
# line2 = ['monday', 'monday@example.com', 'mon', 'day']
# print(dict(zip(header, line2)))

filename = 'contact_file.csv'
with open(filename) as file:
    header = file.readline().strip().split(",")
    contacts = [
        dict(zip(header, line.strip().split(","))) for line in file
    ]

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact)) 

