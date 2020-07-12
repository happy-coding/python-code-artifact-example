def is_palindrome(check_this: str) -> bool:
    if not check_this:
        return False
    return check_this == check_this[::-1]
