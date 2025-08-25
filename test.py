# python
import os
import tempfile
from inventario import Inventario

def pruebas():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "inventario_test.txt")

        # Inicializa inventario (crea archivo vacío si no existe)
        inv = Inventario(path)
        assert inv.anadir("X1", "Prueba", 1.0, 2)
        assert inv.guardar()

        # Corrompe el archivo a propósito
        with open(path, "w", encoding="utf-8") as f:
            f.write("basura no JSON")

        # Nueva carga debe detectar corrupción, crear copia y reiniciar a vacío
        inv2 = Inventario(path)
        copia = path + ".corrupto"
        assert os.path.exists(copia), "Se esperaba copia .corrupto del archivo inválido"
        assert inv2.productos == {}, "El inventario debería reiniciarse a vacío tras corrupción"

        # Debe permitir añadir tras reinicio
        assert inv2.anadir("Y1", "Nuevo", 2.0, 3)

        print("[OK] Tests pasados.")

if __name__ == "__main__":
    pruebas()