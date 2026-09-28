def remove_last(lst):
    """Removes the last element IN PLACE (mutates the caller's list)."""
    if lst:                      # guard: pop() on an empty list raises IndexError
        lst.pop()

if __name__ == "__main__":
    print("Q1: List Mutation")
    nums = [1, 2, 3, 4]
    print("  before:", nums)
    remove_last(nums)
    print("  after :", nums, "-> original list CHANGED (lists are mutable)")