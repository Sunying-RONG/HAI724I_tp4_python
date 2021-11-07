import sys
n = int(sys.argv[1])
np = [2]
for candidat in range(3, n+1) :
    premier = True
    for diviseur in np :
        if candidat % diviseur == 0 :
            premier = False
            break # arret la boucle la plus proche 
    if premier == True :
        np.append(candidat)

print(np)