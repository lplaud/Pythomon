import tkinter as tk
from _csv import writer

from createPythomons import createpythomons
import random
import time
from PIL import Image
from PIL import ImageTk
import csv

# Create and test pythomon objects and dictionary
pythomonPackage = createpythomons()
pythomonsList = pythomonPackage.pythomonslist
pythomonsObjects = pythomonPackage.pythomonobjects

for pythomon in pythomonsList:
    print(pythomon)
print(pythomonsObjects)
#################################################

# Encompassing method for pokemon selection and display ################################################################
global CORRECT #Needed for dex + Capture reasons
global WINS
global LOSSES
CORRECT = 0
WINS = 0
LOSSES = 0

def getrandommon():

    # Get the random encounter pokemon #################################################
    chosenID = random.randint(0, 807)
    chosenMons = []
    print("ChosenID = " + str(chosenID))
    for pythomon in pythomonsObjects:
        if int(pythomon.idnum) == chosenID:
            chosenMons.append(pythomon)
    chosenForm = random.randint(0, len(chosenMons)-1)
    chosenMon = chosenMons[chosenForm]

    if chosenMon.name.lower() in chosenMon.form.lower():
        appeared = "A wild " + str(chosenMon.form) + " appeared!"
        print(appeared)
        nameType = 1
    elif chosenMon.form != " ":
        appeared = "A wild " + str(chosenMon.form) + " " + chosenMon.name + " appeared!"
        print(appeared)
        nameType = 2
    else:
        appeared = "A wild " + chosenMon.name + " appeared!"
        print(appeared)
        nameType = 3
    #######################################################################################

    # Image Grabbing ONLY VIA ID NUM ATM, FORMS NOT INCORPORATED##################################
    fixedID = chosenMon.idnum
    if nameType == 1:
        if "mega" in chosenMon.form.lower():
            fixedID = chosenMon.idnum + "-Mega"
        elif "galarian" in chosenMon.form.lower():
            fixedID = chosenMon.idnum + "-Galar"
        elif "alolan" in chosenMon.form.lower():
            fixedID = chosenMon.idnum + "-Alola"
        else:
            fixedID = chosenMon.idnum + chosenMon.form

    if int(chosenMon.idnum) < 10:
        path = "C:/Users/lplau/PycharmProjects/pythomon/images/" + "00" + fixedID + '.png'
    elif int(chosenMon.idnum) < 100:
        path = "C:/Users/lplau/PycharmProjects/pythomon/images/" + "0" + fixedID + '.png'
    else:
        path = "C:/Users/lplau/PycharmProjects/pythomon/images/" + fixedID + '.png'
    #############################################################################################

    # Tkinter setup######################
    root = tk.Tk()
    root.geometry("400x400")

    for i in range(3):
        root.columnconfigure(i, weight=1)
    root.rowconfigure(1, weight=1)
    #####################################

    # Canvas where image will be placed ###############
    canvas = tk.Canvas(root, width=300, height=300)
    global WINS, LOSSES
    tk.Label(root, text="Wins: " + str(WINS) + " Losses: " + str(LOSSES)).grid(row=0, column=1)
    canvas.grid(row=1, column=1)
    ####################################################

    # resize the image with width and height of root ####
    image = Image.open(path)
    resized = image.resize((300, 300), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
    ####################################################

    # Entry Box ################
    entry = tk.Entry(root)
    entry.grid(row=2, column=1)
    ############################

    # Method for checking the validity of name entry ######################################
    def correctcheck():
        global CORRECT
        name = entry.get()
        match nameType:
            case 1:
                if name.lower() == chosenMon.form.lower():
                    CORRECT = 1
                    root.destroy()
                else:
                    CORRECT = 0
                    root.destroy()

            case 2:
                if name.lower() == chosenMon.form.lower() + " " + chosenMon.name.lower():
                    CORRECT = 1
                    root.destroy()
                else:
                    CORRECT = 0
                    root.destroy()
            case 3:
                if name.lower() == chosenMon.name.lower():
                    CORRECT = 1
                    root.destroy()
                else:
                    CORRECT = 0
                    root.destroy()
    ###########################################################################################

    # Submission button, calls the previous method #########################################
    button1 = tk.Button(text='Submit', command=correctcheck, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold')).grid(row=3, column=1)
    canvas.create_window(100, 100, window=button1)
    #########################################################################################

    root.mainloop()
    return chosenMon
########################################################################################################################

def addtodex(chosenMon):
    print("Pog")
    stats = [chosenMon.idnum, chosenMon.name, chosenMon.form, chosenMon.type, chosenMon.type2, chosenMon.total, chosenMon.hp,
             chosenMon.atk, chosenMon.defn, chosenMon.spatk, chosenMon.spdef, chosenMon.spd, chosenMon.gen]
    with open('dex.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(stats)
        f_object.close()

starttime = time.time()
while True:
    chosenMon = getrandommon()
    if CORRECT == 1:
        WINS += 1
        addtodex(chosenMon)
    else:
        LOSSES += 1
        print("Dog")

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
