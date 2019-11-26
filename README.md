# Clg Badger

Clg-badger (pour College Badger) permet de faire l'appel automatiquement dans les salles de classe grâce à un lecteur de carte RFID sur une carte Arduino.

Le programme fonctionne, pour le moment, uniquement mode hors ligne. A chaque session (ie. chaque ouverture du programme), un registre des cartes badgées est créé.

Il s'agirait dans le futur de concevoir un service web Python (avec Flask) pour réceptionner et stocker chaque présence.

# Pré-requis

Une carte Arduino avec un capteur RFID.

Python 3 avec :
- **PySerial** pour écouter le port Serie communiquant avec Arduino
- **TkInter** `python3-tk`, pour l'interface locale (UI)
- **Pillow Tk** python3-pil.imagetk, pour afficher des images dans l'UI
- **Pillow** idem
- **Pandas** pour manipuler la base de données élèves (contenant les associations Nom-Prénom <-> Identifiant)

Sous Linux, accordez les permissions aux ports USB
```bash
sudo chmod a+rw /dev/ttyACM0
```

# Paramétrage

Le fichier `config.json` permet de configurer l'application :
- Mode local ou en ligne (non implémenté encore)
- Langage de l'application
- Plein-écran ou non
- Identifiant de la salle de classe
- Chemin d'accès vers une base de données élèves (.csv) et vers un dossier comprenant des photos

Un fichier `locale.json` permet de traduire aisément l'application dans un nouveau langage.

# Fonctionnement de l'application

Chaque lancement de l'application crée un fichier `registry_DD-MM-YY_HH-MM-AM/PM`.

Chaque passage de badge est lu par la machine, puis enregistré dans le fichier `registry_DD-MM-YY_HH-MM-AM/PM`.

Le mode en ligne permettra d'appeler une API à chaque badge scanné pour centraliser dans une base de données le registre de présence dans une salle.

# Prochaines étapes

## Envoi par mail du registre


## Connexion à un service web pour centraliser les informations dans le collège

Permettre un appel à une API à chaque scan :
- Réaliser une requête HTTP GET pour obtenir une clé de chiffrement asymétrique
- Chiffrer le numéro de la carte + numéro de salle + un sel
- Réaliser une requête HTTP POST pour envoyer le numéro de carte chiffré à l'API

L'API en question devra être gardienne d'une base de données, et être capable de déchiffrer puis d'insérer la carte dans la base de données.
