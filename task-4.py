
phone_book = {}


def parse_input(income: str) -> tuple:
    """I struct the input to use it in the modul's functions!"""
    command = income.split(' ')[0]
    args = income.split(' ')[1:]
    return command, args

def add_contact(args: list) -> str:
    """I add new contacts to the phone-book."""
    if args[0] in phone_book:
        query = input('The name is already in the phone-book! Rewrite (y/n): ')
        if query == 'n':
            return "Adding contact was abborted"
    phone_book[args[0]] = args[1]
    return 'Contact added.'
    
def change_contact(args: list) -> str:
    """I change a contact in the phone-book."""
    try: # This must be in all the functions which take the args
        if args[0] in phone_book:
            phone_book[args[0]] = args[1]
            return 'Contact updated.'
        return "Sorry, I do not know this man!"
    except IndexError:
        return 'I need more arguments to commit the action!'

def show_phone(args: list) -> str:
    """I show the phone number of a chosen man."""
    if args[0] in phone_book:
        return phone_book[args[0]]
    return "Sorry, I don't know the man!"

def show_all() -> dict:
    """I return the phone-book to print it."""
    return phone_book

def main() -> None:
    """I rule the show!"""
    print('Welcome to the assistant bot!')
    while True:
        command, args = parse_input(input('Enter a command: '))
        match command.lower():
            case 'hello':
                print('How can I help you?')
            case 'add':
                print(add_contact(args))
            case 'change':
                print(change_contact(args))
            case 'phone':
                print(show_phone(args))
            case 'all':
                print(show_all())
            case 'close' | 'exit':
                print('Good bye!')
                break
            case _:
                print('Invalid command.')


if __name__ == '__main__':
    main()