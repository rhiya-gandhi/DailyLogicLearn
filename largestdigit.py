#largest digit in the number 
def largestdigit (n : int):
    digit = (str(abs(n)))
    return int(max(digit) for digit in n )