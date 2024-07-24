def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please enter a valid name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter a command and arguments."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot! Type [hello] to get started")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            print("\n Add  \n Change  \n Phone \n All \n Exit - Close \n")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            try:
                result = show_phone(args, contacts)
                if result is not None:
                    print(f"Phone number for contact {args[0]}: {result}")
                else:
                    print("Contact not found.")
            except IndexError:
                print("Give me name")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
