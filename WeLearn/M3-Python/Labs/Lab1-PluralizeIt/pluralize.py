print("Hello User!")

num = int(raw_input("Enter number: "))
word = raw_input("Enter word: ")



def pluralize(word):
    if num != 1:
        if word[-3:] == "ife":
            return word[:-3] + "ives"
        elif word[-2:] == "ch":
            return word[:-2] +'ches'
        elif word[-2:] == "sh":
            return word[:-2] +'shes'
        elif word[-2:] == "us":
            return word[:-2] +'i'
        elif word[-2:] == "ay":
            return word[:-2] +'ays'
        elif word[-2:] == "oy":
            return word[:-2] +'oys'
        elif word[-2:] == "ey":
            return word[:-2] +'eys'
        elif word[-2:] == "uy":
            return word[:-2] +'uys'
        elif word[-1:] == "y":
            return word[:-1] +'ies'

        else:
            return word +'s'
    else:
        return word


print(str(num) + " " + pluralize(word))
