import os
import json
from datetime import datetime
from app.logger import log

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT = os.path.join(BASE_DIR, "app", "output")

if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)


def salvar_json(nome_imagem, texto):

    dados = {
        "arquivo": nome_imagem,
        "texto_extraido": texto,
        "data": str(datetime.now())
    }

    caminho = os.path.join(
        OUTPUT,
        nome_imagem.replace(".", "_") + ".json"
    )

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    log(f"JSON salvo em: {caminho}")

    return caminho
