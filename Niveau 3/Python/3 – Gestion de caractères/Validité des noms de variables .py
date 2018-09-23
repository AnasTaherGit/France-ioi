def is_valide(nom):
    nom=nom[1:]
    print(nom)
    for lettre in nom:
        if (not lettre.isalpha()) and (not lettre.isdigit()) and (lettre!="_"):
            print(lettre)
            return False
    return True

Nbvar=int(input())
Nb_var=[]

for i in range(0,Nbvar):
    var=input()
    Nb_var.append(var)

for var in Nb_var:
    if var[0].isalpha() or var[0]=="_":
        if is_valide(var):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
            
    
