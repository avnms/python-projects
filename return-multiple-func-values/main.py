def split_full_name(full_name: str) -> tuple[str, str, str]:
    fname = mname = lname = ""
    parts = full_name.split()

    if len(parts) >= 1:
        fname = parts[0]

    if len(parts) >= 2:
        mname = parts[1]

    if len(parts) == 3:
        lname = parts[2]

    if not lname:
        mname, lname = (lname, mname)

    return (fname, mname, lname)


if __name__ == "__main__":
    fname, mname, lname = split_full_name("John Doe Wick")
    print(f"First name: {fname}\nMiddle name: {mname}\nLast name: {lname}")
