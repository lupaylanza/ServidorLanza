from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

with open("trampas.json", "r", encoding="utf-8") as f:
    trampas = json.load(f)

class TextoContrato(BaseModel):
    texto: str

@app.post("/analizar")
def analizar_contrato(input: TextoContrato):
    texto = input.texto.lower()
    coincidencias = []

    for trampa in trampas:
        if trampa["clave"].lower() in texto:
            coincidencias.append(trampa)

    resumen = f"Se han detectado {len(coincidencias)} posibles trampas." if coincidencias else "No se han detectado trampas conocidas."

    return {
        "resumen": resumen,
        "total": len(coincidencias),
        "coincidencias": coincidencias
    }
