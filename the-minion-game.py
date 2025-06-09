def minion_game(string):
    v1=string.upper()
    vowels="AEIOU"
    Manas_score=0
    Vedant_score=0

    length= len(string)

    for i in range(len(string)):
        if string[i] in vowels:
            Manas_score += 1
        else:
            Vedant_score +=1
        if Manas_score > Vedant_score:
            print("Manas",Manas_score)
        elif Vedant_score > Manas_score:
            print("Vedant",Vedant_score)
        else:
            print("Game Draw")

minion_game("SANIKA")