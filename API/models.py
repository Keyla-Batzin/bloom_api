from pydantic import BaseModel
from datetime import date, time
from typing import List, Optional

###########################################################################
# MODELOS
###########################################################################

####### CATEGORIA #######
# Tabla Categoria
class Categoria(BaseModel):
    id: int
    nombre: str
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Categoria
class CategoriaUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### RAMOS FLORES #######
# Tabla Ramos Flores
class RamosFlores(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Ramos Flores
class RamosFloresUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### PLANTAS INTERIOR #######
# Tabla Plantas Interior
class PlantasInterior(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Plantas Interior
class PlantasInteriorUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### PLANTAS EXTERIOR #######
# Tabla Plantas Exterior
class PlantasExterior(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Plantas Exterior
class PlantasExteriorUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### FLORES EVENTOS #######
# Tabla Flores Eventos
class FloresEventos(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Flores Eventos
class FloresEventosUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### MACETAS Y ACESORIOS #######
# Tabla Macetas Accesorios
class MacetasAccesorios(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Macetas Accesorios
class MacetasAccesoriosUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

####### PACK #######
# Tabla Pack
class Pack(BaseModel):
    id: int
    nombre: str
    precio: float
    url: Optional[str] = None

    class Config:
        orm_mode = True

# Modelo para modificar URL Pack
class PackUpdateUrl(BaseModel):
    url: Optional[str] = None

    class Config:
        orm_mode = True

###########################################################################
# OTROS MODELOS
###########################################################################
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