# Clg Badger

Clg-badger permet de faire l'appel automatiquement grâce à un lecteur de carte RFID et une carte Arduino. 

# Pré-requis

Python 3 avec :
- **TkInter** python3-tk
- **Pillow Tk** python3-pil.imagetk
- **Pandas**
- **Pillow**

Une carte Arduino avec un capteur RFID.

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

# Fonctionnement de l'application

Chaque lancement de l'application crée un fichier `registry_25-11-19_16-33-PM`.

Chaque passage de badge est lu par la machine, puis enregistré dans le fichier `registry_25-11-19_16-33-PM`.

Le mode en ligne permettra d'appeler une API à chaque badge scanné pour centraliser dans une base de données le registre de présence dans une salle.