# imports
from tkinter import *

# import functions/methods
from actions import *

# interfaz grafica
root = Tk()
root.title("Archivos")
root.geometry("900x600")

def btn_nueva_ventana():
  mainFrame = Frame(root)
  mainFrame.grid(row=1, column=0, padx=10, pady=2)
  mainPanel = MyMainPanel(root, mainFrame)
  abrir.destroy()

abrir = Button(root, text="Abrir", command=btn_nueva_ventana)
abrir.place(relx=0.5, rely=0.5, anchor='center')

# execute main()
if __name__ == "__main__":
  main()

# tkinter mainloop
root.mainloop()