from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Modelo Usuario
class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    rol: str
    correo: str
    contraseña: str

# Modelo Producto
class Producto(BaseModel):
    idProducto: Optional[int] = None
    nombre: str
    categoria: str
    precio: float
    imagen_url: Optional[str] = None

# Modelo Compra
class Compra(BaseModel):
    idCompra: Optional[int] = None
    fechaCompra: datetime
    idUsuario: int

# Modelo CompraProducto (relación entre Compra y Producto)
class CompraProducto(BaseModel):
    idCompra: int
    idProducto: int
    cantidad: int
