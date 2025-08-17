from producto import Producto
from inventario import Inventario
import os


class SistemaInventario:
    """
    Clase principal que maneja la interfaz de usuario del sistema de inventarios.
    """

    def __init__(self):
        """Constructor que inicializa el inventario."""
        self.inventario = Inventario()
        self.cargar_datos_ejemplo()  # Carga algunos productos de ejemplo

    def cargar_datos_ejemplo(self):
        """
        Carga algunos productos de ejemplo para probar el sistema.
        """
        productos_ejemplo = [
            Producto(1, "Laptop HP", 5, 899.99),
            Producto(2, "Mouse Logitech", 15, 25.50),
            Producto(3, "Teclado Mecánico", 8, 75.00),
            Producto(4, "Monitor Samsung", 3, 299.99),
            Producto(5, "Auriculares Sony", 12, 149.99)
        ]

        for producto in productos_ejemplo:
            self.inventario.agregar_producto(producto)

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema."""
        print("\n" + "=" * 50)
        print("     SISTEMA DE GESTIÓN DE INVENTARIOS")
        print("=" * 50)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar producto por ID")
        print("6. Mostrar todos los productos")
        print("7. Estadísticas del inventario")
        print("0. Salir")
        print("-" * 50)

    def obtener_entero(self, mensaje, valor_minimo=None):
        """
        Solicita al usuario un número entero con validación.

        Args:
            mensaje (str): Mensaje a mostrar al usuario
            valor_minimo (int): Valor mínimo permitido (opcional)

        Returns:
            int: Número entero válido ingresado por el usuario
        """
        while True:
            try:
                valor = int(input(mensaje))
                if valor_minimo is not None and valor < valor_minimo:
                    print(f"Error: El valor debe ser mayor o igual a {valor_minimo}")
                    continue
                return valor
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")

    def obtener_float(self, mensaje, valor_minimo=None):
        """
        Solicita al usuario un número decimal con validación.

        Args:
            mensaje (str): Mensaje a mostrar al usuario
            valor_minimo (float): Valor mínimo permitido (opcional)

        Returns:
            float: Número decimal válido ingresado por el usuario
        """
        while True:
            try:
                valor = float(input(mensaje))
                if valor_minimo is not None and valor < valor_minimo:
                    print(f"Error: El valor debe ser mayor o igual a {valor_minimo}")
                    continue
                return valor
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

    def agregar_producto(self):
        """Maneja la adición de un nuevo producto."""
        print("\n--- AÑADIR NUEVO PRODUCTO ---")

        id_producto = self.obtener_entero("Ingrese el ID del producto: ", 1)

        # Verificar si ya existe el ID
        if self.inventario.obtener_producto_por_id(id_producto):
            print(f"Error: Ya existe un producto con el ID {id_producto}")
            return

        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío")
            return

        cantidad = self.obtener_entero("Ingrese la cantidad: ", 0)
        precio = self.obtener_float("Ingrese el precio: $", 0)

        producto = Producto(id_producto, nombre, cantidad, precio)

        if self.inventario.agregar_producto(producto):
            print(f"✓ Producto '{nombre}' añadido exitosamente al inventario.")
        else:
            print("Error: No se pudo añadir el producto.")

    def eliminar_producto(self):
        """Maneja la eliminación de un producto."""
        print("\n--- ELIMINAR PRODUCTO ---")

        if self.inventario.esta_vacio():
            print("El inventario está vacío.")
            return

        id_producto = self.obtener_entero("Ingrese el ID del producto a eliminar: ")

        # Mostrar información del producto antes de eliminar
        producto = self.inventario.obtener_producto_por_id(id_producto)
        if producto:
            print(f"Producto encontrado: {producto}")
            confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/N): ")

            if confirmacion.lower() == 's':
                if self.inventario.eliminar_producto(id_producto):
                    print("✓ Producto eliminado exitosamente.")
                else:
                    print("Error: No se pudo eliminar el producto.")
            else:
                print("Eliminación cancelada.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}")

    def actualizar_producto(self):
        """Maneja la actualización de un producto."""
        print("\n--- ACTUALIZAR PRODUCTO ---")

        if self.inventario.esta_vacio():
            print("El inventario está vacío.")
            return

        id_producto = self.obtener_entero("Ingrese el ID del producto a actualizar: ")

        producto = self.inventario.obtener_producto_por_id(id_producto)
        if not producto:
            print(f"No se encontró un producto con el ID {id_producto}")
            return

        print(f"Producto actual: {producto}")
        print("\n¿Qué desea actualizar?")
        print("1. Cantidad")
        print("2. Precio")
        print("3. Ambos")

        opcion = self.obtener_entero("Seleccione una opción (1-3): ")

        if opcion == 1 or opcion == 3:
            nueva_cantidad = self.obtener_entero(f"Nueva cantidad (actual: {producto.get_cantidad()}): ", 0)
            if self.inventario.actualizar_cantidad(id_producto, nueva_cantidad):
                print("✓ Cantidad actualizada exitosamente.")
            else:
                print("Error al actualizar la cantidad.")

        if opcion == 2 or opcion == 3:
            nuevo_precio = self.obtener_float(f"Nuevo precio (actual: ${producto.get_precio():.2f}): $", 0)
            if self.inventario.actualizar_precio(id_producto, nuevo_precio):
                print("✓ Precio actualizado exitosamente.")
            else:
                print("Error al actualizar el precio.")

    def buscar_por_nombre(self):
        """Maneja la búsqueda de productos por nombre."""
        print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")

        if self.inventario.esta_vacio():
            print("El inventario está vacío.")
            return

        nombre = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
        if not nombre:
            print("Error: Debe ingresar un nombre para buscar.")
            return

        productos_encontrados = self.inventario.buscar_productos_por_nombre(nombre)

        if productos_encontrados:
            print(f"\n✓ Se encontraron {len(productos_encontrados)} producto(s):")
            print("-" * 70)
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos que contengan '{nombre}'")

    def mostrar_producto_por_id(self):
        """Muestra un producto específico por su ID."""
        print("\n--- BUSCAR PRODUCTO POR ID ---")

        if self.inventario.esta_vacio():
            print("El inventario está vacío.")
            return

        id_producto = self.obtener_entero("Ingrese el ID del producto: ")

        producto = self.inventario.obtener_producto_por_id(id_producto)
        if producto:
            print("-" * 70)
            print(producto)
        else:
            print(f"No se encontró un producto con el ID {id_producto}")

    def mostrar_todos_productos(self):
        """Muestra todos los productos del inventario."""
        print("\n--- INVENTARIO COMPLETO ---")

        productos = self.inventario.mostrar_todos_los_productos()

        if productos:
            print(f"Total de productos: {len(productos)}")
            print("-" * 70)
            for producto in productos:
                print(producto)
        else:
            print("El inventario está vacío.")

    def mostrar_estadisticas(self):
        """Muestra estadísticas del inventario."""
        print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")

        productos = self.inventario.mostrar_todos_los_productos()

        if not productos:
            print("El inventario está vacío.")
            return

        total_productos = len(productos)
        total_items = sum(producto.get_cantidad() for producto in productos)
        valor_total = sum(producto.get_cantidad() * producto.get_precio() for producto in productos)
        precio_promedio = sum(producto.get_precio() for producto in productos) / total_productos

        print(f"• Productos diferentes: {total_productos}")
        print(f"• Total de items en inventario: {total_items}")
        print(f"• Valor total del inventario: ${valor_total:.2f}")
        print(f"• Precio promedio por producto: ${precio_promedio:.2f}")

        # Producto más caro y más barato
        producto_mas_caro = max(productos, key=lambda p: p.get_precio())
        producto_mas_barato = min(productos, key=lambda p: p.get_precio())

        print(f"• Producto más caro: {producto_mas_caro.get_nombre()} (${producto_mas_caro.get_precio():.2f})")
        print(f"• Producto más barato: {producto_mas_barato.get_nombre()} (${producto_mas_barato.get_precio():.2f})")

    def pausar(self):
        """Pausa el programa hasta que el usuario presione Enter."""
        input("\nPresione Enter para continuar...")

    def ejecutar(self):
        """Ejecuta el bucle principal del programa."""
        while True:
            self.mostrar_menu_principal()

            try:
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    self.agregar_producto()
                elif opcion == 2:
                    self.eliminar_producto()
                elif opcion == 3:
                    self.actualizar_producto()
                elif opcion == 4:
                    self.buscar_por_nombre()
                elif opcion == 5:
                    self.mostrar_producto_por_id()
                elif opcion == 6:
                    self.mostrar_todos_productos()
                elif opcion == 7:
                    self.mostrar_estadisticas()
                elif opcion == 0:
                    print("\n¡Gracias por usar el Sistema de Gestión de Inventarios!")
                    print("¡Hasta luego!")
                    break
                else:
                    print("Error: Opción no válida. Por favor seleccione un número del 0 al 7.")

                if opcion != 0:
                    self.pausar()

            except ValueError:
                print("Error: Por favor ingrese un número válido.")
                self.pausar()
            except KeyboardInterrupt:
                print("\n\nPrograma interrumpido por el usuario.")
                print("¡Hasta luego!")
                break


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.ejecutar()