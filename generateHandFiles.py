import tkinter as tk
import os
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def editText(self, fileName, scale):
        if(not(scale.isnumeric()) or scale == '0'):
            scale = '1'

        # Read file
        importedFile = open(fileName, "r")              # open the file in reading mode
        lineList = list(importedFile)                   # turn each line into an element of a list
        lineList[0] = 'scale = ' + str(scale) + ';\n'   # change the first line (first element)in the list)
        importedFile.close()                            # close the file

        # Write file
        importedFile = open(fileName, "w")      # open the file in writing mode
        for line in lineList:                      # loop through each line (element in the list)
            importedFile.write(str(line))          # write the line (element of the list) to the file
        importedFile.close()                    # close the file

    def makePartFiles(self):
        filePath = os.path.dirname(os.path.abspath(__file__)) + "\SCADtoSTL.bat"
        #filePath = "c:\\Users\Jeff\PycharmProjects\Biomedical_Robotics\SCADtoSTL.bat"

        # Read edit field data =========================================================
        valThumb1 = self.efThumb1.get()
        valThumb2 = self.efThumb2.get()
        valIndex1 = self.efIndex1.get()
        valIndex2 = self.efIndex2.get()
        valIndex3 = self.efIndex3.get()
        valMiddle1 = self.efMiddle1.get()
        valMiddle2 = self.efMiddle2.get()
        valMiddle3 = self.efMiddle3.get()
        valRing1 = self.efRing1.get()
        valRing2 = self.efRing2.get()
        valRing3 = self.efRing3.get()

        # Make SCAD files ===============================================================
        self.editText('thumb1.scad', valThumb1)
        self.editText('thumb2.scad', valThumb2)
        self.editText('index1.scad', valIndex1)
        self.editText('index2.scad', valIndex2)
        self.editText('index3.scad', valIndex3)
        self.editText('middle1.scad', valMiddle1)
        self.editText('middle2.scad', valMiddle2)
        self.editText('middle3.scad', valMiddle3)
        self.editText('ring1.scad', valRing1)
        self.editText('ring2.scad', valRing2)
        self.editText('ring3.scad', valRing3)

        # Make STL files ================================================================
        # display some 'creating stl files dialogue'
        self.stSplash['text'] = 'Creating STL Files'
        self.update()

        # make the files
        p = subprocess.Popen(filePath)
        p.communicate()

        # remove 'creating stl files dialogue'
        self.stSplash['text'] = 'Prosthetic Hand STL Generator'
        self.update()

    def createWidgets(self):
        # Static Texts =======================================================================
        self.stSplash = tk.Label(self, text="Prosthetic Hand STL Generator", font=("Helvetica", 16))

        self.stthumb1 = tk.Label(self, text="Thumb 1 Length")
        self.stthumb2 = tk.Label(self, text="Thumb 2 Length")
        self.stindex1 = tk.Label(self, text="Index 1 Length")
        self.stindex2 = tk.Label(self, text="Index 2 Length")
        self.stindex3 = tk.Label(self, text="Index 3 Length")
        self.stmiddle1 = tk.Label(self, text="Middle 1 Length")
        self.stmiddle2 = tk.Label(self, text="Middle 2 Length")
        self.stmiddle3 = tk.Label(self, text="Middle 3 Length")
        self.string1 = tk.Label(self, text="Ring 1 Length")
        self.string2 = tk.Label(self, text="Ring 2 Length")
        self.string3 = tk.Label(self, text="Ring 3 Length")

        # Pushbuttons ========================================================================
        self.pbMakePartFiles = tk.Button(self, text="Generate STL", command=self.makePartFiles)
        self.pbQuit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

        # Edit Fields ========================================================================
        self.efThumb1 = tk.Entry(self)
        self.efThumb2 = tk.Entry(self)
        self.efIndex1 = tk.Entry(self)
        self.efIndex2 = tk.Entry(self)
        self.efIndex3 = tk.Entry(self)
        self.efMiddle1 = tk.Entry(self)
        self.efMiddle2 = tk.Entry(self)
        self.efMiddle3 = tk.Entry(self)
        self.efRing1 = tk.Entry(self)
        self.efRing2 = tk.Entry(self)
        self.efRing3 = tk.Entry(self)

        # Arrange Items ======================================================================
        self.stSplash.grid(row = 0, column = 0, columnspan = 2, sticky='E'+'W')

        self.pbMakePartFiles.grid(row = 1, column = 0, columnspan = 2, sticky='E'+'W')

        self.stthumb1.grid(row = 2, column = 0, sticky='E'+'W')
        self.stthumb2.grid(row = 3, column = 0, sticky='E'+'W')
        self.stindex1.grid(row = 4, column = 0, sticky='E'+'W')
        self.stindex2.grid(row = 5, column = 0, sticky='E'+'W')
        self.stindex3.grid(row = 6, column = 0, sticky='E'+'W')
        self.stmiddle1.grid(row = 7, column = 0, sticky='E'+'W')
        self.stmiddle2.grid(row = 8, column = 0, sticky='E'+'W')
        self.stmiddle3.grid(row = 9, column = 0, sticky='E'+'W')
        self.string1.grid(row = 10, column = 0, sticky='E'+'W')
        self.string2.grid(row = 11, column = 0, sticky='E'+'W')
        self.string3.grid(row = 12, column = 0, sticky='E'+'W')

        self.efThumb1.grid(row = 2, column = 1, sticky='E'+'W')
        self.efThumb2.grid(row = 3, column = 1, sticky='E'+'W')
        self.efIndex1.grid(row = 4, column = 1, sticky='E'+'W')
        self.efIndex2.grid(row = 5, column = 1, sticky='E'+'W')
        self.efIndex3.grid(row = 6, column = 1, sticky='E'+'W')
        self.efMiddle1.grid(row = 7, column = 1, sticky='E'+'W')
        self.efMiddle2.grid(row = 8, column = 1, sticky='E'+'W')
        self.efMiddle3.grid(row = 9, column = 1, sticky='E'+'W')
        self.efRing1.grid(row = 10, column = 1, sticky='E'+'W')
        self.efRing2.grid(row = 11, column = 1, sticky='E'+'W')
        self.efRing3.grid(row = 12, column = 1, sticky='E'+'W')

        self.pbQuit.grid(row = 13, column = 0, columnspan = 2, sticky='E'+'W')



root = tk.Tk()
root.title("Prosthetic Hand STL Generator")
root.iconbitmap('BRicon.ico')
app = Application(master=root)
app.mainloop()
