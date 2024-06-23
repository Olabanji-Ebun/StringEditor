def make_uppercase(s):
    return s.upper()


def make_lowercase(s):
    return s.lower()


def reverse_string(s):
    return s[::-1]


def change_characters(s, ch1, ch2):
    return s.replace(ch1, ch2)


def undo(history):
    if history:
        return history.pop()
    return ""


def process_commands(initial_string):
    current_string = initial_string
    history = []

    while True:
        command = input("Enter command: ").strip()
        if command == 'X':
            break
        elif command == 'U':
            history.append(current_string)
            current_string = make_uppercase(current_string)
        elif command == 'L':
            history.append(current_string)
            current_string = make_lowercase(current_string)
        elif command == 'R':
            history.append(current_string)
            current_string = reverse_string(current_string)
        elif command.startswith('C'):
            parts = command.split()
            if len(parts) == 3:
                history.append(current_string)
                current_string = change_characters(current_string, parts[1], parts[2])
        elif command == 'Z':
            current_string = undo(history)

        print(f"Current string: {current_string}")

    print(f"Final output: {current_string}")


if __name__ == "__main__":
    initial_string = input("Enter initial string: ")
    process_commands(initial_string)
