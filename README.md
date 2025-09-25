# Proyecto Biblioteca – Pruebas de Integración Top-Down

Este repositorio contiene la implementación de un sistema de **gestión de biblioteca** y su estrategia de pruebas aplicando el enfoque **Top-Down**, utilizando **stubs** para simular módulos aún no implementados.

---

## 📌 Descripción del Proyecto
El sistema de Biblioteca permite gestionar préstamos de libros, validando la disponibilidad y la autorización de los usuarios.  
El desarrollo de las pruebas se realizó aplicando la estrategia de integración **Top-Down**, donde se comenzó desde los módulos principales y se usaron **stubs** para representar las funcionalidades aún no desarrolladas.

Se aplicó el enfoque **Top-Down** porque:
- Permite validar primero los **casos de uso principales** (ej. préstamo de libros).
- Los **stubs** ayudan a simular respuestas de módulos incompletos.
- Se puede comprobar el flujo general del sistema antes de tener todos los componentes reales.

---

## ⚙️ Tecnologías Utilizadas
- **Python 3.13**
- **Pytest** para pruebas unitarias e integración
- **Markdown** para documentación
- **Stubs** como sustitutos temporales de módulos

---

## 🚀 Ejecución de Pruebas
### Pruebas de Integración Top-Down

python -m pytest test_top_down.py -v
📸 Evidencia:
<img width="1622" height="318" alt="prueba test lisandro" src="https://github.com/user-attachments/assets/899916fa-29e6-411a-8f17-d20d067f3c92" />

📊 Resultados Obtenidos
Durante la ejecución de pruebas se validaron tres escenarios principales:

✅ Préstamo exitoso
El usuario tiene permisos y el libro está disponible.

✅ Usuario no autorizado
El sistema impide el préstamo cuando el usuario no tiene permisos.

✅ Libro no disponible
El sistema rechaza el préstamo si el libro ya está ocupado.


✅ Conclusiones
El enfoque Top-Down permitió verificar primero los flujos de alto nivel.

Los stubs facilitaron simular módulos faltantes sin frenar las pruebas.


Se confirmaron los tres escenarios críticos: préstamo válido, usuario no autorizado y libro no disponible.

La estrategia permitió obtener retroalimentación temprana del sistema, incluso sin todos los módulos implementados.
```
