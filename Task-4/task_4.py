def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return None


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot! Type [hello] to get started")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            print("\n Add  \n Change  \n Phone \n All \n Exit - Close \n")

        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("There must be two arguments => add [name] [phone]")

        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("There must be two arguments => change [name] [phone]")

        elif command == "phone":
            try:
                result = show_phone(args, contacts)
                if result is not None:
                    print(f"Phone number for contact {args[0]}: {result}")
                else:
                    print("Contact not found.")
            except IndexError:
                print("There must be => phone [name]")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
