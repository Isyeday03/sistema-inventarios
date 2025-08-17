# Sistema de Gestión de Inventarios

Un sistema completo de gestión de inventarios desarrollado en Python que permite administrar productos de una tienda de manera eficiente.

## 📋 Características

- **Gestión completa de productos**: Añadir, eliminar, actualizar y buscar productos
- **Búsqueda avanzada**: Buscar productos por ID o nombre (búsqueda parcial)
- **Validación de datos**: Verificación de IDs únicos y valores válidos
- **Interfaz intuitiva**: Menú interactivo en consola fácil de usar
- **Estadísticas**: Información detallada sobre el inventario
- **Datos de ejemplo**: Sistema pre-cargado con productos para pruebas

## 🚀 Estructura del Proyecto

```
sistema-inventarios/
├── producto.py          # Clase Producto
├── inventario.py        # Clase Inventario
├── main.py             # Interfaz de usuario y programa principal
└── README.md           # Documentación
```

## 🛠️ Clases Principales

### Clase Producto
- **Atributos**: ID único, nombre, cantidad, precio
- **Características**: Encapsulación con getters/setters, validación de datos
- **Métodos**: Constructor, métodos de acceso y representación

### Clase Inventario
- **Funcionalidades**: 
  - Gestión de lista de productos
  - Verificación de IDs únicos
  - Búsqueda por nombre e ID
  - Operaciones CRUD completas
- **Métodos principales**:
  - `agregar_producto()`
  - `eliminar_producto()`
  - `actualizar_cantidad()` / `actualizar_precio()`
  - `buscar_productos_por_nombre()`
  - `mostrar_todos_los_productos()`

### Clase SistemaInventario
- **Interfaz de usuario**: Menú interactivo en consola
- **Validación**: Entrada de datos robusta
- **Características**: 
  - Manejo de errores
  - Confirmaciones para operaciones críticas
  - Datos de ejemplo pre-cargados
  - Estadísticas del inventario

## 💻 Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo: Windows, macOS, Linux

## 🎯 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Isyeday03/sistema-inventarios.git
cd sistema-inventarios
```

### 2. Ejecutar el programa
```bash
python main.py
```

### 3. Usar el sistema
El programa iniciará con un menú interactivo que permite:

1. **Añadir nuevo producto**: Crear productos con ID único
2. **Eliminar producto**: Remover productos por ID
3. **Actualizar producto**: Modificar cantidad y/o precio
4. **Buscar por nombre**: Búsqueda parcial de productos
5. **Mostrar por ID**: Visualizar producto específico
6. **Ver inventario completo**: Lista todos los productos
7. **Estadísticas**: Información detallada del inventario

## 📊 Funcionalidades Destacadas

### ✅ Validación de Datos
- IDs únicos garantizados
- Valores no negativos para cantidades y precios
- Validación robusta de entrada de usuario

### 🔍 Búsqueda Inteligente
- Búsqueda por ID exacto
- Búsqueda parcial por nombre (no sensible a mayúsculas)
- Múltiples resultados para nombres similares

### 📈 Estadísticas Avanzadas
- Total de productos y items
- Valor total del inventario
- Precios promedio, máximo y mínimo
- Análisis completo de datos

### 🛡️ Manejo de Errores
- Validación de entrada de usuario
- Manejo de excepciones
- Mensajes informativos de error
- Confirmaciones para operaciones críticas

## 🧪 Datos de Ejemplo

El sistema incluye productos de ejemplo para facilitar las pruebas:

| ID | Producto | Cantidad | Precio |
|----|----------|----------|--------|
| 1 | Laptop HP | 5 | $899.99 |
| 2 | Mouse Logitech | 15 | $25.50 |
| 3 | Teclado Mecánico | 8 | $75.00 |
| 4 | Monitor Samsung | 3 | $299.99 |
| 5 | Auriculares Sony | 12 | $149.99 |

## 🔧 Desarrollo

### Herramientas Utilizadas
- **IDE**: PyCharm
- **Control de versiones**: Git/GitHub
- **Lenguaje**: Python 3.x

### Principios de Diseño
- **Programación Orientada a Objetos**: Clases bien estructuradas
- **Encapsulación**: Atributos privados con métodos de acceso
- **Separación de responsabilidades**: Cada clase tiene un propósito específico
- **Código limpio**: Documentación y comentarios detallados

## 📝 Notas de Implementación

### Decisiones de Diseño
1. **Atributos privados**: Uso de `__` para encapsulación
2. **Validación centralizada**: Métodos de validación en setters
3. **Búsqueda flexible**: Búsqueda parcial case-insensitive
4. **Interfaz robusta**: Manejo completo de errores de usuario

### Supuestos del Sistema
- Los IDs son números enteros positivos únicos
- Los precios y cantidades no pueden ser negativos
- La búsqueda por nombre es case-insensitive
- El sistema mantiene todos los datos en memoria

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear un Pull Request

## 👨‍💻 Autor

Desarrollado como proyecto educativo para el aprendizaje de:
- Programación Orientada a Objetos en Python
- Estructuras de datos personalizadas
- Herramientas de desarrollo (PyCharm, Git, GitHub)
- Diseño de interfaces de usuario en consola

---

**¡Gracias por usar el Sistema de Gestión de Inventarios!** 🎉