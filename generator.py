import string
import random

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
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
        raise ValueError("Selecione ao menos um tipo de caractere!")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


if __name__ == "__main__":
    print("=== Gerador de Senhas Seguras ===")
    tamanho = int(input("Tamanho da senha: "))
    senha = gerar_senha(tamanho=tamanho)
    print(f"Sua senha gerada: {senha}")
