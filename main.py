from fastapi import FastAPI
import random
import string

app = FastAPI()

def generar_contraseña(longitud: int = 12, mayusculas: bool = True, numeros: bool = True, especiales: bool = True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

@app.get("/generar_contraseña/")
def obtener_contraseña(longitud: int = 12, mayusculas: bool = True, numeros: bool = True, especiales: bool = True):
    contraseña = generar_contraseña(longitud, mayusculas, numeros, especiales)
    return {"contraseña": contraseña}
