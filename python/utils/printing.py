def print_heading(text, level):
    if level == 1:
        formatted_text = (
            f"\n{'# ' + '=' * 72}"
            f"\n# {text.upper()}\n"
            f"{'# ' + '=' * 72}\n")
    elif level == 2:
        formatted_text = (
            f"\n# {'-' * 72}\n"
            f"# {text.title()}"
            f"\n# {'-' * 72}\n")
    elif level == 3:
        formatted_text = f"\n> {text.capitalize()} <\n"
    else:
        formatted_text = text
    print(formatted_text)