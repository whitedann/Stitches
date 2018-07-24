import os
import fileinput
import sys

class Patchwerk:

    def __init__(self, barcode):
        self.barcode = barcode
        self.filenames = [self.barcode + "_SWP1.txt", self.barcode + "_SWP2.txt",
                     self.barcode + "_SWP3.txt", self.barcode + "_SWP4.txt"]
        os.chdir('W:\Employees\Danny\dev\patchwerk')
        ##Add other work path here###

        ###

    def confirmTargetFiles(self):
        try:
            i = 0
            for fname in self.filenames:
                file = open(fname)
                file.close()
                i += 1
            if(i == 4):
                return 0;
            else:
                return 1;
        except IOError:
            print('Raw file not found for this barcode')
            return 1;
        return 0;

    def editFiles(self):
        i = 1
        for fname in self.filenames:
            for line in fileinput.input([fname], inplace=True):
                if(i == 1):
                    line = line.replace("Plate", "Blank1")
                elif(i == 2):
                    line = line.replace("Plate", "Blank2")
                elif(i == 3):
                    line = line.replace("Plate", "Sameple1")
                elif(i ==4):
                    line = line.replace("Plate", "Sample2")
                sys.stdout.write(line)
            i += 1
                
    

test = Patchwerk("2581712")
test.confirmTargetFiles()
test.editFiles()
        
        
            
            
        
        
