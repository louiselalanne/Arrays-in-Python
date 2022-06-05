from tkinter import *
from array import *

root=Tk()
root.title("Multidimensional Arrays")
root.geometry("500x500")
root.config(bg="#9D98FF")

label = Label(root, fg="#65FE54", bg="#9D98FF", font="Arial 12 bold")

array_1d = ["Mingau", "Thomas", "Matheus"]
array_2d = [["Mingau", "dormir"], ["Thomas", "ciências"], ["Matheus", "criminologia"]]
array_3d = [[["Mingau", "dormir", "excelente"], ["Thomas", "ciências", "muito bom"], ["Matheus", "criminologia", "indo bem"]]]

def relatorio():
    label["text"] = array_3d[0][2][0] + " na matéria " + array_3d[0][2][1] + " está " + array_3d[0][2][2] + "!"

btn= Button(root, text="Mostrar relatório", command = relatorio)

btn.place(relx=0.5,rely=0.5, anchor=CENTER)
label.place(relx=0.5,rely=0.6, anchor=CENTER)

root.mainloop()
