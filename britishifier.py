class British:
    string = input("say something: ")
    
    our = string.replace("or", "our")
    chewsday = our.replace("tuesday", "chewsday")
    biscuit = chewsday.replace("cookie", "biscuit")
    centre = biscuit.replace("er", "re")
    oi = centre.replace("hey", "oi")    
    
    noT = oi.replace("t", "'")
    british = noT.upper()
    print(british)