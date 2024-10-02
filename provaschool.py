import tkinter as tk
from tkinter import messagebox

# Função para verificar o login


def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    # Verifica as condições de e-mail e senha
    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
    elif len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 dígitos.")
    else:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")


# Criação da janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

# Rótulo para e-mail
label_email = tk.Label(janela, text="E-mail:")
label_email.pack(pady=5)

# Campo de entrada para e-mail
entry_email = tk.Entry(janela)
entry_email.pack(pady=5)

# Rótulo para senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

# Campo de entrada para senha (entrada escondida)
entry_senha = tk.Entry(janela, show='*')
entry_senha.pack(pady=5)

# Botão para realizar o login
botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
