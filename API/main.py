from fastapi import FastAPI, HTTPException
from db import get_db_connection
from models import Producto,RamosFlores
from datetime import date, time
import time

DELAY_TIME = 3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API COMPRAS, amb FastAPI i MariaDB sense routers"}

####################### CRUD Productos ###############################
@app.post("/productos/")
def crear_producto(producto: Producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Productos (id, nombre, precio, urlImagen, categoria) VALUES (%s, %s, %s, %s, %s)",
            (producto.id, producto.nombre, producto.precio, producto.urlImagen, producto.categoria),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Producto creado correctamente"}

@app.get("/productos/{id}")
def obtener_producto(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos WHERE id = %s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.get("/productos/")
def obtener_todos_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos

@app.put("/productos/{id}")
def modificar_producto(id: int, producto: Producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Productos SET nombre = %s, precio = %s, urlImagen = %s, categoria = %s WHERE id = %s",
            (producto.nombre, producto.precio, producto.urlImagen, producto.categoria, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Producto actualizado correctamente"}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Productos WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Producto eliminado correctamente"}


####################### CRUD RamosFlores ###############################
# POST
@app.post("/ramos_flores/")
def crear_ramo_flores(ramo_flores: RamosFlores):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO RamosFlores (id, nombre, precio, urlImagen) VALUES (%s, %s, %s, %s)",
            (ramo_flores.id, ramo_flores.nombre, ramo_flores.precio, ramo_flores.urlImagen),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ramo de flores creado correctamente"}

#GET por ID
@app.get("/ramos_flores/{id}")
def obtener_ramo_flores(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM RamosFlores WHERE id = %s", (id,))
    ramo_flores = cursor.fetchone()
    cursor.close()
    conn.close()
    if not ramo_flores:
        raise HTTPException(status_code=404, detail="Ramo de flores no encontrado")
    return ramo_flores

#GET all
@app.get("/ramos_flores/")
def obtener_todos_ramos_flores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM RamosFlores")
    ramos_flores = cursor.fetchall()
    cursor.close()
    conn.close()
    return ramos_flores

# PUT
@app.put("/ramos_flores/{id}")
def modificar_ramo_flores(id: int, ramo_flores: RamosFlores):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE RamosFlores SET nombre = %s, precio = %s, urlImagen = %s WHERE id = %s",
            (ramo_flores.nombre, ramo_flores.precio, ramo_flores.urlImagen, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ramo de flores no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ramo de flores actualizado correctamente"}

# DELETE
@app.delete("/ramos_flores/{id}")
def eliminar_ramo_flores(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM RamosFlores WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ramo de flores no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ramo de flores eliminado correctamente"}