def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first.title() + ' ' + middle.title() + ' ' + last.title()
    else:
        full_name = first.title() + ' ' + last.title()
    return full_name
