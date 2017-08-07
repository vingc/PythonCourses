#! python
#graduation script of <A byte of python>

#a dictionary of contacts

class Person:

    def __init__(self, name, addr='', phone=''):
        self.name = name
        self.addr = addr
        self.phone = phone

    def show(self):
        print("name: {0}, addr: {1}, phone: {2}".format(self.name, self.addr, self.phone))

    def __del__(self):
        print("del ", self.name)

    def __repr__(self):
        return '"name: {0}, addr: {1}, phone: {2}"'.format(self.name, self.addr, self.phone)

Contacts = {}
Contacts["bib"] = Person("bib", "aaa", "123")
Contacts["did"] = Person("did", "bbb", "234") 

#print(Contacts)

Contacts["cic"] = Person("cic", "fjjfj", "123" )

print(Contacts)
if "did" in Contacts:
    pep = Contacts["did"]
    pep.addr = "sdf"
    print(repr(pep))
else:
    print("dont' find did")
