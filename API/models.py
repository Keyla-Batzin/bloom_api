from pydantic import BaseModel
from datetime import date, time
from typing import List, Optional

class Usuario(BaseModel):
    id: int
    rol: str  # 'admin' o 'cliente'
    nombreUsuario: str
    email: str
    contraseña: str

    class Config:
        orm_mode = True

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    urlImagen: Optional[str] = None
    categoria: str = 'general'

    class Config:
        orm_mode = True

class Compra(BaseModel):
    id: int
    idUsuario: int
    fecha: Optional[date] = None
    precioTotal: float
    hora: Optional[time] = None

    class Config:
        orm_mode = True

class CompraProducto(BaseModel):
    idCompra: int
    idProducto: int
    cantidad: int = 1
    precioUnitario: float

    class Config:
        orm_mode = True

# Ejemplo de cómo podrías representar una compra con sus productos
class CompraDetalle(BaseModel):
    compra: Compra
    productos: List[CompraProducto]

    class Config:
        orm_mode = True


# Tabla Ramos Flores
class RamosFlores(BaseModel):
    id: int
    nombre: str
    precio: float
    urlImagen: Optional[str] = None

    class Config:
        orm_mode = True