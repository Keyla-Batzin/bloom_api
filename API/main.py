from fastapi import FastAPI, HTTPException
from db import get_db_connection
from models import RamosFloresUpdateUrl, CategoriaUpdateUrl, PlantasInteriorUpdateUrl, PlantasExteriorUpdateUrl, FloresEventosUpdateUrl, MacetasAccesoriosUpdateUrl, PackUpdateUrl, Compra
from datetime import date, time
import time

DELAY_TIME = 3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API COMPRAS, amb FastAPI i MariaDB sense routers"}

####################### Categoria ###############################
# GET por ID
@app.get("/categorias/{id}")
def obtener_categoria(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categorias WHERE id = %s", (id,))
    categoria = cursor.fetchone()
    cursor.close()
    conn.close()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# GET all
@app.get("/categorias/")
def obtener_todas_categorias():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categorias")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return categorias

# PUT (Modificar URL)
@app.put("/categorias/{id}")
def modificar_url_categoria(id: int, categoria_update: CategoriaUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Categorias SET url = %s WHERE id = %s",
            (categoria_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL de la categoría actualizada correctamente"}

####################### RamosFlores ###############################
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
# Modificar la URL
@app.put("/ramos_flores/{id}")
def modificar_url_ramo_flores(id: int, ramo_flores_update: RamosFloresUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE RamosFlores SET url = %s WHERE id = %s",
            (ramo_flores_update.url, id),
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
    return {"message": "URL del ramo de flores actualizada correctamente"}

####################### PlantasInterior ###############################
# GET por ID
@app.get("/plantas_interior/{id}")
def obtener_planta_interior(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PlantasInterior WHERE id = %s", (id,))
    planta_interior = cursor.fetchone()
    cursor.close()
    conn.close()
    if not planta_interior:
        raise HTTPException(status_code=404, detail="Planta de interior no encontrada")
    return planta_interior

# GET all
@app.get("/plantas_interior/")
def obtener_todas_plantas_interior():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PlantasInterior")
    plantas_interior = cursor.fetchall()
    cursor.close()
    conn.close()
    return plantas_interior

# PUT (Modificar URL)
@app.put("/plantas_interior/{id}")
def modificar_url_planta_interior(id: int, planta_interior_update: PlantasInteriorUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE PlantasInterior SET url = %s WHERE id = %s",
            (planta_interior_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Planta de interior no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL de la planta de interior actualizada correctamente"}

####################### PlantasExterior ###############################
# GET por ID
@app.get("/plantas_exterior/{id}")
def obtener_planta_exterior(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PlantasExterior WHERE id = %s", (id,))
    planta_exterior = cursor.fetchone()
    cursor.close()
    conn.close()
    if not planta_exterior:
        raise HTTPException(status_code=404, detail="Planta de exterior no encontrada")
    return planta_exterior

# GET all
@app.get("/plantas_exterior/")
def obtener_todas_plantas_exterior():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PlantasExterior")
    plantas_exterior = cursor.fetchall()
    cursor.close()
    conn.close()
    return plantas_exterior

# PUT (Modificar URL)
@app.put("/plantas_exterior/{id}")
def modificar_url_planta_exterior(id: int, planta_exterior_update: PlantasExteriorUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE PlantasExterior SET url = %s WHERE id = %s",
            (planta_exterior_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Planta de exterior no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL de la planta de exterior actualizada correctamente"}

####################### FloresEventos ###############################
# GET por ID
@app.get("/flores_eventos/{id}")
def obtener_flor_evento(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM FloresEventos WHERE id = %s", (id,))
    flor_evento = cursor.fetchone()
    cursor.close()
    conn.close()
    if not flor_evento:
        raise HTTPException(status_code=404, detail="Flor de evento no encontrada")
    return flor_evento

# GET all
@app.get("/flores_eventos/")
def obtener_todas_flores_eventos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM FloresEventos")
    flores_eventos = cursor.fetchall()
    cursor.close()
    conn.close()
    return flores_eventos

# PUT (Modificar URL)
@app.put("/flores_eventos/{id}")
def modificar_url_flor_evento(id: int, flor_evento_update: FloresEventosUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE FloresEventos SET url = %s WHERE id = %s",
            (flor_evento_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Flor de evento no encontrada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL de la flor de evento actualizada correctamente"}

####################### MacetasAccesorios ###############################
# GET por ID
@app.get("/macetas_accesorios/{id}")
def obtener_maceta_accesorio(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MacetasAccesorios WHERE id = %s", (id,))
    maceta_accesorio = cursor.fetchone()
    cursor.close()
    conn.close()
    if not maceta_accesorio:
        raise HTTPException(status_code=404, detail="Maceta o accesorio no encontrado")
    return maceta_accesorio

# GET all
@app.get("/macetas_accesorios/")
def obtener_todas_macetas_accesorios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MacetasAccesorios")
    macetas_accesorios = cursor.fetchall()
    cursor.close()
    conn.close()
    return macetas_accesorios

# PUT (Modificar URL)
@app.put("/macetas_accesorios/{id}")
def modificar_url_maceta_accesorio(id: int, maceta_accesorio_update: MacetasAccesoriosUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE MacetasAccesorios SET url = %s WHERE id = %s",
            (maceta_accesorio_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Maceta o accesorio no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL de la maceta o accesorio actualizada correctamente"}

####################### Pack ###############################
# GET por ID
@app.get("/packs/{id}")
def obtener_pack(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pack WHERE id = %s", (id,))
    pack = cursor.fetchone()
    cursor.close()
    conn.close()
    if not pack:
        raise HTTPException(status_code=404, detail="Pack no encontrado")
    return pack

# GET all
@app.get("/packs/")
def obtener_todos_packs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pack")
    packs = cursor.fetchall()
    cursor.close()
    conn.close()
    return packs

# PUT (Modificar URL)
@app.put("/packs/{id}")
def modificar_url_pack(id: int, pack_update: PackUpdateUrl):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Pack SET url = %s WHERE id = %s",
            (pack_update.url, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Pack no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "URL del pack actualizada correctamente"}

####################### Compra ###############################
# Obtener todas las compras
@app.get("/compras/")
def obtener_todas_compras():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Compra")
        compras = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return compras

# Añadir una Compra (un Producto)
@app.post("/compras/")
def crear_compra(compra: Compra):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Insertar el nuevo ítem de compra en la base de datos
        cursor.execute(
            "INSERT INTO Compra (nombre, precio, url, cantidad) VALUES (%s, %s, %s, %s)",
            (compra.nombre, compra.precio, compra.url, compra.cantidad),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()  # Revertir la transacción en caso de error
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ítem de compra creado correctamente", "id": cursor.lastrowid}

# Eliminar una compra por ID
@app.delete("/compras/{id}")
def eliminar_compra(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Verificar si la compra existe
        cursor.execute("SELECT * FROM Compra WHERE id = %s", (id,))
        compra = cursor.fetchone()
        if not compra:
            raise HTTPException(status_code=404, detail="Compra no encontrada")

        # Eliminar la compra
        cursor.execute("DELETE FROM Compra WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        conn.rollback()  # Revertir la transacción en caso de error
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": f"Compra con ID {id} eliminada correctamente"}

# Precio total de las compras
@app.get("/compras/precio-total")
def obtener_precio_total():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Query para calcular el precio total
        query = """
        SELECT SUM(precio * cantidad) AS total
        FROM Compra
        """
        cursor.execute(query)
        resultado = cursor.fetchone()

        # Si no hay compras, el total será 0
        precio_total = float(resultado["total"]) if resultado["total"] else 0
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"precio_total": precio_total}