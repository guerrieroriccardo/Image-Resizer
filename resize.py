import glob
import os
import sys
from PIL import Image, ImageOps
import tkinter as tk
from tkinter.filedialog import askdirectory

argouments = sys.argv  # 1) width 2) height
filedirectory = ""


def main():
    tk.Tk().withdraw()
    print(argouments)
    setdirectory()
    modifyfile()


def getfile():
    filename = askdirectory()
    return filename


def setdirectory():
    global filedirectory
    filedirectory = getfile()  # get the directory
    if not os.path.exists(filedirectory + "/output/"):
        os.makedirs(filedirectory + "/output/")  # create the output directory


def modifyfile():
    # get every files in directory
    filedirectorys = glob.glob(filedirectory + "/*.png")

    size = [int(argouments[1]), int(argouments[2])]

    i = 1
    for file in filedirectorys:
        name = file.split("\\")[1]
        immagine = Image.open(file)
        #immagine.resize((500, 600), Image.ANTIALIAS)
        immagine = ImageOps.fit(immagine, size, Image.ANTIALIAS)
        immagine.save(filedirectory + "/output/" +
                      name, optimize=True, quality=100)
        completed = int(100/len(filedirectorys)*i)
        print("Completed: " + str(completed) + "%")
        i += 1


main()
