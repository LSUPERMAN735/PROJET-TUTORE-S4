# RSA crypte et décrypte avec les nombres premiers
import math
from random import choice


#de Javascript à Python
codageGroupSize = 0
    #def private_tableComplete(): #définit la table de conversion
constAuthorizedChar = "0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&~#|*+-\\/=%!:?,.<>'àâçéèêëïîöôüûù" + '"'

tdesblocs = 3

#qp sélecteur de nombres premiers :
qplist= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,151, 157, 163, 167, 173, 179, 
181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 
1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,
1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567,
1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789,
1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999,2003, 2011, 2017, 2027, 2029, 2039,
2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287,
2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539,
2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 
2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 7727, 7741,
7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829 ]
def qp() :
    while True:
        p = choice(qplist)
        q = choice(qplist)
        if p != q:
            return [p, q]

#calcul le pgcd entre les nombres premiers
def private_pgcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
#fonction Inverse modulaire : modulo inversé entre phi et l'argument m
def private_inversemodulaire(phi, m):
    for x in range(1, m):
        if (phi * x) % m == 1:
            return x
    return None

# def private_pgcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     g, y, x = private_pgcd(b%a,a)
#     return (g, x - (b//a) * y, y)
# def private_inversemodulaire(phi, m):
#     g, x, y = private_pgcd(a, m)
#     if g != 1:
#         raise Exception('Pas d\'inverse modulaire')
#     return x%m

    
# calcul le nombre premier entre eux et vérifie que x est différent de l facultatif, pour calculer e et prend phi en paramètre
def private_nbprementreux(phi):
    l = []
    for x in range(2, phi):
        if private_pgcd(phi, x) == 1 and private_inversemodulaire(x, phi) != None:
            l.append(x)
        if len(l) > 5: break
    for x in l:
        if x == private_inversemodulaire(x, phi):
            l.remove(x)
    return l

#fonction standard qui ne garde que les chiffres a été réadapté en javascript
def private_standard(entree):
    longueur = len(str(entree))#commentable
    res = list(filter(str.isdigit, str(entree)))# isdiggit remplace alphabet/que numéro
    entree_standard = str("".join(res))
    # print('entree_standard',entree_standard)
    return entree_standard

#utile pour récupérer les caractères avec sa valeur de position
def private_indexInAuthorizedChar(lettre): 
    return constAuthorizedChar.index(lettre)
  
# Calcul le modulo "Modulo" de "base" a la puissance "exposant" INDISPENSABLE
def private_moduloExpo(base, exposant, Modulo):
    moduloBase2 = []

    # Niveau de puissance de 2 à considérer
    moduloLevel = max(math.floor(math.log(exposant) / 0.6931471805599), 1) 
    # Préparation du tableau de transcodage
    moduloBase2.append(base % Modulo)
    for level in range(1, moduloLevel + 1):
        moduloBase2.append((moduloBase2[level - 1] ** 2) % Modulo)#simplifier en ^

    # Utilisation pour décomposition en utilisant le tableau
    expoDec = exposant
    valeur = 1
    level = moduloLevel

    while (expoDec > 0):
        if (expoDec >= math.pow(2,level)):
            valeur = (valeur * moduloBase2[level]) % Modulo #boucle for obligatoire
            expoDec -= math.pow(2, level)
            #level -= 1 #important à la fin pas à la ligne au-dessus sinon cela peut créer une boucle infinie
            level=level-1
        else:
            level=level-1 #level-=1
    return valeur

#fonction pour chiffrer le bloc
def private_encodage(message, e, n):
    messageCode = ""
    messageNum=""
    preSize = math.ceil(math.log(n) / math.log(10)) # calculer en fonction de n

    for k in range(0, len(message)):
        chiffre= str(private_indexInAuthorizedChar(message[k]))
        if(int(chiffre) < 10):
            chiffre="0" + chiffre
        messageNum += chiffre
        
    while(len(messageNum) % tdesblocs > 0):
        messageNum = "0" + messageNum
    
    #chiffre le groupe
    for k in range(0, len(messageNum), tdesblocs):
        GroupeValue = int(messageNum[k : k + tdesblocs])
        groupePreCode = private_moduloExpo(GroupeValue, e, n)
        xx=str(groupePreCode)
        while(len(xx) < preSize):
            groupePreCode = "0" + str(groupePreCode)
            xx = str(groupePreCode)
        
        messageCode += str(groupePreCode)
        messageCode += " "
    
    return messageCode
  
#fonction pour déchiffrer le bloc
def private_decodage(messageCode, d, n)  :
    continu = private_standard(messageCode)
    preSize = math.ceil(math.log(n) / math.log(10))
    nombre = ""
    nB=0
    while(len(continu) > 0):
        groupeCode = int(continu[0:preSize])
        continu = continu[preSize:len(continu)]
        #déchiffre le groupe
        groupeLettre = private_moduloExpo(groupeCode, d, n)
        if(nB > 0):
            xx = str(groupeLettre)
            while(len(xx) < tdesblocs):
                groupeLettre = "0" + str(groupeLettre)
                xx = str(groupeLettre)
        nB += 1
        nombre += str(groupeLettre)
    
    message = ""
    for k in range(0, len(nombre), 2):
        lettre= int(nombre[k:k+2])
        message += constAuthorizedChar[lettre]
    
    return message
 
#adaptation python javascript
#fonction pour générer les clés utilisées
def GENERATEUR_DE_CLE():
    # e=377    
    # p=1511
    # q=907
    q,p = qp() #q,p pour que ça soit un int sinon ça sera une list !!!
    n=p*q
    phi = (p-1) * (q-1)#ajout de phi
    print ('p=',p)
    print('q=',q)
    print ('phi=',phi)
    euler = n - p - q + 1 
    tmpNe = 1
    e = choice(private_nbprementreux(phi))
    # d = private_inversemodulaire(e, phi)#pas de phi,e mais c'est théoriquement
    d = 1
    while(((d * e) % euler) != 1):
        tmpNe += 1
        d = math.ceil( tmpNe * euler / e)

    public_key = [e, n]
    private_key = [d, n]
    return [public_key, private_key]


#retour à Python
# méthode pour chiffrer un message
def chiffre_string(s, public_key):
    #s correspond à la châine du message entier :, nom, et espace inclus
    e, n = public_key
    # print('message encrypte', private_encodage(s, e, n))
    return private_encodage(s, e, n)
    
# méthode pour déchiffrer un message
def dechiffre_string(s, private_key):
    d, n = private_key
    return private_decodage(s, d, n)


