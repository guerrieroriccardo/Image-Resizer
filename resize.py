import glob
import os
import sys
import argparse
from PIL import Image, ImageOps
import tkinter as tk
from tkinter.filedialog import askdirectory

argouments = sys.argv  # 1) width 2) height
filedirectory = ""


def main():
    tk.Tk().withdraw()

    parser = argparse.ArgumentParser(description="Bulk image size scaler")
    required_args = parser.add_argument_group("required argouments")
    required_args.add_argument('-w', type=int, help="width", required=True)
    required_args.add_argument('-l', type=int, help="height", required=False)
    args = parser.parse_args()

    setdirectory()
    modifyfile(args.w, args.l)


def getfile():
    filename = askdirectory()
    return filename


def setdirectory():
    global filedirectory
    filedirectory = getfile()  # get the directory
    if not os.path.exists(filedirectory + "/output/"):
        os.makedirs(filedirectory + "/output/")  # create the output directory


def modifyfile(width, height=0):
    # get every files in directory
    filedirectorys = glob.glob(filedirectory + "/*.png")

    if height == 0:
        size = [width, width]
    else:
        size = [width, height]

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


if __name__ == '__main__':
    main()
