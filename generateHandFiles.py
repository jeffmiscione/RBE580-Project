import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def makePartFiles(self):
        filepath = "c:\\Users\Jeff\PycharmProjects\Biomedical_Robotics\SCADtoSTL.bat"

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
        # read generic thumb1.scad
        # edit generic thumb1.scad
        # write new file for thumb1.scad
        # ===============================================================================

        # Make STL files
        p = subprocess.Popen(filepath)
        p.communicate()

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