# Original function
def full_name_and_print(fname: str, mname: str, lname: str) -> None:
    """
    Concatenates the names together and prints them

    Arguments:
        fname (str) -- first name
        mname (str) -- middle name
        lname (str) -- last name
    """
    full_name = " ".join(name for name in [fname, mname, lname] if name)
    print(full_name)


# Modified function to satisfy Single Responsibility Principle
def full_name(fname: str, mname: str, lname: str) -> None:
    """
    Concatenates the names together and returns the full name

    Arguments:
        fname (str) -- first name
        mname (str) -- middle name
        lname (str) -- last name

    Returns:
        str -- the full name with only a single space between names
    """
    full_name = " ".join(name for name in [fname, mname, lname] if name)
    return full_name


if __name__ == "__main__":
    fname = "John"
    mname = "Doe"
    lname = "Wick"
    full_name_and_print(fname, mname, lname)
    print(full_name(fname, mname, lname))
