from fastapi import FastAPI
from pydantic import BaseModel

app = fastAPI()

class Animal(BaseModel):
    nombre: str
    tipo: str
    vuelan: bool


db = {

    "perro": Animal(nombre="perro", tipo="mamifero", vuelan=False),
    "pajaro": Animal(nombre="pajaro", tipo="ave", vuelan=True)
}

#@app.get("/animales/")




