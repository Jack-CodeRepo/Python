# -*- coding: utf-8 -*-
# ==================================================================================================


# ==================================================================================================
#   IMPORT
# ==================================================================================================

# import framework GUI tkinter
import tkinter as tk
from tkinter import filedialog

# import module standard python
import configparser
import os
import random
import time


# import dictionnaire
from words import words_list

# import des éléments modifiables
import classes.elements.player
import classes.elements.mot
import classes.elements.lettre

# import des composants d'interface
import classes.interface.menu_bar
import classes.interface.bouton
import classes.interface.saisie
import classes.interface.display

# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================

# fichier de sauvegarde
save_file = "save_file.txt"
# fichier de conf
conf_file = "pendu.conf"

# ==================================================================================================
#   DICT
# ==================================================================================================


# ==================================================================================================
#   LISTS
# ==================================================================================================


# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

# fonctions liées au fichier pendu.conf

def modify_conf(section, option, value):
    """
        modifier la valeure d'une option du fichier pendu.conf

        :param section: section de l'option ex: [FILES]
        :type section: str
        :param option: option à modifier ex: save_file
        :type option: str
        :param value: valeur de l'option à modifier
        :type value: str
    """
    config = configparser.ConfigParser()
    config.read(conf_file)
    config.set(section, option, value)

    with open(conf_file, 'w') as configfile:
        config.write(configfile)



def get_config_element(section, option):
    """
        recupere la valeure d'une option du fichier pendu.conf

        :param section: section de l'option ex: [FILES]
        :type section: str
        :param option: option à modifier ex: save_file
        :type option: str
        :param value: valeur de l'option à modifier
        :type value: str
    """
    config = configparser.ConfigParser()
    config.read(conf_file)
    value = config.get(section, option)

    return value



# fonctions liées à l'interface autre que le menu
def add_player(name):
    """
        ajoute un joueur dans le fichier de sauvegarde

        :param name: nom du joueur à ajouter
        :type name: str
    """

    check_empty_file = os.stat(save_file).st_size == 0
    name = name
    if check_empty_file:
        with open(save_file, 'a') as fichier:
            fichier.write(f"{name}=10")

    if not check_empty_file:
        with open(save_file, 'a') as fichier:
                fichier.write(f"\n{name}=10")


def get_list_players():
    """
        recupere la liste des joueurs enregistré dans le fichier de sauvegarde

        :return: liste des joueurs
        :rtype: list
    """

    with open(save_file, 'r') as fichier:
        lignes = fichier.readlines()
        joueur = []
        for l in lignes:
            nom_joueur = l.split("=")
            joueur.append(nom_joueur[0])
    return joueur



def get_score_from_save(name):
    """
        récupere le score du joueur à partir du fichier de sauvegarde

        :param name: nom du joueur
        :type name: str
        :return: score du joueur
        :rtype: int
    """

    with open(save_file, 'r') as fichier:
        lignes = fichier.readlines()
        for l in lignes:
            nom_joueur = l.split("=")[0]
            score = l.split("=")[1]
            if name == nom_joueur:
                return score



def write_player_score(name, score):
    """
        ecris le score du joueur dans le fichier de sauvegarde

        :param name: nom du joueur
        :type name: str
        :param score: score du joueur a ecrire
        :type score: int
    """

    with open(save_file, 'w') as fichier:
        lignes = fichier.readlines()
        nb_lignes = len(lignes)
        for i in nb_lignes:
            index = i
            for l in lignes:
                nom_joueur = l.split("=")[0]
                score = l.split("=")[1]
                if name == nom_joueur:
                    lignes[index] = f"{nom_joueur}={score}"
                    fichier.writelines(lignes)



def hide_word(word):
    """
        remplace chaque charactere d'une sting par "_ "

        :param word: string à transformer
        :type word: str
        :return: string transformée
        :rtype: str
    """
    mot = []
    mot_long = len(word)
    for i in range(mot_long):
        mot.insert(i, "_")
    return mot



def pick_random_word(list_word):
    """
        choisi un mot aléatoire à partir d'une liste de string, et le renvois

        :param list_word: liste de mot
        :type list_word: list
        :return: list de mot
        :rtype: string
    """

    word = random.choice(list_word)
    return str(word)



def affichage(objet, liste):
    """
        affiche les éléments

        :param  objet: objet gérant l'endroit où afficher (l'objet doit etre créé avec la classe display)
        :type   objet: tkinter.Text
        :param  liste: liste des éléments à afficher
        :type   liste: list || autres
    """

    if type(liste) is list:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        for l in liste:
            objet.insert('1.0', l)
        objet.config(state=tk.DISABLED)

    else:
        objet.config(state=tk.NORMAL, font="Calibri")
        objet.delete('1.0', tk.END)
        objet.insert('1.0', liste)
        objet.config(state=tk.DISABLED)



# ==================================================================================================
#   CLASSES
# ==================================================================================================

class interface_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent

        self.player = classes.elements.player.class_player()
        self.mot = classes.elements.mot.class_mot(tentative=10)
        self.mot_cache = classes.elements.mot.class_mot()
        self.lettre = classes.elements.lettre.class_lettre()

        self.main_display = classes.interface.display.display(parent, 0, 0, 30, 10, 20).get_text()
        self.select_player_input = classes.interface.saisie.saisie(parent, 0, 1, 20, 10, "nom du joueur")
        self.pendu_play_button = classes.interface.bouton.bouton(parent, 1, 1, "jouer", self.pendu_game)


    def pendu_game(self):
        self.check_player()
        self.hide()
        self.lettre_button = classes.interface.bouton.bouton(self.parent, 2, 1, "valider lettre", self.get_letter)
        self.lettre_input = classes.interface.saisie.saisie(self.parent, 2, 2, 2, 1, "lettre")


    def get_letter(self):
        a = self.lettre_input.get_value()
        self.lettre.set_name(a)
        time.sleep(1)
        self.check_lettre()
       

    def check_player(self):
        a = self.select_player_input.get_value()
        self.player.set_name(str(a))
        nom_joueur = self.player.get_name()

        players = get_list_players()

        if a:
            nom_joueur = nom_joueur.upper()
            if players:
                if nom_joueur in players:
                    # si le joueur existe
                    for p in players:
                        if nom_joueur == p:
                            self.player.set_name(nom_joueur)
                            s = get_score_from_save(nom_joueur)
                            self.player.set_score(s)
                            string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                            affichage(self.main_display, string)
                else:
                    # si le joueur n'existe pas
                    self.player.set_name(nom_joueur)
                    self.player.set_score(10)
                    add_player(nom_joueur)
                    string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                    affichage(self.main_display, string)
            # si le fichier de sauvegarde est vide
            else:
                self.player.set_name(nom_joueur)
                self.player.set_score(10)
                add_player(nom_joueur) 
                string = f"joueur: {self.player.get_name()} // score: {self.player.get_score()}"
                affichage(self.main_display, string)
        else:
            string = "Renseignez un nom de joueur"
            affichage(self.main_display, string)




    def hide(self):
        mot = pick_random_word(words_list)
        self.mot.set_name(mot)
        a = hide_word(self.mot.get_name())
        affichage(self.main_display, a)



    def check_lettre(self):
        l = self.lettre.get_name()
        m = self.mot.get_name()
        mc = self.mot_cache.get_name()
        mc_list = []
        mc_display_list = []

        if not mc:
            mc = hide_word(m)

        for i in range(len(mc)):
                if l == m[i]:
                    mc_list.append(l)
                elif mc[i].isalpha():
                    mc_list.append(mc[i])
                else:
                    mc_list.append("_")

        if l not in m:
            self.mot.lower_tentative(1)

        mc = "".join(mc_list)
        self.mot_cache.set_name(mc)


        for i in mc:
            mc_display_list.append(i+" ")
        
        mc_display = "".join(mc_display_list)
        string = f"{mc_display} \n Tentatives restantes: {self.mot.get_tentative()}"
        affichage(self.main_display, string)
        


        
#
#   TO DO 
#   fonction du pendu
#







# ==================================================================================================
#   SCRIPT
# ==================================================================================================
root = tk.Tk()

save_file = get_config_element("FILES", "save_file")
menu = classes.interface.menu_bar.class_menu_bar()


root.title("Jeu du pendu")
root.config(menu=menu)

root.geometry("600x200")


interface_main(root)

root.mainloop()