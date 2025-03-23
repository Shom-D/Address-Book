import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class AddressBook:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Address Book")
        self.root.geometry("520x500")

        
        self.filepath = "info.csv"
        self.dataframe = pd.read_csv(self.filepath)

        self.f1 = tk.Frame(self.root)         
        self.f2 = tk.Frame(self.root, padx = 5)

        self.f1.grid(row = 0, column= 0)
        self.f2.grid(row = 0, column= 1, padx = 5)

        ttk.Label(self.f1, text = "Address Book", font = ("Calvetica", 17)).pack(pady=5, anchor="e")

        columns = list(self.dataframe.columns)
        self.tree = ttk.Treeview(self.f1, show = ("headings"), columns= columns[0])

        self.tree.heading("name", text = "Name")
        self.tree.column("name", width= 110, anchor= "center")
 
        

        for x in range(len(self.dataframe)):
            data = self.dataframe.iloc[x]
            self.tree.insert("", tk.END, values= data["name"])
            print(data["name"])

        self.tree.bind("<ButtonRelease-1>", self.clicked)
        
        self.tree.pack(padx = 5)

        ttk.Button(self.f1, text = "Update", command= self.update).pack(pady = 5)
        ttk.Button(self.f1, text = "Save", command= self.save).pack(pady= 5)
        

        button = ttk.Button(self.f2, command= self.open, text = "Open", padding= 5)
        button.grid(row = 0, column= 0 , padx= 5, pady= 5)
        self.entries: dict[str, ttk.Entry] = {}
       
        for x, col in enumerate(self.dataframe):

            ttk.Label(self.f2, text = col.capitalize() + ":", font= ("Calvetica" , 11)).grid(row = x+1, column= 0, pady = 4)
            self.entries[col] = ttk.Entry(self.f2 )
            self.entries[col].grid(row = x+1, column = 1, padx = 2)

        ttk.Button(self.f2, text = "Add/Update", command = self.add, padding = 5).grid(row = 100, column=1)
        

        self.root.mainloop()

    def add(self):

        data = {key: self.entries[key].get() if self.entries[key].get() else None for key in self.entries}
        

        idx = len(self.dataframe)
        self.dataframe.loc[idx] = data
        self.dataframe = self.dataframe.dropna()
        print(self.dataframe)

    def clicked(self, event):
        try:
            idx = self.tree.focus()

            item = self.tree.item(idx)["values"][0]
            row_index = self.dataframe[self.dataframe["name"]==item].index.tolist()[0]
            window = tk.Toplevel(self.root)

            self.edit = True
            self.index = row_index
            
            for col in self.dataframe.columns:
                ttk.Label(window, text = f"{col.capitalize()}: {self.dataframe.iloc[row_index][col]}").pack(pady = 5)
                self.entries[col].delete(0, tk.END)
                self.entries[col].insert(tk.END, self.dataframe.iloc[row_index][col])
        except:
            pass
        
        
        

    def update(self):
        if self.edit:
            item = self.tree.selection()[0]
            self.tree.item(item, values = self.entries["name"].get())

        data = {key: self.entries[key].get() if self.entries[key].get() else None for key in self.entries}

        self.dataframe.loc[self.index] = data

        
    def open(self):
        pass

    def save(self):
        self.dataframe.dropna()
        print(self.dataframe)
        self.dataframe.to_csv(self.filepath, index = False)

AddressBook()