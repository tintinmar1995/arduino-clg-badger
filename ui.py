import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import json

# La partie suivante traite de la fenêtre badgeuse

def refresh(registry_name, prenom, nom, panel):
    global badger_window

    try :
        with open(registry_name, "r+") as file :
            line = ""
            for line in file:
                pass
            if line != "" :
                line = line.split(",")
                eleve = data_eleve[data_eleve.id_eleve == int(line[0])]
                prenom.set(list(eleve.prenom)[0].upper())
                nom.set(list(eleve.nom)[0].upper())
                img = ImageTk.PhotoImage(Image.open(config["path_pictures"]+str(line[0])+".jpg").resize((250,250)))
                panel.configure(image=img)
                panel.image = img
                first = true
    except :
        pass

    badger_window.after(50, refresh, registry_name, prenom, nom, panel)

def badger():
    global init
    global registry_name
    global badger_window
    init.destroy()

    badger_window = tk.Tk()

    if config["fullscreen"] :
        badger_window.attributes("-fullscreen", True)
    else :
        badger_window.geometry("800x600")
    badger_window.title(locale["badger_title"][config["lang"]])

    prenom = tk.StringVar()
    prenom.set("")

    nom = tk.StringVar()
    nom.set("")

    # frame 1
    frame_l = tk.Frame(badger_window, borderwidth=2, relief=tk.GROOVE)
    frame_l.pack(side=tk.LEFT, padx=30, pady=30)

    # frame 2
    frame_r = tk.Frame(badger_window, borderwidth=2, relief=tk.GROOVE)
    frame_r.pack(side=tk.LEFT, padx=10, pady=10)

    tk.Label(frame_r, textvariable=prenom, font=("Helvetica", 25)).grid(row = 1, column = 1)
    tk.Label(frame_r, textvariable=nom, font=("Helvetica", 25)).grid(row = 1, column = 3)
    photo_elv = ImageTk.PhotoImage(Image.open("assets/refresh.png").resize((250,250), Image.ANTIALIAS))
    panel=tk.Label(frame_l, image = photo_elv)
    panel.grid(row = 1, column = 1)

    badger_window.after(0, refresh, registry_name, prenom, nom, panel)
    badger_window.mainloop()

# La partie suivante traite de la fenêtre de démarrage

def Start(input_registry_name, input_config):
    global init
    global data_eleve
    global registry_name
    global config
    global locale

    # Set registry name and config as global variable
    # Global varaible can be used in every function of the script
    registry_name = input_registry_name
    config = input_config

    # Open languages
    with open('locale.json') as f:
        locale = json.load(f)

    init = tk.Tk()
    if config["fullscreen"] :
        init.attributes("-fullscreen", True)
    else :
        init.geometry("800x600")
    init.title(locale["start_title"][config["lang"]])

    Frame1 = tk.Frame(init, borderwidth=2)
    photo_clg = ImageTk.PhotoImage(Image.open("assets/clg.jpg").resize((500,250), Image.ANTIALIAS))
    panel = tk.Label(Frame1, image = photo_clg)
    panel.pack()
    Frame1.pack(padx=30, pady=30)

    Frame2 = tk.Frame(init, borderwidth=2)

    height = 5
    width = 2
    label = locale["labels_params"][config["lang"]]
    index = ["id_room", "online", "lang", "path_student", "path_pictures"]
    config_text = ""
    for i in range(len(label)):
        config_text += label[i] + " : " + str(config[index[i]]) + "\n"
    tk.Label(Frame1, text=config_text).pack()
    Frame2.pack()

    tk.Button(init, text =locale["button_viewer"][config["lang"]], command=badger).pack(side=tk.RIGHT, padx=5, pady=10)

    try :
        data_eleve = pd.read_csv(config["path_student"])
    except:
        showerror(locale["error"][config["lang"]], locale["error_student_db_not_found"][config["lang"]])

    init.mainloop()
