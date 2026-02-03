# Bitácora de Diseño UX - Actividad 5: Integración Final y Coherencia Visual

## 1. El Reto de Integración
> **Situación:** Teníamos dos componentes funcionales pero visualmente desconectados: una Landing Page con estética "Cyberpunk/Nocturna" (Act1) y un Mapa interactivo con estética "Oficina/Diurna" (Act4).
> **Problema UX:** Al navegar de la portada al mapa, el cambio brusco de luminosidad (de fondo negro a blanco brillante) generaba fatiga visual y rompía la inmersión de la marca "TijuArte".

## 2. Decisiones de Diseño (Iteración Final)

### A. Unificación de Tema (Dark Mode Total)
Para mantener la consistencia de la marca, migré la interfaz del mapa a un esquema de colores oscuros.
* **Mapa Base:** Reemplacé `OpenStreetMap` (Standard) por **CartoDB Dark Matter**.
    * *Justificación:* Los mapas oscuros hacen resaltar mejor los marcadores de colores (Cyan/Fuchsia) y reducen el consumo de batería en dispositivos móviles OLED.
* **UI Kit:** Actualicé todos los contenedores de `bg-white` a `bg-slate-900` y `bg-slate-800` usando Tailwind CSS, alineando la paleta con la Landing Page.

### B. Mejora de Heurística: Control y Libertad del Usuario
Detecté que guardar todos los puntos con el nombre genérico "Punto Personalizado" limitaba la utilidad de la app.
* **Solución:** Rediseñé el Popup de creación para incluir un **Input de Texto**.
* **Resultado:** Ahora el usuario puede nombrar sus hallazgos (ej. "Mural de la calle 6ta"), lo que aumenta el valor emocional y personal de la lista guardada.

### C. Feedback del Sistema y Affordance
Mejoré el diseño del Popup de confirmación.
* **Antes:** Se veía apretado y poco legible.
* **Ahora:** Aumenté el *padding*, mejoré el contraste de los botones (Cyan para acción primaria, Gris para cancelar) y usé bordes redondeados para invitar a la interacción (*Affordance*).

### D. Optimización de Conversión (CTA Principal)
Apliqué el principio de **Jerarquía Visual** en la pantalla principal (Hero Section).
* **Cambio:** Eliminé el botón secundario ("Ver Demo") que competía visualmente.
* **Justificación:** Al reducir las opciones (Ley de Hick), dirigimos toda la atención del usuario hacia la acción principal: **"Explorar Mapa"**. Esto mejora la tasa de clics y evita la parálisis por análisis.

### E. Conexión Externa y Realismo
Para que el prototipo se sienta como un producto real en el mercado, actualicé el pie de página (Footer).
* **Implementación:** Agregué enlaces funcionales (`<a>`) a **Apple App Store**, **Google Play Store** y perfil de **Instagram**.
* **Objetivo:** Aumentar la credibilidad del proyecto mediante elementos de confianza reconocibles por el usuario.

---

## 3. Conclusión Técnica
La Actividad 5 no fue solo "copiar y pegar"; fue un proceso de **refinamiento estético y funcional**. El producto final se siente como una sola aplicación nativa y coherente, lista para producción.