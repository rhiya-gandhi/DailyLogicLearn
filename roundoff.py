#round off to the nearest 10 
def roundToNearest(s: str) -> str:
    n=int(s)
    return n//10*10 if n%10<=5 else (n//10+1)*10