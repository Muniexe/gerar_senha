import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

# === Funções ===
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
    entry_resultado.configure(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)
    entry_resultado.configure(state="readonly")

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# === Interface ===
root = tk.Tk()
root.title("🔒 Gerador de Senhas Seguras")
root.geometry("420x430")
root.resizable(False, False)

COR_FUNDO = "#000000"      
COR_TEXTO = "#FFFFFF"      
COR_BOTAO = "#1E90FF"      
COR_BOTAO2 = "#00C853"    
COR_CAIXA = "#111111"      
root.configure(bg=COR_FUNDO)

# Estilo ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background=COR_FUNDO, foreground=COR_TEXTO, font=("Segoe UI", 10))
style.configure("TCheckbutton", background=COR_FUNDO, foreground=COR_TEXTO, font=("Segoe UI", 10))
style.configure("TFrame", background=COR_FUNDO)
style.configure("TLabelframe", background=COR_FUNDO, foreground=COR_TEXTO)
style.configure("TLabelframe.Label", background=COR_FUNDO, foreground=COR_TEXTO)

# === Título ===
tk.Label(root, text="🔒 Gerador de Senhas Seguras", font=("Segoe UI", 16, "bold"), bg=COR_FUNDO, fg="#FFFFFF").pack(pady=15)

# === Campo de tamanho ===
frame_tamanho = tk.Frame(root, bg=COR_FUNDO)
frame_tamanho.pack(pady=5)
tk.Label(frame_tamanho, text="Tamanho da senha:", font=("Segoe UI", 11), fg=COR_TEXTO, bg=COR_FUNDO).pack(side=tk.LEFT, padx=5)
entry_tamanho = tk.Entry(frame_tamanho, width=5, justify="center", font=("Segoe UI", 11),
                         bg=COR_CAIXA, fg=COR_TEXTO, insertbackground=COR_TEXTO, relief="flat")
entry_tamanho.insert(0, "12")
entry_tamanho.pack(side=tk.LEFT)

# === Opções de caracteres ===
frame_opcoes = ttk.LabelFrame(root, text="Opções de caracteres", padding=10)
frame_opcoes.pack(pady=10, padx=20, fill="x")

var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

ttk.Checkbutton(frame_opcoes, text="Letras maiúsculas (A-Z)", variable=var_maiusculas).pack(anchor="w")
ttk.Checkbutton(frame_opcoes, text="Letras minúsculas (a-z)", variable=var_minusculas).pack(anchor="w")
ttk.Checkbutton(frame_opcoes, text="Números (0-9)", variable=var_numeros).pack(anchor="w")
ttk.Checkbutton(frame_opcoes, text="Símbolos (!@#$...)", variable=var_simbolos).pack(anchor="w")

# === Botão Gerar ===
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha,
                      bg=COR_BOTAO, fg=COR_TEXTO, font=("Segoe UI", 11, "bold"),
                      activebackground="#4682B4", activeforeground=COR_TEXTO,
                      relief="flat", padx=10, pady=6, cursor="hand2")
btn_gerar.pack(pady=10)

# === Campo de resultado ===
entry_resultado = tk.Entry(root, width=34, font=("Consolas", 13), justify="center",
                           bg=COR_CAIXA, fg=COR_TEXTO, insertbackground=COR_TEXTO,
                           relief="flat", bd=1)
entry_resultado.pack(pady=8)
entry_resultado.configure(state="readonly")

# === Botão Copiar ===
btn_copiar = tk.Button(root, text="Copiar Senha", command=copiar_senha,
                       bg=COR_BOTAO2, fg=COR_TEXTO, font=("Segoe UI", 10, "bold"),
                       activebackground="#2E7D32", activeforeground=COR_TEXTO,
                       relief="flat", padx=8, pady=4, cursor="hand2")
btn_copiar.pack(pady=6)

# === Rodapé ===
tk.Label(root, text="Feito com ❤️ em Python", font=("Segoe UI", 9),
         bg=COR_FUNDO, fg="#555555").pack(side="bottom", pady=10)

root.mainloop()


#quem leu e gay