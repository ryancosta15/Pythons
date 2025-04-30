def is_opposite(s1,s2):
    if s1.isalpha() and s2.isalpha():
        s1 = s1.swapcase()
        if s1 == s2:
            return True
        else:
            return False
    else:
        return False
