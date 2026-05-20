import tkinter as Tk
from database.schema import create_tables
from views.main_window import MainWindow
def main():
    create_tables()

    root=Tk.Tk()
    root.title("REVO_LUTION Paie-Bordereau CNSS")
    root.geometry("900x600")

    MainWindow(root)


    root.mainloop()

if __name__== "__main__":
    main()