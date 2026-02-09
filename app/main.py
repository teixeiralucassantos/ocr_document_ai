import os
from app.image import preprocessar_imagem
from app.ocr import extrair_texto
from app.storage import salvar_json
from app.logger import log

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
INPUT = os.path.join(BASE_DIR, "app", "input")


def processar_todas_imagens():

    log("==== INICIO OCR ====")

    arquivos = os.listdir(INPUT)

    imagens = [
        f for f in arquivos
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    for img in imagens:

        caminho = os.path.join(INPUT, img)

        try:
            processada = preprocessar_imagem(caminho)

            texto = extrair_texto(processada)

            salvar_json(img, texto)

        except Exception as e:
            log(f"Erro na imagem {img}: {str(e)}")

    log("==== FIM OCR ====")


if __name__ == "__main__":
    processar_todas_imagens()
