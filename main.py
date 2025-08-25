from inventario import Inventario

def pedir_float(msg: str, minimo: float | None = None) -> float:
    while True:
        try:
            txt = input(msg).strip().replace(",", ".")
            val = float(txt)
            if minimo is not None and val < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return val
        except ValueError:
            print("Ingrese número válido.")

def pedir_int(msg: str, minimo: int | None = None) -> int:
    while True:
        try:
            txt = input(msg).strip()
            val = int(txt)
            if minimo is not None and val < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return val
        except ValueError:
            print("Ingrese entero válido.")

def pedir_float_opcional(msg: str, minimo: float | None = None) -> float | None:
    while True:
        txt = input(msg).strip().replace(",", ".")
        if txt == "":
            return None
        try:
            val = float(txt)
            if minimo is not None and val < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return val
        except ValueError:
            print("Ingrese número válido o deje vacío para mantener.")

def pedir_int_opcional(msg: str, minimo: int | None = None) -> int | None:
    while True:
        txt = input(msg).strip()
        if txt == "":
            return None
        try:
            val = int(txt)
            if minimo is not None and val < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return val
        except ValueError:
            print("Ingrese entero válido o deje vacío para mantener.")

def menu():
    inv = Inventario()
    # Si __init__ no carga datos, descomentar:
    # inv.cargar()

    try:
        while True:
            print("\n1) Listar  2) Añadir  3) Actualizar  4) Eliminar  5) Salir")
            op = input("> ").strip()

            if op == "1":
                # Asume que Inventario expone listar()
                inv.listar()

            elif op == "2":
                c = input("Código: ").strip()
                n = input("Nombre: ").strip()
                if not c:
                    print("El código no puede estar vacío.")
                    continue
                if not n:
                    print("El nombre no puede estar vacío.")
                    continue
                p = pedir_float("Precio: ", minimo=0)
                q = pedir_int("Cantidad: ", minimo=0)
                ok = inv.anadir(c, n, p, q)
                if not ok:
                    print("No se pudo añadir (posible código duplicado u otro error).")
                else:
                    if hasattr(inv, "guardar"):
                        if not inv.guardar():
                            print("Aviso: no se pudo guardar los cambios en disco.")

            elif op == "3":
                c = input("Código a actualizar: ").strip()
                if not c:
                    print("El código no puede estar vacío.")
                    continue
                n = input("Nuevo nombre (vacío=mantener): ").strip()
                precio = pedir_float_opcional("Nuevo precio (vacío=mantener): ", minimo=0)
                cantidad = pedir_int_opcional("Nueva cantidad (vacío=mantener): ", minimo=0)
                # Convierte nombre vacío a None
                n = n if n else None
                # Asume que Inventario expone actualizar(...)
                ok = inv.actualizar(c, nombre=n, precio=precio, cantidad=cantidad)
                if not ok:
                    print("No se pudo actualizar (código inexistente u otro error).")
                else:
                    if hasattr(inv, "guardar"):
                        if not inv.guardar():
                            print("Aviso: no se pudo guardar los cambios en disco.")

            elif op == "4":
                c = input("Código a eliminar: ").strip()
                if not c:
                    print("El código no puede estar vacío.")
                    continue
                ok = inv.eliminar(c)
                if not ok:
                    print("No se pudo eliminar (código inexistente u otro error).")
                else:
                    if hasattr(inv, "guardar"):
                        if not inv.guardar():
                            print("Aviso: no se pudo guardar los cambios en disco.")

            elif op == "5":
                if hasattr(inv, "cerrar"):
                    inv.cerrar()
                break

            else:
                print("Opción inválida.")

    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("¡Hasta luego!")


if __name__ == "__main__":
    menu()