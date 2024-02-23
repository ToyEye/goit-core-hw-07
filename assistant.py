from handlers import add_contact, change_contact, show_all,show_phone
from decorators import input_error
from classes import AddressBook

# @input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

   

def main():

    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command =='change':
            print(change_contact(args,book))
        elif command == "phone":
            print(show_phone(args,book))    
        elif command == "all":
            print(show_all(book))    

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()