from fastapi import FastAPI, HTTPException
from db import get_db_connection
from models import Usuario, Producto, Compra, CompraProducto
from datetime import datetime

app = FastAPI()

# CRUD para Usuario

@app.post("/usuarios/")
def crear_usuario(usuario: Usuario):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Usuario (nombre, rol, correo, contraseña) VALUES (%s, %s, %s, %s)",
            (usuario.nombre, usuario.rol, usuario.correo, usuario.contraseña),
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
    cursor.execute("SELECT * FROM Usuario WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# CRUD para Producto

@app.post("/productos/")
def crear_producto(producto: Producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Producto (nombre, categoria, precio, imagen_url) VALUES (%s, %s, %s, %s)",
            (producto.nombre, producto.categoria, producto.precio, producto.imagen_url),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Producto creado correctamente"}

@app.get("/productos/{idProducto}")
def obtener_producto(idProducto: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# CRUD para Compra

@app.post("/compras/")
def crear_compra(compra: Compra):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Compra (fechaCompra, idUsuario) VALUES (%s, %s)",
            (compra.fechaCompra, compra.idUsuario),
        )
        conn.commit()
        idCompra = cursor.lastrowid  # Obtener el id de la compra recién insertada
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return {"message": "Compra creada correctamente", "idCompra": idCompra}

@app.get("/compras/{idCompra}")
def obtener_compra(idCompra: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Compra WHERE idCompra = %s", (idCompra,))
    compra = cursor.fetchone()
    cursor.close()
    conn.close()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra

# Relacionar productos con compras (tabla intermedia Compra_Producto)

@app.post("/compras/{idCompra}/productos/")
def agregar_producto_compra(idCompra: int, productos: List[CompraProducto]):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for producto in productos:
            cursor.execute(
                "INSERT INTO Compra_Producto (idCompra, idProducto, cantidad) VALUES (%s, %s, %s)",
                (idCompra, producto.idProducto, producto.cantidad),
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Productos añadidos a la compra correctamente"}
