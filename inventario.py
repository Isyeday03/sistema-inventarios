from producto import Producto


class Inventario:
    """
    Clase que gestiona el inventario de productos de una tienda.

    Atributos:
        productos (list): Lista de productos en el inventario
    """

    def __init__(self):
        """Constructor de la clase Inventario. Inicializa lista vacía de productos."""
        self.__productos = []

    def __buscar_producto_por_id(self, id):
        """
        Método privado para buscar un producto por su ID.

        Args:
            id (int): ID del producto a buscar

        Returns:
            Producto or None: El producto si se encuentra, None en caso contrario
        """
        for producto in self.__productos:
            if producto.get_id() == id:
                return producto
        return None

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Args:
            producto (Producto): Producto a añadir

        Returns:
            bool: True si se añadió correctamente, False si ya existe el ID
        """
        # Verificar que el ID sea único
        if self.__buscar_producto_por_id(producto.get_id()) is not None:
            return False  # ID ya existe

        self.__productos.append(producto)
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.

        Args:
            id (int): ID del producto a eliminar

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró
        """
        producto = self.__buscar_producto_por_id(id)
        if producto:
            self.__productos.remove(producto)
            return True
        return False

    def actualizar_cantidad(self, id, nueva_cantidad):
        """
        Actualiza la cantidad de un producto.

        Args:
            id (int): ID del producto a actualizar
            nueva_cantidad (int): Nueva cantidad del producto

        Returns:
            bool: True si se actualizó correctamente, False si no se encontró
        """
        producto = self.__buscar_producto_por_id(id)
        if producto:
            try:
                producto.set_cantidad(nueva_cantidad)
                return True
            except ValueError:
                return False
        return False

    def actualizar_precio(self, id, nuevo_precio):
        """
        Actualiza el precio de un producto.

        Args:
            id (int): ID del producto a actualizar
            nuevo_precio (float): Nuevo precio del producto

        Returns:
            bool: True si se actualizó correctamente, False si no se encontró
        """
        producto = self.__buscar_producto_por_id(id)
        if producto:
            try:
                producto.set_precio(nuevo_precio)
                return True
            except ValueError:
                return False
        return False

    def buscar_productos_por_nombre(self, nombre):
        """
        Busca productos por nombre (búsqueda parcial, no case-sensitive).

        Args:
            nombre (str): Nombre o parte del nombre a buscar

        Returns:
            list: Lista de productos que coinciden con el nombre
        """
        productos_encontrados = []
        nombre_lower = nombre.lower()

        for producto in self.__productos:
            if nombre_lower in producto.get_nombre().lower():
                productos_encontrados.append(producto)

        return productos_encontrados

    def obtener_producto_por_id(self, id):
        """
        Obtiene un producto específico por su ID.

        Args:
            id (int): ID del producto a buscar

        Returns:
            Producto or None: El producto si se encuentra, None en caso contrario
        """
        return self.__buscar_producto_por_id(id)

    def mostrar_todos_los_productos(self):
        """
        Retorna todos los productos del inventario.

        Returns:
            list: Lista de todos los productos en el inventario
        """
        return self.__productos.copy()  # Retorna una copia para evitar modificaciones externas

    def obtener_cantidad_productos(self):
        """
        Retorna el número total de productos diferentes en el inventario.

        Returns:
            int: Número de productos en el inventario
        """
        return len(self.__productos)

    def esta_vacio(self):
        """
        Verifica si el inventario está vacío.

        Returns:
            bool: True si está vacío, False en caso contrario
        """
        return len(self.__productos) == 0