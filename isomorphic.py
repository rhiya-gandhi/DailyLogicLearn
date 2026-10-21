def isisomophic(s:str,t:str) -> bool:
    if len(s) != len(t):
        return False
    return len(set(s)) == len(set(t)) == len(set(zip(s,t)))