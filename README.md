# Clg Badger

Clg-badger (pour College Badger) permet de faire l'appel automatiquement dans les salles de classe grâce à un lecteur de carte RFID sur une carte Arduino.

A chaque session (ie. chaque ouverture du programme), un registre des cartes badgées est créé.

En mode en ligne, l'application met en route un web service permettant un accès à distance à la feuille d'émargement.

# Pré-requis

Une carte Arduino avec un capteur RFID.

Python 3 avec les packages précisées dans `requirements.txt`. Pour installer les packages, lancer la commande suivante (sous Linux).

```bash
pip install -r requirements.txt
```

Sous Linux, accordez les permissions aux ports USB
```bash
sudo chmod a+rw /dev/ttyACM0
```

# Paramétrage

Le fichier `config.json` permet de configurer l'application :
- Mode local ou en ligne
- Langage de l'application
- Plein-écran ou non
- Identifiant de la salle de classe
- Chemin d'accès vers une base de données élèves (.csv) et vers un dossier comprenant des photos

Un fichier `locale.json` permet de traduire aisément l'application dans un nouveau langage.

# Fonctionnement de l'application

Chaque lancement de l'application crée un fichier `registry_DD-MM-YY_HH-MM-AM/PM`.

Chaque passage de badge est lu par la machine, puis enregistré dans le fichier `registry_DD-MM-YY_HH-MM-AM/PM`.


# Mode en ligne

## TODO

- Implémenter les informations correspondant à chaque service
- Chiffrer les retours de chaque service : seuls les comptes accrédités peuvent lire les informations
