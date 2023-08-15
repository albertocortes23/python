# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# %%
class Item(BaseModel):
    song: str
    artist: str
    position: int

app = FastAPI()

# %%

#ENDPOINT PARA AGREGAR NOTICIAS POR MEDIO DE LA API
@app.post("/agregar_noticia/")
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO noticias (titulo, url_noticia, medio) VALUES (?, ?, ?)", (item.titulo, item.url_noticia, item.medio))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

# %%

#ENDPOINT PARA LEER TODAS LAS NOTICIAS GUARDADAS
@app.get("/leer_noticias/")
async def leer_elementos():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, url_noticia, medio FROM noticias")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"titulo": resultado[0], "url": resultado[1], "medio": resultado[2]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

# %%

#ENDPOINT PARA LEER UNA NOTICIA EN ESPECIFICO
@app.get("/leer_noticia/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, url_noticia, medio FROM noticias WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"titulo": resultado[0], "url_noticia": resultado[1], "medio": resultado[2]}
    else:
        return {"mensaje": "Datos no encontrados"}

# %%

#ENDPOINT PARA ACTUALIZAR UNA NOTICIA
@app.put("/actualizar_noticia/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE noticias SET titulo=?, url_noticia=?, medio=? WHERE id=?", (item.titulo, item.url_noticia, item.medio, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

# %%

#ENDPOINT PARA ELIMINAR UNA NOTICIA
@app.delete("/eliminar_noticia/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM noticias WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}

# %%
