def isPalindrome(x: int) -> bool:
    if x<0 or (x > 0 and x % 10 == 0): return False
    y = x
    result = 0
    while y > 0:
        result = result * 10 + y % 10
        y = y // 10
    if result == x: return True
    return False

