def isAna(text1, text2):
    if not text1 or text2:
        return False
    else:
        text1 = text1.lower
        text2 = text2.lower
        result1 = ""
        result2 = ""
        for i in range(text1):
            if text1[i] == " ":
                
            elif text1[i] > result1:
                result1 = result1 + text1[i]
            else:
                result1 = text1[i] + result1
        
        for i in range(text2):
            if text2[i] == " ":

            elif text2[i] > result2:
                result2 = result2 + text2[i]
            else:
                result2 = text2[i] + result2

        if result1 == result2:
            return True
        else:
            return False
        
print("is Funeral an anagram of Real Fun?...", isAna("Funeral", "Real Fun"))
