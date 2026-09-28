def add_entry(d):
    """Mutates the dict the caller passed in."""
    d["new_key"] = "new_value"

def reassign_dict(d):
    """Rebinds the LOCAL name d to a brand-new dict.
    The caller's dict is untouched."""
    d = {"replaced": True}
    return d

if __name__ == "__main__":
    print("\nQ3: Dictionary Mutation vs Rebinding")
    data = {"a": 1}
    print("  start:", data)
    add_entry(data)
    print("  after add_entry     :", data, "-> CHANGED (mutation)")
    reassign_dict(data)
    print("  after reassign_dict :", data, "-> UNCHANGED (rebinding is local)")

    

