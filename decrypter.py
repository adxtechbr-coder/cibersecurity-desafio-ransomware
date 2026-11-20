import os
import pyaes

# ============================================================
# DECRIPTADOR DIDÁTICO — DESAFIO DIO RANSOMWARE PYTHON
# Instructor: Cassiano Peres | Curso: Cibersegurança
# ============================================================
# Fluxo:
#   1. Abre o arquivo criptografado (.ransomwaretroll) em modo binário (rb)
#   2. Lê o conteúdo cifrado
#   3. Remove o arquivo criptografado
#   4. Descriptografa com a MESMA chave (AES-CTR é simétrico)
#   5. Salva o arquivo original restaurado
# ============================================================

# Nome do arquivo criptografado a ser descriptografado
file_name = "teste.txt.ransomwaretroll"

try:
    # ETAPA 1: Abrir arquivo criptografado em modo binário de leitura (rb)
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()
    print(f"[+] Arquivo criptografado '{file_name}' lido ({len(file_data)} bytes)")

except FileNotFoundError:
    # Tratamento explícito: arquivo .ransomwaretroll não encontrado
    print(f"[ERRO] Arquivo criptografado '{file_name}' não encontrado.")
    print("       Execute primeiro o encrypter.py ou verifique o nome do arquivo.")
    exit(1)

# ETAPA 2: Chave de descriptografia (DEVE SER IDÊNTICA à de criptografia)
# AES-CTR usa a mesma chave para cifrar e decifrar (cifra simétrica)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# ETAPA 3: Descriptografar os dados
# decrypt() inverte a operação de encrypt() no modo CTR
decrypt_data = aes.decrypt(file_data)
print(f"[+] Dados descriptografados ({len(decrypt_data)} bytes)")

# ETAPA 4: Remover o arquivo criptografado
os.remove(file_name)
print(f"[+] Arquivo criptografado '{file_name}' removido")

# ETAPA 5: Recriar o arquivo original com o conteúdo restaurado
new_file_name = "teste.txt"
new_file = open(new_file_name, "wb")  # 'wb' = write binary
new_file.write(decrypt_data)
new_file.close()
print(f"[+] Arquivo original restaurado como '{new_file_name}'")
print("[✓] Descriptografia concluída com sucesso — arquivo legível novamente")