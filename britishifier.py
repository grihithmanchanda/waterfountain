import random

class British:
    string = input("say something: ")

    
    
    our = string.replace("or", "our")
    chewsday = our.replace("tuesday", "chewsday")
    schewpid = chewsday.replace("stupid", "schewpid")
    biscuit = schewpid.replace("cookie", "biscuit")
    centre = biscuit.replace("er", "re")
    oi = centre.replace("hey", "oi")    
    
    noT = oi.replace("t", "'")

    listwords = noT.split()
    
    for i in range(len(listwords)):
        probability = random.uniform(0,1)
        if probability > 0.8:
            listwords.insert(i, 'bloody')
    
    final = ' '.join(listwords)

    british = final.upper()
    print(british)
