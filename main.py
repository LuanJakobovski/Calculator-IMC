import customtkinter as ctk
import webbrowser

ctk.set_appearance_mode("light")

color0 = "#2C3E50"  # Azul Escuro
color1 = "#ECF0F1"  # Cinza Claro
color2 = "#3498DB"  # Azul
color3 = "#E5E8E8"  # Cinza Claro
color4 = "#16A085"  # Verde Água
color5 = "#95A5A6"  # Cinza

root = ctk.CTk()
root.title("Calculator IMC")
root.geometry('440x540')
root.configure(bg=color0)

# Separating frames
quadro_superior = ctk.CTkFrame(
    root, width=400, height=90, corner_radius=15,)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

quadro_inferior = ctk.CTkFrame(root, width=400, height=400, corner_radius=15)
quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

quadro_link = ctk.CTkFrame(root, width=230, height=30, corner_radius=15)
quadro_link.place(relx=0.5, rely=0.96, anchor="center")


# Function to calculate IMC
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get()) ** 2
    result = peso / altura

    if result < 18.5:
        l_texto_resultado.configure(text='Abaixo do peso')
        quadro_link.place_forget()
    elif result >= 18.5 and result <= 24.9:
        quadro_link.place_forget()
        l_texto_resultado.configure(text='Peso normal')
    elif result >= 25 and result <= 29.9:
        l_texto_resultado.configure(text='Sobre peso')
        quadro_link.place_forget()
    elif result >= 30 and result < 34.9:
        l_texto_resultado.configure(text='Obesidade grau 1')
        quadro_link.place(relx=0.5, rely=0.96, anchor="center")
        l_link.place(relx=0.5, rely=0.5, anchor="center")
    elif result >= 35 and result < 39.9:
        l_texto_resultado.configure(text='Obesidade grau 2')
        quadro_link.place(relx=0.5, rely=0.96, anchor="center")
        l_link.place(relx=0.5, rely=0.5, anchor="center")
    else:
        l_texto_resultado.configure(text='Obesidade grau 3')
        quadro_link.place(relx=0.5, rely=0.96, anchor="center")
        l_link.place(relx=0.5, rely=0.5, anchor="center")

    l_result.configure(text="IMC = {:.{}f}".format(result, 2))

# Function to open the link
def open_link():
    webbrowser.open("https://www.einstein.br/n/glossario-de-saude/obesidade")


# Configuring top label
name_app = ctk.CTkLabel(quadro_superior,
                        text='CALCULADORA IMC',
                        text_color='black',
                        font=('helvetica', 30, 'bold'), anchor="center")
name_app.place(x=0, y=25, relwidth=1)


# Configuring lower labels
l_peso = ctk.CTkLabel(quadro_inferior,
                      text='Informe seu peso (Kg)',
                      text_color=color0,
                      font=('helvetica', 14, 'bold'))
l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

l_altura = ctk.CTkLabel(quadro_inferior,
                        text='Informe sua altura (M)',
                        text_color=color0,
                        font=('helvetica', 14, 'bold'))
l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

l_link = ctk.CTkLabel(quadro_link, text="Saiba mais sobre obesidade aqui.",
                      text_color="blue", cursor="hand2", font=('roboto', 13, "underline"))
l_link.place(relx=0.5, rely=0.5, anchor="center")
l_link.bind("<Button-1>", lambda e: open_link())

l_result = ctk.CTkLabel(quadro_inferior,
                        text='---',
                        text_color=color0,
                        font=('helvetica', 32, 'bold'), anchor='center', corner_radius=12)
l_result.grid(row=2, column=0, columnspan=2, padx=30, pady=30)

l_texto_resultado = ctk.CTkLabel(quadro_inferior, text=None, text_color=color0,
                                 font=('helvetica', 16, 'bold'), anchor='center')
l_texto_resultado.grid(row=3, column=0, columnspan=2, padx=15, pady=15)


# Configuring Entrys
e_peso = ctk.CTkEntry(quadro_inferior, width=180, font=(
    'helvetica', 16), justify='center', corner_radius=12)
e_peso.grid(row=0, column=1, sticky='nw', padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width=180, font=(
    'helvetica', 16), justify='center', corner_radius=12)
e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)


# Button calculate
b_calcular = ctk.CTkButton(quadro_inferior, command=calcular, text='Calcular', width=180, height=50,
                           font=('helvetica', 30, 'bold'), anchor='center',
                           fg_color=color2, hover_color="#2980B9", corner_radius=12)
b_calcular.grid(row=4, column=0, padx=15, pady=15, columnspan=2)


# To hide
quadro_link.place_forget()
l_link.place_forget()

root.mainloop()