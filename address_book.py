import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd



class AddressBook:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Address Book")
        self.root.geometry("450x500")

        self.dataframe = pd.read_csv("info.csv")

        f1 = tk.Frame(self.root, 
                    #bg="#dfe8e8"
                    )
        f2 = tk.Frame(self.root, padx = 5)

        f1.grid(row = 0, column= 0)
        f2.grid(row = 0, column= 1, padx = 5)

        ttk.Label(f1, text = "Address Book", font = ("Calvetica", 17)).pack(pady=5, anchor="e")

        list = ttk.Treeview(f1, show = ("tree", "headings"))
        
        list.pack(padx = 5)

        button = ttk.Button(f2, command= self.open, text = "Open", padding= 5)
        button.grid(row = 0, column= 0 , padx= 5, pady= 5)

        for x, col in enumerate(self.dataframe):

            ttk.Label(f2, text = col.capitalize() + ":", font= ("Calvetica" , 11)).grid(row = x+1, column= 0, pady = 4)

            



    
        self.root.mainloop()
        
    def open(self):
        pass

AddressBook()