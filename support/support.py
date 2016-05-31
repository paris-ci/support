# coding: utf8
#!/usr/bin/env python2.7
"""
support -- support.py
MODULE DESC 
"""
# Constants #
from __future__ import unicode_literals

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


import sys
import locale


try:
    # noinspection PyUnresolvedReferences
    from dialog import Dialog
    from dialog import DialogError
except ImportError:
    print("Vous n'avez pas décompréssé l'archive correctement : pythonDialog n'a pas été trouvé :(")
    sys.exit(100)

def propositionsMessages(d, programme):
    d.msgbox("Bon, passons aux choses serieuses...")
    if programme == "serveur":
        if d.yesno("Es-ce que le message parle de permission refusée (permission denied)", yes_label="Oui !", no_label="Non :(") == d.OK:
            if d.yesno("Super ! Ce message apparait-il quand vous essayez de lancer un programme", yes_label="Oui !", no_label="Non :(")== d.OK:
                d.msgbox("La solution est toute trouvée : il faut rendre le programme éxécutable avec la commande chmod +x monprogramme, ou le lancer avec l'interpréteur adéquat (exemple, pour un programme python : python monprogramme.py)")




def main():
    locale.setlocale(locale.LC_ALL, '')
    d = Dialog(dialog="dialog", autowidgetsize=True)
    d.set_background_title("Programme de support express")
    d.msgbox("Bienvenue sur le programme de support technique. Celui-ci vous guidera pour résoudre votre probleme ou la soumettre de maniere correcte !")
    code, programme = d.menu("Quel est le programme concerné par le probleme ?:",
                       choices=[("serveur", "Mon serveur en entier, le soucis est global, ou n'est pas lié à un programme particulier."),
                                ("web", "Mon site web (apache2, nginx, ioncube...)"),
                                ("minecraft", "Un serveur de jeu Minecraft"),
                                ("source", "Un serveur de jeu CS:GO, TF2, ou autre jeu source"),
                                ("vpn", "Un VPN OpenVpn"),
                                ("ssh", "Le SSHd (connexion au serveur avec PuTTy ou équivalent)"),
                                ("bdd", "Une base de données (MySql, phpmyadmin...)"),
                                ("autre", "Autre chose, qui n'est pas expliqué ici")
                                ])

    if code == d.OK:
        if d.yesno("Le principal, avez vous lu les logs de l'application ou du service ?", yes_label="Bien sur que oui !", no_label="Euh... On peut le faire maintenent ?") == d.OK:
            if d.yesno("Et vous n'avez rien trouvé dedans?", yes_label="Sisi, j'ai vu des erreurs", no_label="Vraiment rien trouvé!") == d.OK:
                if programme == "minecraft":
                    if d.yesno("Hum... S'agit t'il d'un trés long message avec des at à quasiment chaque ligne ?", yes_label="Oui, c'est ca !", no_label="Non !") == d.OK:
                        d.msgbox("C'est une stacktrace. Il doit y avoir le nom d'un ou plusieurs plugins dedans, ainsi que leur version. Essaye de les mettre à jour.")
                        if d.yesno("La mise à jour et le redémarrage ont-ils résolu le probleme ?", yes_label="Oui, merci !", no_label="Non :'(") == d.OK:
                            d.msgbox("Dans, ce cas, merci à toi ! :)")
                            sys.exit(0)
                        else:
                            propositionsMessages(d, programme)
                    else:
                        d.msgbox("Pas grave, nous allons trouver, alors dit moi :")

                code, tag = d.menu("Quel genre de messages ?:",
                                   choices=[("1", "Des messages d'erreurs"),
                                            ("2", "Des \"Warnings\""),
                                            ("3", "Des messsages que j'ai pas trop compris")
                                            ])
                tag = int(tag)
                if code == d.OK:
                    if tag == 1:
                        d.msgbox("Super ! La plupart du boulot est fait ! Essayez d'entrer dans google le message d'erreur en retirant la date, l'heure, les chemins de fichiers et tout autre signe distinctif, puis appliquez les solutions proposées")
                        if d.yesno("Cela à résolu votre probleme ?", yes_label="Oui, merci beaucoup !", no_label="Malheureusement non !") == d.OK:
                            d.msgbox("Dans, ce cas, merci à toi ! :)")
                            sys.exit(0)
                        else:
                            propositionsMessages(d, programme)
                    elif tag == 2:
                        if d.yesno("Le mieux serait d'entrer ces messages sans trop de signes distinctifs dans google et d'essayer les solutions proposées. Est-ce que cela résout le problème ?", yes_label="Oui, merci beaucoup !", no_label="Malheureusement non !") == d.OK:
                            d.msgbox("Dans, ce cas, merci à toi ! :)")
                            sys.exit(0)
                        else:
                            propositionsMessages(d, programme)
                    elif tag == 3:
                        d.msgbox("Essayez d'entrer dans google le message en retirant la date, l'heure, les chemins de fichiers et tout autre signe distinctif, puis appliquez les solutions proposées")
                        if d.yesno("Cela à résolu votre probleme ?", yes_label="Oui, merci beaucoup !", no_label="Malheureusement non !") == d.OK:
                            d.msgbox("Dans, ce cas, merci à toi ! :)")
                            sys.exit(0)
                        else:
                            propositionsMessages(d, programme)
            else:
                d.msgbox("Si tu ne trouves pas de message particulier, cherche si l'application n'a pas d'autres fichiers de logs. Si ce n'est pas le cas, passe nous voir au support sur IRC")
        else:
            d.msgbox("Pas de soucis, regardons. Tu dois chercher des lignes contenant des erreurs")
            if d.yesno("Connais-tu le chemin vers ces logs ? Je ne connais que ceux par défault, et si tes serveurs sont installés a d'autres endroits, je ne les trouverai pas.", yes_label="Oui, je connais!", no_label="Malheureusement non !") != d.OK:
                d.msgbox("Voici les logs, si je les trouves...")
                try:
                    if programme == "serveur":
                        d.textbox("/var/log/syslog")
                    elif programme == "web":
                        d.textbox("/var/log/apache2/error.log")
                    elif programme == "minecraft":
                        code, serv = d.inputbox("Quel est le nom du serveur aprés /home/minecraft ? (tapez juste / si il n'y en a pas)", init="/")
                        d.textbox("/home/minecraft/" + serv + "/logs/latest.log")
                    elif programme == "source":
                        d.msgbox("Les logs pour les serveurs source sont dans la console seulement")
                    elif programme == "vpn":
                        d.textbox("/var/log/syslog") # oui, ca log dans syslog openvpn :o
                    elif programme == "sshd":
                        d.textbox("/var/log/auth.log")
                        d.textbox("/var/log/messages")
                    elif programme == "bdd":
                        d.textbox("/var/log/mysql.log")
                    else:
                        d.msgbox("Le mieux serait de chercher ce chemin sur google...")
                        code, logs = d.inputbox("Quel est ce chemin ?", init="/var/log/[...]")
                        if code == d.OK:
                            d.textbox(logs)
                        else:
                            d.msgbox("Au revoir è_é!")
                            sys.exit(2)
                except DialogError:
                    d.msgbox("Je n'ai pas trouvé le fichier :'(. Le mieux serait de chercher ce chemin sur google...")
                    code, logs = d.inputbox("Quel est ce chemin ?", init="/var/log/[...]")
                    if code == d.OK:
                        d.textbox(logs)
                    else:
                        d.msgbox("Au revoir è_é!")
                        sys.exit(2)
            else:
                code, logs = d.inputbox("Quel est ce chemin ?", init="/var/log/[...]")
                if code == d.OK:
                    d.textbox(logs)
                else:
                    d.msgbox("Au revoir è_é!")
                    sys.exit(2)
            d.msgbox("Avec les logs, tu devrais pouvoir résoudre pas mal de problémes, essaye de googler chaque message que tu ne comprends pas... Si ca ne suffit pas, relance le programme")
            sys.exit(0)



    else:
        d.msgbox("Au revoir è_é!")


if __name__ == '__main__':
    main()
