import pytesseract
from app.logger import log

# >>> SE NECESSÁRIO INFORME O CAMINHO DO TESSERACT <<<
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extrair_texto(imagem_processada):

    log("Executando OCR")

    texto = pytesseract.image_to_string(
        imagem_processada,
        lang="por"
    )

    return texto
