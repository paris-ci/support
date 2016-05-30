# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
support -- support.py
MODULE DESC 
"""
# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import sys
import locale


try:
    from dialog import Dialog
except ImportError:
    print("Vous n'avez pas décompréssé l'archive correctement : pythonDialog n'a pas été trouvé :(")
    sys.exit(1)

def main():
    locale.setlocale(locale.LC_ALL, '')
    d = Dialog(dialog="dialog")
    d.set_background_title("Programme de support express")
    d.msgbox("Bienvenue sur le programme de support technique. Celui-ci vous guidera pour résoudre votre probleme ou la soumettre de maniere correcte !")
    code, tag = d.menu("Quel est le programme concerné par le probleme ?:",
                       choices=[("1", "Mon serveur en entier, le soucis est global, ou n'est pas lié à un programme particulier."),
                                ("2", "Mon site web (apache2, nginx, ioncube...)"),
                                ("3", "Un serveur de jeu Minecraft"),
                                ("4", "Un serveur de jeu CS:GO, TF2, ou autre jeu source"),
                                ("5", "Un VPN OpenVpn"),
                                ("6", "Le SSHd (connexion au serveur avec PuTTy ou équivalent)"),
                                ("7", "Une base de donnée (MySql, phpmyadmin...)"),
                                ("8", "Autre chose, qui n'est pas expliqué ici"),
                                ])
    if code == d.OK:
        pass


if __name__ == '__main__':
    main()
