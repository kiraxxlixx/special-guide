#  TijuArte Urbano - Explorador de Murales

![Estado](https://img.shields.io/badge/Estado-Finalizado-success)
![Tecnología](https://img.shields.io/badge/Stack-Flask%20%7C%20Leaflet%20%7C%20Tailwind-blue)

**Una plataforma inmersiva para redescubrir la identidad visual de Tijuana a través de sus rutas artísticas.**

 **[VER APP EN VIVO](https://kirxllix.pythonanywhere.com)**

---

##  Cómo correrlo localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/kiraxxlixx/special-guide.git](https://github.com/kiraxxlixx/special-guide.git)
    cd special-guide/Act5
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
4.  Visita: `http://127.0.0.1:5000`

---

##  Stack Tecnológico

* **Backend:** Python + Flask (API REST simulada).
* **Frontend:** HTML5, Tailwind CSS (Diseño responsivo y animaciones).
* **Mapas:** Leaflet.js + OpenStreetMap (Con filtro Dark Mode CSS).
* **Iconos:** Lucide Icons.

---

##  Justificación de Diseño UX

Este proyecto integra las 5 actividades del laboratorio siguiendo principios de usabilidad:

1.  **Diseño Emocional (Landing Page):** Uso de paleta de colores neón (Cyberpunk/Urbano) y copywriting inspirador para conectar con el usuario joven/turista.
2.  **Ley de Fitts (Mapa):** Controles de navegación ubicados en la zona inferior para facilitar el uso con pulgares en móviles.
3.  **Visibilidad del Estado:** Feedback inmediato (Spinners y Toasts) al guardar marcadores, simulando latencia de red.
4.  **Accesibilidad:**
    * Sistema de **Pestañas (Tabs)** en móvil para separar la carga cognitiva de ver el Mapa vs. la Lista.
    * Etiquetas `aria-label` inyectadas dinámicamente en los controles de mapa.

---

##  Créditos IA

Código co-creado con **Gemini Canvas**.
* **Prompt Principal:** *"Crea una Landing Page HTML para una app de mapas llamada [NOMBRE]. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad."*

---
*Laboratorio de Mapas y UX - 2026*