# Payload Generator #

**Payload Generator** es una herramienta avanzada de generación de payloads en PHP, diseñada específicamente para pruebas de penetración en aplicaciones web, con esta herramienta puedes seleccionar y generar payloads organizados en categorías por niveles de complejidad, desde **Básico** hasta **Zona de Peligro**, su propósito es permitir la evaluación de la seguridad web en entornos de prueba controlados.

---

## ⚠️ Disclaimer
Esta herramienta fue creada por **Técnicos en Hacking** y está destinada exclusivamente a fines educativos y de auditoría en entornos controlados y con permiso, **No nos hacemos responsables del mal uso de esta herramienta,** Utilízala solo en sistemas y redes donde tengas autorización expresa para realizar pruebas de seguridad.

---

## Características
- **Categorías de Payloads**:
  - **Básico**: Payloads para pruebas iniciales de seguridad y configuración.
  - **Medio**: Payloads de mayor funcionalidad para pruebas avanzadas.
  - **Avanzado**: Payloads más complejos para simulación de vulnerabilidades críticas.
  - **Zona de Peligro**: Payloads extremadamente avanzados y de alto riesgo.
  
- **Menú de Selección**: Interfaz interactiva para seleccionar categoría y payload específico.
- **Generación de Archivos PHP**: Los payloads seleccionados se guardan automáticamente en el directorio actual.

---

## Instalación

### Requisitos
- **Python 3**: Asegúrate de tener Python 3 instalado en tu sistema.
- **Librerías**: La herramienta usa solo bibliotecas estándar, por lo que no se necesita instalación adicional.

### Instrucciones para instalacion

1. **Actualiza el sistema e instala Python 3**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 -y
   ```
2. **Clona el repositorio**:
   ```bash
   git clone https://github.com/TecnicosEnHacking/payload-generator
   cd payload-generator
   ```
3. **Ejecuta la herramienta**:
   ```bash
   python3 payload-generator.py
   ```

