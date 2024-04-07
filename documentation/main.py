from uuid import uuid4


# A function without documentation
def get_uuid_no_docstring():
    return uuid4().hex


# The same function with documentation using docstrings
def get_uuid():
    """
    Generate a shortened UUID4 value to use as the
    primary key for database records

    Returns:
        string: A shortened (no '-' characters) UUID4 value
    """
    return uuid4().hex


if __name__ == "__main__":
    print(help(get_uuid))
