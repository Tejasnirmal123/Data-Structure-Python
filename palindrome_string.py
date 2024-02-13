list = "ababa"
def palindrome(s,e,list):
    if s>e:
        return True
    if list[s] != list[e]:
        return False
    return palindrome(s+1,e-1,list)

ans = palindrome(0,len(list)-1,list)
print(ans)

    