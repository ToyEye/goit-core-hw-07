from decorators import input_error
from classes import Record

@input_error
def add_contact(args, book):
    name, phone = args
    findName = book.find(name)
    
    if not findName :
        new_record = Record(name)
        new_record.add_phone(phone) 
        book.add_record(new_record)
        
        return "Contact added."
    else:
        return "Contact exist"

@input_error
def change_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Conctact not exist"
    
@input_error
def show_phone(args, contacts):
    name = args[0]

    contacts_phone = contacts.get(name)

    if contacts_phone:
        return contacts_phone

    else:
        return "Conctact not exist"
    
@input_error
def show_all(book):
    print(book)
    for name, record in book.data.items():
        print(record)
        return record


@input_error
def add_birthday(args, book):
    pass
    # реалізація

@input_error
def show_birthday(args, book):
    pass
    # реалізація

@input_error
def birthdays(args, book):
    pass
    # реалізація
