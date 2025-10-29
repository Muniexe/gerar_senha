import tkinter as tk
from tkinter import messagebox
import string
import random

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho.")
        return

    maiusculas = var_maiusculas.get()
    minusculas = var_minusculas.get()
    numeros = var_numeros.get()
    simbolos = var_simbolos.get()

    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# --- Interface ---
root = tk.Tk()
root.title("Gerador de Senhas Seguras 🔐")
root.geometry("400x350")
root.resizable(False, False)

# Título
tk.Label(root, text="Gerador de Senhas Seguras", font=("Arial", 14, "bold")).pack(pady=10)

# Entrada de tamanho
frame_tamanho = tk.Frame(root)
frame_tamanho.pack(pady=5)
tk.Label(frame_tamanho, text="Tamanho da senha: ").pack(side=tk.LEFT)
entry_tamanho = tk.Entry(frame_tamanho, width=5)
entry_tamanho.insert(0, "12")
entry_tamanho.pack(side=tk.LEFT)

# Opções de caracteres
frame_opcoes = tk.LabelFrame(root, text="Opções de caracteres", padx=10, pady=10)
frame_opcoes.pack(pady=10, fill="x", padx=20)

var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(frame_opcoes, text="Letras maiúsculas (A-Z)", variable=var_maiusculas).pack(anchor="w")
tk.Checkbutton(frame_opcoes, text="Letras minúsculas (a-z)", variable=var_minusculas).pack(anchor="w")
tk.Checkbutton(frame_opcoes, text="Números (0-9)", variable=var_numeros).pack(anchor="w")
tk.Checkbutton(frame_opcoes, text="Símbolos (!@#$...)", variable=var_simbolos).pack(anchor="w")

# Botão de gerar
tk.Button(root, text="Gerar Senha", command=gerar_senha, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

# Campo de resultado
entry_resultado = tk.Entry(root, width=35, font=("Consolas", 12), justify="center")
entry_resultado.pack(pady=5)

# Botão copiar
tk.Button(root, text="Copiar", command=copiar_senha, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# Rodapé
tk.Label(root, text="Criado com ❤️ em Python", font=("Arial", 9), fg="gray").pack(side="bottom", pady=10)

root.mainloop()
#quem leu e gay