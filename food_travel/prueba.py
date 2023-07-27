# import tkinter
# import customtkinter

# root_tk= tkinter.Tk()
# root_tk.geometry("400x240")
# root_tk.title("hola mundo")

# def boton_funcion():
#     print("apretar boton")

# boton=customtkinter.CTkButton(master= root_tk, corner_radius=10, command=boton_funcion)
# boton.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
# root_tk.mainloop()

viajes = []
for lugar in ['playa', 'montaña', 'ciudad', 'campo', 'extranjero']:
    cant_viajes = int(input(f"Ingrese la cantidad de viajes a {lugar}: "))
    viajes.append(cant_viajes)
print(viajes)