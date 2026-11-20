# Ransomware Didático com Python — Desafio DIO

> **Contexto:** Projeto desenvolvido como parte do desafio **"Criando um Ransomware com Python"** da [Digital Innovation One (DIO)](https://www.dio.me/), ministrado pelo instrutor **Cassiano Peres** no curso de Cibersegurança.

---

## 📖 Descrição do Projeto

Este repositório contém uma implementação **educacional e controlada** de um ransomware simples em Python, utilizando a biblioteca `pyaes` para criptografia AES no modo CTR (Counter). O objetivo é demonstrar, de forma didática, o fluxo básico de funcionamento de um ransomware: **criptografar arquivos, remover os originais e exigir uma chave para recuperação**.

> ⚠️ **AVISO IMPORTANTE:** Este projeto é **exclusivamente educacional**. Deve ser executado **apenas em ambiente controlado** (máquina virtual, sandbox ou arquivo de teste local). O uso indevido para criptografar dados de terceiros sem autorização é crime.

---

## 🔄 Fluxo de Funcionamento

### 🔒 Ransomware (`encrypter.py`)

1. Abre `teste.txt` em modo binário de leitura (`rb`)
2. Lê todo o conteúdo do arquivo para memória
3. Remove o arquivo original do disco (`os.remove`)
4. Gera chave AES-128 (16 bytes): `b"testeransomwares"`
5. Criptografa os dados com `pyaes.AESModeOfOperationCTR`
6. Salva o resultado como `teste.txt.ransomwaretroll`

### 🔓 Descriptografador (`decrypter.py`)

1. Abre `teste.txt.ransomwaretroll` em modo binário (`rb`)
2. Lê o conteúdo cifrado
3. Remove o arquivo criptografado
4. Usa a **mesma chave** para descriptografar (AES-CTR é simétrico)
5. Restaura o arquivo original como `teste.txt`

---

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `encrypter.py` | Script que criptografa `teste.txt` → `teste.txt.ransomwaretroll` |
| `decrypter.py` | Script que descriptografa `teste.txt.ransomwaretroll` → `teste.txt` |
| `teste.txt` | Arquivo de teste com conteúdo: `Este arquivo sera criptografado` |

---

## ✅ Pré-requisitos

- **Python 3.8+** instalado
- Biblioteca `pyaes` instalada via pip:

```bash
pip install pyaes
```

---

## ▶️ Passo a Passo de Execução

```bash
# 1. Criar arquivo de teste
echo "Este arquivo sera criptografado" > teste.txt

# 2. Executar o ransomware (criptografa e remove o original)
python encrypter.py

# 3. Verificar que o original sumiu e o .ransomwaretroll existe
ls

# 4. Executar o descriptografador (restaura o original)
python decrypter.py

# 5. Confirmar que o arquivo voltou legível
cat teste.txt
```

**Saída esperada final:**
```
Este arquivo sera criptografado
```

---

## ⚙️ Detalhes Técnicos

### Por que a chave deve ter exatamente 16, 24 ou 32 bytes?

O AES (Advanced Encryption Standard) é um algoritmo de bloco que opera com tamanhos de chave fixos:

| Tamanho da chave | Algoritmo | Bits de segurança |
|------------------|-----------|-------------------|
| **16 bytes**     | AES-128   | 128 bits          |
| **24 bytes**     | AES-192   | 192 bits          |
| **32 bytes**     | AES-256   | 256 bits          |

No modo **CTR (Counter)**, o `pyaes` **não aceita chaves de tamanho arbitrário** — ele valida internamente e lança erro se a chave não tiver um desses três tamanhos. A string `"testeransomwares"` tem exatamente **16 caracteres ASCII** → **16 bytes** → compatível com **AES-128**.

> 💡 No modo CTR, o AES funciona como *stream cipher*: não há necessidade de *padding* (preenchimento), pois cada bloco de 16 bytes é XORado com a saída do contador criptografado.

---

## 🔗 Referências

- **Curso DIO:** [Cibersegurança — Criando um Ransomware com Python](https://www.dio.me/)
- **Instrutor:** Cassiano Peres
- **Repo-base original:** https://github.com/cassiano-dio/cibersecurity-desafio-ransomware
- **Documentação pyaes:** https://pypi.org/project/pyaes/

---

## 📜 Licença

Projeto educacional sem fins lucrativos. Use com responsabilidade e apenas em ambientes autorizados.