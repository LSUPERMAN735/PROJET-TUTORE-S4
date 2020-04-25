#Pour lancer le serveur qui fait transiter les messsages
from socket import *
from threading import Thread
import urllib.request

client_sock = []    # stocke les sockets client 
adresses_client = {}   # stocke les adresses {clé: socket client , valeurs: adresse client }
public_key = []     # stocke les clés publiques des clients


def communication_entrante_acceptée():
    #ACCEPTE les communications entrantes et les maintient pour les clients
    client, adresse_client = SERVER.accept()
    client_sock.append(client)#ajoute à la socket dy client
    print("%s:%s est connecté." % adresse_client) # affiche l'adresse IP de la personne conectée
    public_key.append(client.recv(BUFFER_SIZE)) #ajoute l'adresse IP publique du client reçu
    adresses_client[client] = adresse_client


def conteneur_client1(client_sock, adresses_client):
    # Contient le premier client (connexion)
    print("clé publique client1",public_key[1])
    client_sock[0].send(public_key[1])# envoie la clé publique
    while True:
        msg0 = client_sock[0].recv(BUFFER_SIZE) #reçoit le message du client1
        client_sock[1].send(msg0) # envoie le message du client1
        print(" Client 1: %s" % msg0.decode('utf8')) # affiche le message chiffrée du client1



def conteneur_client2(client_sock, adresses_client):
    #Contient le deuxième client (connexion)
    print("clé publique client2",public_key[0])
    client_sock[1].send(public_key[0])# envoie la clé publique du client2
    while True:
        msg1 = client_sock[1].recv(BUFFER_SIZE) #reçoit le message du client2
        client_sock[0].send(msg1) # envoie le message du client2
        print(" Client 2: %s" % msg1.decode('utf8')) # affiche le message chiffrée du client2



#****Partie SOCKET****
ippub = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')
print ('L\'adresse IP publique est :', ippub)

IP = gethostbyname(gethostname())     # récupère l'adresse IP
port = 5566 # port d'écoute utilisé
BUFFER_SIZE = 1024   # taille en mémoire tampon du récepteur
adresse = (IP, port)  # adresse du serveur socket utilisé avec le port

SERVER = socket(AF_INET, SOCK_STREAM)   # create socket object
SERVER.bind(adresse)    # Association de l'IP du socket et le numéro du port.

SERVER.listen(2)
print('IP du serveur: ', IP)
print('Port du serveur: ', port)
print("En attente de connexion...")
communication_entrante_acceptée() # accepte la communication du premier client connectée
communication_entrante_acceptée()# accepte la communication du second client connectée

Thread(target = conteneur_client1, args = (client_sock, adresses_client)).start() #contient la tâche du client1
Thread(target = conteneur_client2, args = (client_sock, adresses_client)).start() #contient la tâche du client2
print('Conversation chiffré: ') #affiche la comunication chiffrée
SERVER.close() #ferme la connexion du serveur
