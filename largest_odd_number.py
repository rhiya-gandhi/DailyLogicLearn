#Given a string s representing a non-negative integer, find the largest-valued odd number that can be obtained as a substring of s.
#The returned number must be a string and must not contain leading zeros. If no odd number exists, return an empty string "".
#A substring is a contiguous sequence of characters within a string.
def largestOddNumber(s: str) -> str:
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i + 1]
    return ""