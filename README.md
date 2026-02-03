# Explorador de Tijuana - Proyecto Final UX 🗺️

![Estado](https://img.shields.io/badge/Estado-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)

**Una aplicación web interactiva diseñada para redescubrir Tijuana a través de rutas culturales, optimizada para accesibilidad y dispositivos móviles.**

🔗 **[VER DEMO EN VIVO AQUÍ](https://TU_USUARIO.pythonanywhere.com)**

---

## 🚀 Cómo correrlo localmente

Si quieres probar este proyecto en tu computadora:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/kiraxxlixx/special-guide.git](https://github.com/kiraxxlixx/special-guide.git)
    cd special-guide/Act5
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar el servidor:**
    ```bash
    python app.py
    ```
4.  Abrir en el navegador: `http://127.0.0.1:5000`

---

## 🛠️ Stack Tecnológico

* **Backend:** Python + Flask (API REST para gestión de puntos).
* **Frontend:** HTML5 Semántico + Tailwind CSS.
* **Mapas:** Leaflet.js + OpenStreetMap.
* **Persistencia:** Simulación de base de datos en memoria (Estructuras de datos en Python).

---

## 🎨 Justificación de Diseño UX

Este proyecto fue construido iterativamente siguiendo principios de **Diseño Centrado en el Usuario (UCD)**:

1.  **Ley de Fitts (Móvil):** Los controles de zoom y navegación se ubicaron en la zona inferior derecha ("Thumb Zone") para facilitar el uso con una sola mano.
2.  **Visibilidad del Estado:** Se implementaron "Toasts" (notificaciones) y Spinners de carga para dar feedback inmediato al usuario cuando guarda un punto (Latencia simulada).
3.  **Accesibilidad (WCAG):**
    * Uso de atributos `aria-label` en controles de mapa.
    * Sistema de **Pestañas (Tabs)** en móvil para evitar el scroll infinito y separar la vista de Mapa y Lista.
    * Contraste de color optimizado (Slate-800 sobre blanco).
4.  **Prevención de Errores:** Confirmación en dos pasos antes de guardar un marcador.

---

## 🤖 Créditos a la IA

Este código fue co-creado con la asistencia de **Gemini Canvas**.
* **Prompt Principal:** *"Crea una Landing Page HTML para una app de mapas llamada [NOMBRE]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad."*
* **Rol de la IA:** Generación de boilerplate, lógica de JavaScript para Leaflet y redacción de documentación técnica.
* **Rol del Humano:** Arquitectura de información, validación de UX, pruebas de accesibilidad y ensamblaje final en Flask.

---

*Proyecto desarrollado para la materia de Laboratorio de Mapas y UX - 2026*