import fileinput
import os
from tkinter import Tk, Button, Entry

class Patchwerk():

    def __init__(self, master):

        #GUI stuff
        self.master = master
        master.title("Patchwerk")

        vcmd = master.register(self.validate)
        self.barcode_field = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.barcode_field.pack()

        self.submit_button = Button(master, text="Submit", command=self.generateFile)
        self.submit_button.pack()

        #Script stuff
        self.barcode = None
        self.filenames = None

        #os.chdir('W:\Employees\Danny\dev\patchwerk')
        ##Add other work path here###
        os.chdir('/users/dwhite/patchwerk/patchwerk')
        ###

    def validate(self, new_text):
        if not new_text:
            self.barcode = None
            return True
        try:
            self.barcode = int(new_text)
            return True
        except ValueError:
            return False

    def generateFile(self):
        self.confirmTargetFiles()
        self.editFiles()

    def confirmTargetFiles(self):

        self.barcode = str(self.barcode)
        self.filenames = [self.barcode + "_SWP1.txt", self.barcode + "_SWP2.txt", self.barcode + "_SWP3.txt", self.barcode + "_SWP4.txt"]

        try:
            i = 0
            for fname in self.filenames:
                file = open(fname)
                file.close()
                i += 1
            if(i == 4):
                return 0
            else:
                return 1
        except IOError:
            print('Raw file not found for this barcode')
            return 1
        return 0

    def editFiles(self):
        output = self.barcode + "_backup"
        i = 1
        f = open(output, "w")
        for fname in self.filenames:
            for line in fileinput.input([fname], inplace=True, backup=""):
                if(i == 1):
                    line = line.replace("Plate", "Blank1")
                elif(i == 2):
                    line = line.replace("Plate", "Blank2")
                elif(i == 3):
                    line = line.replace("Plate", "Sample1")
                elif(i ==4):
                    line = line.replace("Plate", "Sample2")
                f.write(line)
            i += 1

root = Tk()
test = Patchwerk(root)
root.mainloop()
