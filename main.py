from pytube import YouTube
import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import *
from tkinter.filedialog import *
import sys

print("BIENVENUE SUR YooLink, LOGICIEL GRATUIT ET SIMPLE POUR TELECHARGER DES VIDEOS YOUTUBE !\n"
      "ATTENTION A LIRE ATTENTIVEMENT POUR BIEN COMPRENDRE COMMENT YooLink FONCTIONNE\n"
      "1) COPIER LE LIEN YOUTUBE GRACE A LA FONCTION PARTAGER\n"
      "2) COLLER LE LIEN DANS L'ENTREE YooLink\n"
      "3) CLIQUER SUR LE BOUTON PARCOURIR POUR SELECTIONNER UN DOSSIER OU LES VIDEOS VONT ETRE STOCKEES\n"
      "4) CLIQUER SUR LE BOUTON GET POUR LANCER LE TELECHARGEMENT\n")

class Window:
    def __init__(self, root):
        root.title("YooLink")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Boutons
        Titre = tk.Label(text="Bienvenue sur YooLink")
        Bouton = tk.Button(root)
        Bouton["bg"] = "pink"
        ft = tkFont.Font(family='Times', size=10)
        Bouton["font"] = ft
        Bouton["fg"] = "#000000"
        Bouton["justify"] = "center"
        Bouton["text"] = "Get"
        Bouton.place(x=270, y=290, width=70, height=25)
        Bouton["command"] = self.Bouton_command
        Bouton['height'] = 35
        Bouton3 = tk.Button(root)
        Bouton3['command'] = self.askFiles
        Bouton3['bg'] = "yellow"
        Bouton3.place(x=360, y=290, width=70, height=25)
        Bouton3['text'] = "Parcourir"
        ft = tkFont.Font(family='Times', size=10)
        Bouton3["font"] = ft
        Bouton3["fg"] = "#000000"
        Bouton3["justify"] = "center"
        BoutonClear = tk.Button(root)
        BoutonClear['bg'] = "brown"
        BoutonClear["command"] = self.clear_text
        BoutonClear["text"] = "Delete"
        BoutonClear['font'] = ft
        BoutonClear.place(x=180, y=290, width=70, height=25)

        #photo
        photo = tk.PhotoImage(file="image.png")

        # Labels
        self.Label = tk.Entry(root)
        self.Label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.Label["font"] = ft
        self.Label["fg"] = "#333333"
        self.Label["justify"] = "left"
        self.Label["text"] = ""
        self.Label.place(x=190, y=200, width=226, height=30)

    def Bouton_command(self):
        name = "videos"
        isExist = os.path.exists(self.chemin + f"/{name}")
        if isExist == True:
            print("Le fichier existe déja")
            os.chdir(self.chemin + f"/{name}")
        else:
            os.mkdir(name)
            os.chdir(self.chemin)
        download_input = self.Label.get()
        link_download = YouTube(download_input)
        link_download.streams.filter(file_extension="mp4")
        stream = link_download.streams.get_by_resolution("360p")
        stream.download()
        return "Succès"

    def askFiles(self):
        filepath = askdirectory(title="Selectionner un repertoire")
        self.chemin = filepath.title()

    def alert(self):
        showinfo("Alert!!!")
    def clear_text(self):
        self.Label.delete(0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()