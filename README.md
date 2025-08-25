sistema de gestión de inventarios mejorado que cumple con todos los requisitos solicitados. Aquí están las características principales:
🌟 Características Principales
1. Almacenamiento Persistente

Formato JSON: Utiliza JSON para almacenar los datos de manera estructurada
Archivo configurable: Por defecto inventario.txt, pero se puede cambiar
Codificación UTF-8: Soporte completo para caracteres especiales

2. Manejo Robusto de Excepciones

FileNotFoundError: Maneja archivos inexistentes
PermissionError: Gestiona problemas de permisos
JSONDecodeError: Detecta archivos corruptos
Excepciones personalizadas: InventarioException para errores específicos del inventario

3. Funcionalidades Avanzadas

Carga automática: Al iniciar, carga automáticamente el inventario existente
Guardado automático: Cada modificación se guarda inmediatamente
Validación de datos: Verificación de precios y cantidades no negativos
Estadísticas: Muestra valor total del inventario y contadores
Stock bajo: Identifica productos con inventario bajo

4. Interfaz de Usuario Mejorada

Menú intuitivo: Opciones claras con iconos descriptivos
Mensajes informativos: Feedback detallado de todas las operaciones
Validación de entrada: Manejo de errores de entrada del usuario
Confirmaciones: Solicita confirmación para operaciones críticas