##  Verifique que  tiene instalado el pip con pip -V
# Instale tk
# pip install tk

## Llamando a la libreria
import tkinter as tk

## Haciendo un Hello World

root = tk.Tk()
label = tk.Label(root,
                 text ='Hello World',
                 padx=40,
                 pady=40)

label.pack()
root.mainloop()