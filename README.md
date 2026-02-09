# OCR de Imagens para Texto

Projeto simples de Document AI usando Python + OpenCV + Tesseract.

## O que faz

- Lê imagens de app/input
- Pré-processa com OpenCV
- Aplica OCR
- Salva resultado em JSON

## Instalação

pip install -r requirements.txt

Instalar Tesseract:
https://github.com/UB-Mannheim/tesseract/wiki

## Como usar

1. Coloque imagens em:

app/input/

2. Execute:

python -m app.main

3. Resultado:

app/output/*.json
