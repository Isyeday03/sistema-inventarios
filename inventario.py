# python
from __future__ import annotations

import json
import os
import shutil
from typing import Any, Dict, List, Optional


class Inventario:
    """
    Inventario con persistencia JSON y operaciones básicas.
    - Almacena internamente como dict[codigo] = {nombre, precio, cantidad}
    - Guarda en disco como lista de objetos [{"codigo", "nombre", "precio", "cantidad"}, ...]
    - Nunca lanza excepciones hacia el exterior en operaciones públicas; devuelve bool/None.
    """

    def __init__(self, ruta: str = "inventario.txt") -> None:
        self.ruta: str = ruta
        self.productos: Dict[str, Dict[str, Any]] = {}
        self.cargar()

    # ===================== Utilidades internas =====================

    def _crear_archivo_vacio(self) -> bool:
        try:
            data: List[Dict[str, Any]] = []
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except OSError:
            return False

    def _normalizar_producto(self, item: Dict[str, Any], codigo: str) -> Dict[str, Any]:
        nombre = str(item.get("nombre") or "").strip()
        try:
            precio = float(item.get("precio", 0.0))
        except (ValueError, TypeError):
            precio = 0.0
        try:
            cantidad = int(item.get("cantidad", 0))
        except (ValueError, TypeError):
            cantidad = 0

        if precio < 0:
            precio = 0.0
        if cantidad < 0:
            cantidad = 0

        return {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }

    def _producto_completo(self, codigo: str, base: Dict[str, Any]) -> Dict[str, Any]:
        # Construye un dict con todos los campos para guardado/listado
        return {
            "codigo": codigo,
            "nombre": str(base.get("nombre", "")).strip(),
            "precio": float(base.get("precio", 0.0)),
            "cantidad": int(base.get("cantidad", 0)),
        }

    def _copiar_como_corrupto(self) -> None:
        try:
            destino = f"{self.ruta}.corrupto"
            shutil.copyfile(self.ruta, destino)
        except OSError:
            # Silencioso: si no puede copiar, continuamos con reset
            pass

    # ===================== Persistencia =====================

    def cargar(self) -> bool:
        if not os.path.exists(self.ruta):
            self.productos = {}
            self._crear_archivo_vacio()
            return True

        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                data = json.load(f)

            productos: Dict[str, Dict[str, Any]] = {}
            if isinstance(data, list):
                for it in data:
                    if not isinstance(it, dict):
                        continue
                    codigo = str(it.get("codigo", "")).strip()
                    if not codigo:
                        continue
                    productos[codigo] = self._normalizar_producto(it, codigo)
            elif isinstance(data, dict):
                # También soporta formato dict {codigo: {...}}
                for k, v in data.items():
                    codigo = str(k).strip()
                    if not codigo or not isinstance(v, dict):
                        continue
                    productos[codigo] = self._normalizar_producto(v, codigo)
            else:
                # Formato desconocido => tratar como corrupto
                self._copiar_como_corrupto()
                self.productos = {}
                self._crear_archivo_vacio()
                return False

            self.productos = productos
            return True

        except (json.JSONDecodeError, ValueError, TypeError) as e:
            # Archivo corrupto => crear copia y reiniciar
            self._copiar_como_corrupto()
            self.productos = {}
            self._crear_archivo_vacio()
            return False
        except (FileNotFoundError, PermissionError, OSError):
            # Cualquier otro problema => intentar crear vacío
            self.productos = {}
            self._crear_archivo_vacio()
            return False

    def guardar(self) -> bool:
        try:
            data: List[Dict[str, Any]] = [
                self._producto_completo(codigo, prod)
                for codigo, prod in sorted(self.productos.items(), key=lambda x: x[0])
            ]
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except (PermissionError, OSError, TypeError, ValueError):
            return False

    # ===================== Operaciones públicas =====================

    def anadir(self, codigo: str, nombre: str, precio: float, cantidad: int) -> bool:
        codigo = str(codigo).strip()
        if not codigo:
            return False
        nombre = str(nombre).strip()
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            return False
        if precio < 0 or cantidad < 0:
            return False
        if codigo in self.productos:
            return False

        self.productos[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        return self.guardar()

    def eliminar(self, codigo: str) -> bool:
        """
        Elimina el producto por código. Devuelve True si elimina algo, False si no existe o falla el guardado.
        No lanza excepciones.
        """
        codigo = str(codigo).strip()
        if not codigo or codigo not in self.productos:
            return False
        del self.productos[codigo]
        return self.guardar()

    def actualizar(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        precio: Optional[float] = None,
        cantidad: Optional[int] = None,
    ) -> bool:
        """
        Actualiza campos del producto. Solo cambia los argumentos no None.
        Devuelve True si se actualiza y guarda correctamente.
        """
        codigo = str(codigo).strip()
        if not codigo or codigo not in self.productos:
            return False

        prod = self.productos[codigo].copy()

        if nombre is not None:
            prod["nombre"] = str(nombre).strip()
        if precio is not None:
            try:
                p = float(precio)
            except (ValueError, TypeError):
                return False
            if p < 0:
                return False
            prod["precio"] = p
        if cantidad is not None:
            try:
                c = int(cantidad)
            except (ValueError, TypeError):
                return False
            if c < 0:
                return False
            prod["cantidad"] = c

        # Normaliza para asegurar atributos completos
        prod = self._normalizar_producto(prod, codigo)
        self.productos[codigo] = prod
        return self.guardar()

    def obtener(self, codigo: str) -> Optional[Dict[str, Any]]:
        """
        Obtiene un producto completo con todos los campos, o None si no existe.
        """
        codigo = str(codigo).strip()
        if not codigo or codigo not in self.productos:
            return None
        base = self.productos[codigo]
        return self._producto_completo(codigo, base)

    def listar(self) -> List[Dict[str, Any]]:
        """
        Lista todos los productos con todos los campos.
        """
        return [
            self._producto_completo(codigo, prod)
            for codigo, prod in sorted(self.productos.items(), key=lambda x: x[0])
        ]

    def existe(self, codigo: str) -> bool:
        return str(codigo).strip() in self.productos

    def valor_total(self) -> float:
        return float(sum(p["precio"] * p["cantidad"] for p in self.productos.values()))