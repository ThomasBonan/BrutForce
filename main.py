

mdpATrouver = input("Insérer le mot de passe a trouver : ")

def verification(mdpATester,test):
    if mdpATester == test :
        print("Le mot de passe est "+ mdpATester)
        return True



def brutForce(mdpATester):
    mdpTest = ''
    for i in range(0,len(mdpATester)) :
        for j in range(33,126) :
            print(mdpTest+chr(j))
            if mdpATester[i]==chr(j):
                mdpTest+=chr(j)
                if verification(mdpATester,mdpTest)==True:
                    break



brutForce(mdpATrouver)