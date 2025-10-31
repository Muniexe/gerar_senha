import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets
from datetime import datetime

ARQUIVO_SENHAS = "senhas.txt"

# === Funções ===
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho.")
        return

    if tamanho < 4 or tamanho > 64:
        messagebox.showwarning("Aviso", "O tamanho deve estar entre 4 e 64 caracteres.")
        return

    caracteres = ""
    if var_maiusculas.get():
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    entry_resultado.configure(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)
    entry_resultado.configure(state="readonly")

    salvar_senha(senha)
    atualizar_historico()

def copiar_senha():
    senha = entry_resultado.get()
    if not senha:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")
        return

    root.clipboard_clear()
    root.clipboard_append(senha)
    lbl_copiado.config(text="✅ Copiado!", fg="#00C853")
    root.after(1500, lambda: lbl_copiado.config(text=""))

def salvar_senha(senha):
    """Salva a senha em um arquivo local com data e hora."""
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARQUIVO_SENHAS, "a", encoding="utf-8") as f:
        f.write(f"[{agora}] {senha}\n")

def atualizar_historico():
    """Atualiza a lista de senhas na interface."""
    listbox_senhas.delete(0, tk.END)
    try:
        with open(ARQUIVO_SENHAS, "r", encoding="utf-8") as f:
            linhas = f.readlines()[-10:]  # mostra as 10 mais recentes
        for linha in linhas:
            listbox_senhas.insert(tk.END, linha.strip())
    except FileNotFoundError:
        pass

def limpar_historico():
    """Limpa apenas a lista da interface, não o arquivo."""
    listbox_senhas.delete(0, tk.END)
    lbl_copiado.config(text="🗑 Histórico limpo!", fg="#FF6F00")
    root.after(1500, lambda: lbl_copiado.config(text=""))

# === Interface ===
root = tk.Tk()
root.title("🔒 Gerador de Senhas Seguras")
root.geometry("440x550")
root.resizable(False, False)

# === Cores ===
COR_TEXTO = "#FFFFFF"
COR_FUNDO = "#000000"
COR_RESULTADO = "#000000"
COR_BOTAO = "#1E90FF"
COR_BOTAO2 = "#00C853"
COR_CAIXA = "#111111"

root.configure(bg=COR_FUNDO)

# === Estilo ===
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background=COR_FUNDO, foreground=COR_TEXTO, font=("Segoe UI", 10))
style.configure("TCheckbutton", background=COR_FUNDO, foreground=COR_TEXTO, font=("Segoe UI", 10))
style.configure("TLabelframe", background=COR_FUNDO, foreground=COR_TEXTO)
style.configure("TLabelframe.Label", background=COR_FUNDO, foreground=COR_TEXTO)

# === Título ===
tk.Label(root, text="🔒 Gerador de Senhas Seguras", font=("Segoe UI", 16, "bold"),
         bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=15)

# === Campo de tamanho ===
frame_tamanho = tk.Frame(root, bg=COR_FUNDO)
frame_tamanho.pack(pady=5)
tk.Label(frame_tamanho, text="Tamanho da senha:", font=("Segoe UI", 11),
         fg=COR_TEXTO, bg=COR_FUNDO).pack(side=tk.LEFT, padx=5)
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
                           bg=COR_CAIXA, fg=COR_RESULTADO, insertbackground=COR_TEXTO,
                           relief="flat", bd=1, state="readonly")
entry_resultado.pack(pady=8)

# === Botão Copiar + Label ===
frame_copy = tk.Frame(root, bg=COR_FUNDO)
frame_copy.pack()
btn_copiar = tk.Button(frame_copy, text="Copiar Senha", command=copiar_senha,
                       bg=COR_BOTAO2, fg=COR_TEXTO, font=("Segoe UI", 10, "bold"),
                       activebackground="#2E7D32", activeforeground=COR_TEXTO,
                       relief="flat", padx=8, pady=4, cursor="hand2")
btn_copiar.pack(side="left", pady=6)
lbl_copiado = tk.Label(frame_copy, text="", bg=COR_FUNDO, fg="#00C853", font=("Segoe UI", 10, "italic"))
lbl_copiado.pack(side="left", padx=10)

# === Histórico ===
frame_hist = ttk.LabelFrame(root, text="Histórico de senhas (últimas 10)", padding=10)
frame_hist.pack(pady=10, padx=20, fill="both", expand=True)

listbox_senhas = tk.Listbox(frame_hist, bg=COR_CAIXA, fg=COR_TEXTO,
                            font=("Consolas", 10), selectbackground="#333333",
                            height=7, relief="flat")
listbox_senhas.pack(fill="both", expand=True, padx=5, pady=5)

btn_limpar = tk.Button(root, text="🗑 Limpar histórico", command=limpar_historico,
                       bg="#444444", fg=COR_TEXTO, font=("Segoe UI", 9),
                       activebackground="#555555", relief="flat", cursor="hand2")
btn_limpar.pack(pady=5)

# === Rodapé ===
tk.Label(root, text="Feito com ❤️ em Python", font=("Segoe UI", 9),
         bg=COR_FUNDO, fg="#555555").pack(side="bottom", pady=10)

# Atualiza histórico ao iniciar
atualizar_historico()

root.mainloop()


#quem leu e gay