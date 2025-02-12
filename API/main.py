from fastapi import FastAPI, HTTPException
from db import get_db_connection
from models import Usuario, Producto, Compra, CompraProducto
from datetime import date, time
import time

DELAY_TIME = 3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API COMPRAS, amb FastAPI i MariaDB sense routers"}

# CRUD per a Usuaris
@app.post("/usuarios/")
def crear_usuario(usuario: Usuario):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Usuarios (id, rol, nombreUsuario, email, contraseña) VALUES (%s, %s, %s, %s, %s)",
            (usuario.id, usuario.rol, usuario.nombreUsuario, usuario.email, usuario.contraseña),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Usuario creado correctamente"}

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/login/{nombreUsuario}")
def obtener_usuario_por_nombre(nombreUsuario: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombreUsuario, rol FROM Usuarios WHERE nombreUsuario = %s", (nombreUsuario,))    
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# CRUD per a Productos
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

# CRUD per a Compras
@app.post("/compras/")
def crear_compra(compra: Compra):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Compras (id, idUsuario, fecha, precioTotal, hora) VALUES (%s, %s, %s, %s, %s)",
            (compra.id, compra.idUsuario, compra.fecha, compra.precioTotal, compra.hora),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra creada correctamente"}

@app.get("/compras/{id}")
def obtener_compra(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Compras WHERE id = %s", (id,))
    compra = cursor.fetchone()
    cursor.close()
    conn.close()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra

@app.get("/compras/usuario/{idUsuario}")
def obtener_compras_usuario(idUsuario: int):
    time.sleep(DELAY_TIME)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Compras.*, Productos.nombre as nombreProducto FROM Compras INNER JOIN Compras_Productos ON Compras.id = Compras_Productos.idCompra INNER JOIN Productos ON Compras_Productos.idProducto = Productos.id WHERE idUsuario = %s", (idUsuario,))
    compras = cursor.fetchall()
    cursor.close()
    conn.close()
    return compras

@app.put("/compras/{id}")
def modificar_compra(id: int, compra: Compra):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Compras SET idUsuario = %s, fecha = %s, precioTotal = %s, hora = %s WHERE id = %s",
            (compra.idUsuario, compra.fecha, compra.precioTotal, compra.hora, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Compra no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra actualizada correctamente"}

@app.delete("/compras/{id}")
def eliminar_compra(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Compras WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Compra no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra eliminada correctamente"}

# CRUD per a Compras_Productos
@app.post("/compras_productos/")
def crear_compra_producto(compra_producto: CompraProducto):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Compras_Productos (idCompra, idProducto, cantidad, precioUnitario) VALUES (%s, %s, %s, %s)",
            (compra_producto.idCompra, compra_producto.idProducto, compra_producto.cantidad, compra_producto.precioUnitario),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra_Producto creada correctamente"}

@app.get("/compras_productos/{idCompra}/{idProducto}")
def obtener_compra_producto(idCompra: int, idProducto: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM Compras_Productos WHERE idCompra = %s AND idProducto = %s",
        (idCompra, idProducto),
    )
    compra_producto = cursor.fetchone()
    cursor.close()
    conn.close()
    if not compra_producto:
        raise HTTPException(status_code=404, detail="Compra_Producto no encontrada")
    return compra_producto

@app.put("/compras_productos/{idCompra}/{idProducto}")
def modificar_compra_producto(idCompra: int, idProducto: int, compra_producto: CompraProducto):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Compras_Productos SET cantidad = %s, precioUnitario = %s WHERE idCompra = %s AND idProducto = %s",
            (compra_producto.cantidad, compra_producto.precioUnitario, idCompra, idProducto),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Compra_Producto no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra_Producto actualizada correctamente"}

@app.delete("/compras_productos/{idCompra}/{idProducto}")
def eliminar_compra_producto(idCompra: int, idProducto: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM Compras_Productos WHERE idCompra = %s AND idProducto = %s",
            (idCompra, idProducto),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Compra_Producto no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Compra_Producto eliminada correctamente"}