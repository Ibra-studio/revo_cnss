import tkinter as Tk
from database.schema import create_tables

def main():
    create_tables()

    root=Tk.Tk()
    root.title("REVO_LUTION Paie-Bordereau CNSS")
    root.geometry("900x600")

    root.mainloop()

if __name__== "__main__":
    main()