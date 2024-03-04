import customtkinter as ctkn

ctkn.set_appearance_mode('dark')


janela = ctkn.CTk()
janela.geometry('500x400')
janela.title('APP calculo IMC')

# funcoes

def calcular():
    global resultado
    p = float(peso.get())
    a = float(altura.get())
    imc = p / (a ** 2)
    resultado.configure(text=f'{nome.get()},\nSeu IMC é: {imc:.2f}')

    if imc < 18.5:
        resultado.configure(text=f'{nome.get()},\nSeu IMC é: {imc:.2f} - Magreza')
    elif imc >= 18.5 and imc < 25:
        resultado.configure(text=f'{nome.get()}\nSeu IMC é: {imc:.2f} - Normal')
    elif imc >= 25 and imc < 30:
        resultado.configure(text=f'{nome.get()}\nSeu IMC é: {imc:.2f} - Acima da média')
    elif imc >= 30:
        resultado.configure(text=f'{nome.get()}\nSeu IMC é: {imc:.2f} - Obesidade')

texto = ctkn.CTkLabel(janela, text='APP calculo IMC', text_color='black', font=('verdana', 25, 'bold'))
texto.pack(padx=10, pady=10)

nome = ctkn.CTkEntry(janela, placeholder_text='digite seu nome', text_color='black', width=300, height=40, fg_color='white', placeholder_text_color='gray')
nome.pack(padx=10, pady=10)

peso = ctkn.CTkEntry(janela, placeholder_text='digite seu peso', text_color='black', width=300, height=40, fg_color='white', placeholder_text_color='gray')
peso.pack(padx=10, pady=10)

altura = ctkn.CTkEntry(janela, placeholder_text='digite sua altura', text_color='black', width=300, height=40, fg_color='white', placeholder_text_color='gray')
altura.pack(padx=10, pady=10)

botao = ctkn.CTkButton(janela, text='Calcular', font=('verdana', 20, 'bold'), fg_color='darkblue', height=50, command=calcular)
botao.pack(padx=10, pady=10)

resultado = ctkn.CTkLabel(janela, text='', text_color='darkred', font=('verdana',20,'bold'))
resultado.pack(padx=10, pady=10)

janela.mainloop()