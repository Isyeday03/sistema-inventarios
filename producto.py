class Producto:
    """
    Clase que representa un producto en el inventario.

    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto
        cantidad (int): Cantidad disponible en inventario
        precio (float): Precio unitario del producto
    """

    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Args:
            id (int): ID único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad inicial del producto
            precio (float): Precio unitario del producto
        """
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        """Retorna el ID del producto."""
        return self.__id

    def get_nombre(self):
        """Retorna el nombre del producto."""
        return self.__nombre

    def get_cantidad(self):
        """Retorna la cantidad del producto."""
        return self.__cantidad

    def get_precio(self):
        """Retorna el precio del producto."""
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        """
        Establece el nombre del producto.

        Args:
            nombre (str): Nuevo nombre del producto
        """
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Establece la cantidad del producto.

        Args:
            cantidad (int): Nueva cantidad del producto
        """
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    def set_precio(self, precio):
        """
        Establece el precio del producto.

        Args:
            precio (float): Nuevo precio del producto
        """
        if precio >= 0:
            self.__precio = precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def __str__(self):
        """
        Representación en string del producto para mostrar información.

        Returns:
            str: Información formateada del producto
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

    def __repr__(self):
        """
        Representación técnica del objeto Producto.

        Returns:
            str: Representación del objeto
        """
        return f"Producto(id={self.__id}, nombre='{self.__nombre}', cantidad={self.__cantidad}, precio={self.__precio})"