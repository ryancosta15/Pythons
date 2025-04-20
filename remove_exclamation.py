def remove_exclamation_marks(s):
        if "!" in s:
            while "!" in s:
                s=s.replace("!","")
            return s
        else:
            return s
