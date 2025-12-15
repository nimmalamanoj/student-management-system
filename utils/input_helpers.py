def get_int_input(prompt: str):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def get_optional_int_input(prompt: str):
    value = input(prompt)
    if value.strip() == "":
        return None
    try:
        return int(value)
    except ValueError:
        print("Invalid number. Skipping input.")
        return None
