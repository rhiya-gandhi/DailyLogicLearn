# check if the 2 numbers are anagram 
def isanagram (n1:int, n2:int):
    return sorted(str(n1)) == sorted(str(n2))
