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

class Compra(BaseModel):
    id: int
    nombre: str
    precio: float
    cantidad: int
    url: Optional[str] = None

    class Config:
        orm_mode = True
