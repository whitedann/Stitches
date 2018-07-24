import os
import fileinput

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
        i = 0
        for fname in self.filenames:
            file = open(fname, "r+")
            file.write("Hello")
            for line in file:
                print(line)
    

test = Patchwerk("2581707")
test.confirmTargetFiles()
test.editFiles()
        
        
            
            
        
        
