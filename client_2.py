from socket import *
from threading import Thread
import tkinter, sys, time
import RSA

def recevoir():
    #Reçoit les messages.
    message_list.insert(tkinter.END, "Bonjour! %s" % NOM)
    message_list.insert(tkinter.END, " Vous êtes en ligne!")
    while True:
        try:
            message = CLIENT.recv(BUFFER_SIZE).decode("utf8")
            print("décrypte message", message, " avec ma clé privée", private_key_2)
            message = RSA.dechiffre_string(message, private_key_2)
            print("le message décrypté est", message)
            message_list.insert(tkinter.END, message)
        except OSError:  # Si l'utilisateur se déconnecte
            print('OSERROR')
            break
def send(event = None):  # évènement passé par le binders.
    #Pour send des messages.
    message = my_message.get()    
    my_message.set("")  # Vide le champ de saisie
    message = NOM + ": " + message
    message_list.insert(tkinter.END, message)
    print("chiffre le message", message, " avec la clé publique de l'autre", public_key_1)
    message = RSA.chiffre_string(message, public_key_1)
    print("le message cryptée est ", message)
    CLIENT.send(bytes(message, "utf8"))

def fermeture(event = None):
   #Quand on clique fermer la fenêtre
    message_list.insert(tkinter.END, "déconnexion...")
    time.sleep(2)
    CLIENT.close()
    mytk.destroy()
    mytk.quit()
    sys.exit()

#----INTERFACE GRAPHIQUE tkinter GUI----
mytk = tkinter.Tk()
mytk.title("Projet tutoré S4 client2")

messages_frame = tkinter.Frame(mytk)
my_message = tkinter.StringVar()  # Pour les messages à être send.
my_message.set("Coucou")
scrollbar = tkinter.Scrollbar(messages_frame)  # Pour naviguer entre les messages.
# Conteneur du message
message_list = tkinter.Listbox(messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(mytk, textvariable=my_message)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(mytk, text = "Envoyer", command = send)
send_button.pack()

mytk.protocol("WM_DELETE_WINDOW", fermeture)


#****Partie SOCKET****
#IP = input('IP: ')
#PORT = int(input('port: '))
#NOM = input(NOM: ')

IP = "192.168.56.1"
PORT = 5566
NOM= "Bob au pays des merveilles"
BUFFER_SIZE = 1024
ADRESSE = (IP, PORT)

CLIENT = socket(AF_INET, SOCK_STREAM)    # client socket object
CLIENT.connect(ADRESSE)	# Pour se connecter au socket du serveur socket grâce à l'adresse

public_key_2, private_key_2 = RSA.GENERATEUR_DE_CLE()
print("Cle privée personnelle client2", private_key_2)

message = str(public_key_2[0]) + '*' + str(public_key_2[1])
print("Cle publique personnelle (à send)", public_key_2)

CLIENT.send(bytes(message, "utf8"))
m = CLIENT.recv(BUFFER_SIZE).decode('utf8')
public_key_1 = [int(x) for x in m.split('*')]
print("cle publique recue", public_key_1)

recevoir_thread = Thread(target = recevoir)   # Thread créée pour pouvoir recevoir simultanément avec cette méthode
recevoir_thread.start() # démarre la tâche thread pour pouvoir recevoir les connexions 
tkinter.mainloop()  # Démarre l'interface graphique Tkinter.
