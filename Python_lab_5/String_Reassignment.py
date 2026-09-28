def change_string(s):
    """Tries to replace the first character with 'X'.
    Strings are immutable, so s[0] = "X" would raise TypeError.
    We build a NEW string and rebind the local name s only.
    """
    s = "X" + s[1:]
    return s


if __name__ == "__main__":
    original = "hello"

    print("before:", original)

    new_string = change_string(original)

    print("after:", new_string,
          "--> original string UNCHANGED (strings are immutable)")

    