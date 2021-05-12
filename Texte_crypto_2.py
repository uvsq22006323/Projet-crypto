# Texte_crypto_2
# gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu
# vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo
# gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu
# vlkwwoxxi.


def frequence(message_chiffre):
    resultat = []
    for c in message_chiffre:
        if 97 <= ord(c) <= 122:   # si chr compris entre ord(a) et ord(z)

            exist = True
            for i in range(len(resultat)):
                if resultat[i][0] == c:
                    exist = False
            if exist:
                resultat.append([c, round(message_chiffre.count(c) /
                                 len(message_chiffre)*100, 2)])
    return(resultat)


def cherche_cle(liste):
    Valmax = 0
    for i in range(len(liste)):
        k = liste[i][1]
        if k > Valmax:
            Valmax = k
            cle1 = liste[i][0]
    return(Valmax, cle1)  # pourcentage, lettre


texte = open("Texte 2", 'r')
res = open('Trad_T2', 'w')

lettre = []
mots_cles = ['fichier', 'taille', 'mot', 'de', 'passe', 'lettres']

for ligne in texte:
    a = str(ligne)  # # # on a le texte

fr = frequence(a)  # # # fréquence texte

res.write('TRAD TEXTE 2 \n')
valmax, cle_e = cherche_cle(fr)  # # # donne x = e

for i in a:
    if i == cle_e:
        i = cle_e

b = a.split()  # mots dans a

for i in range(len(b)):                # trouver des mots
    i = str(i)
    if len(str(i)) == 2 and i[1] == cle_e:
        pass

res.write('\n')


for ch in a:
    if ch == 'x':
        res.write('e')  # trouvé en cherchant avec la fréquence
    elif ch == 'g':
        res.write('l')  # trouvé par déduction en cherchant 'le'
    elif ch == 'u':
        res.write('t')  # trouvé un mot 'unklle' qui aurait pu être 'taille'
    elif ch == 'n':
        res.write('a')  # trouvé un mot 'unklle' qui aurait pu être 'taille'
    elif ch == 'k':
        res.write('i')  # trouvé un mot 'unklle' qui aurait pu être 'taille'
    elif ch == 'i':
        res.write('s')  # trouvé un mot 'qaiie' qui aurait pu être 'passe'
    elif ch == 'q':
        res.write('p')  # trouvé un mot 'qaiie' qui aurait pu être 'passe'
    elif ch == 'o':
        res.write('r')  # trouvé par déduction
    elif ch == 's':
        res.write('o')  # trouvé par déduction
    elif ch == 'v':
        res.write('c')  # trouvé par déduction
    elif ch == 'd':
        res.write('n')  # trouvé par déduction
    elif ch == 'l':
        res.write('h')  # pour écrire 'fichier'
    elif ch == 'w':
        res.write('f')  # pour écrire 'fichier'
    elif ch == 'c':
        res.write('d')  # pouur écrire 'fichier'
    elif ch == 'y':
        res.write('u')  # pour compléter le 'un'
    elif ch == 'f':
        res.write('m')  # trouvé par déduction
    elif ch == 'm':
        res.write('g')  # trouvé par déduction
    elif ch == 'a':
        res.write('z')  # trouvé par déduction
    else:
        res.write(str(ch))

res.close()
texte.close()
