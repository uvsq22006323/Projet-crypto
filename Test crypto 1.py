# test crypto 1
# FINI

def frequence(message_chiffre):
    resultat = []
    for ch in message_chiffre:
        if 97 <= ord(ch) <= 122:   # si chr compris entre ord(a) et ord(z)

            exist = True
            for i in range(len(resultat)):
                if resultat[i][0] == ch:
                    exist = False
            if exist:
                resultat.append([ch, round(message_chiffre.count(ch) /
                                 len(message_chiffre)*100, 2)])
    return(resultat)


texte = open('Texte 1', 'r')
final = open('Trad T1', 'w')

for ligne in texte:
    a = str(ligne)  # a = texte

freq = frequence(a)

# trouver le 'e'

maximum, cle1 = 0, 0

for i in range(len(freq)):
    k = freq[i][1]
    if k > maximum:
        maximum = k
        cle1 = freq[i][0]

print(maximum, cle1)

cle = ord('e') - ord(cle1)
print(cle)
res = ''

# décode

for ch in a:
    if 97 <= ord(ch) <= 122:
        if ord(ch) + cle > 122:
            res += chr(ord(ch) + cle - 26)
        else:
            res += chr(ord(ch) + cle)
    else:
        res += (ch)

final.write(res)

final.close()
texte.close()
