import cv2
import numpy as np
from app.logger import log

def preprocessar_imagem(caminho):
    log(f"Pré-processando imagem: {caminho}")

    img = cv2.imread(caminho)

    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        cinza, 150, 255, cv2.THRESH_BINARY
    )

    denoise = cv2.medianBlur(thresh, 3)

    return denoise
