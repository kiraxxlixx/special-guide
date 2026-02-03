# Bitácora de Diseño UX - Actividad 4: Accesibilidad y Sincronización

## 1. Prompt / Requerimiento
> "Modifica la interfaz para tener dos columnas (o pestañas en móvil): 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como un texto descriptivo en la sección de Lista (ej. 'Punto en Lat: X, Long: Y'). Asegúrate de que los botones del mapa tengan atributos 'aria-label' como 'Acercar mapa' o 'Alejar mapa'."


## 2. Decisiones de Diseño y UX

### A. Estrategia Mobile-First (Pestañas de Navegación)
**Problema:** En pantallas pequeñas, tener el mapa encima y la lista debajo dificultaba la navegación (el usuario tenía que hacer mucho scroll para ver la lista).
**Solución:** Se implementó un control de pestañas (`switchTab`) exclusivo para móviles.
* **Justificación:** Reduce la carga cognitiva al permitir que el usuario se enfoque en una sola tarea a la vez: **Explorar** (Mapa) o **Consultar** (Lista). Además, al hacer clic en un ítem de la lista en modo móvil, la app cambia automáticamente a la pestaña del mapa para mostrar el lugar.

### B. Accesibilidad (A11y) y Etiquetas ARIA
**Problema:** Los controles nativos de Leaflet (Zoom + / -) no traen etiquetas accesibles por defecto, lo que confunde a los lectores de pantalla.
**Solución:** Inyecté atributos `aria-label` mediante JavaScript (`zoomInBtn.setAttribute...`).
* **Justificación:** Ahora un lector de pantalla anunciará claramente "Acercar mapa" o "Alejar mapa" en lugar de simplemente decir "Botón". También mejoré el contraste de los textos (Slate-800 sobre blanco).

### C. Heurística: Control y Libertad del Usuario
**Implementación:** Agregué un botón flotante con icono de "Diana" (🎯) en la esquina superior derecha del mapa.
**Justificación:** Los usuarios a menudo se pierden haciendo *panning* (moviendo el mapa) lejos de la ciudad. Este botón permite **"Resetear la vista"** (`resetMapView`) para volver al centro de Tijuana inmediatamente, funcionando como una "salida de emergencia" visual.

### D. Sincronización Bidireccional (Feedback Visual)
El sistema mantiene el estado compartido entre el Mapa y la Lista usando un registro central (`markersRegistry`).
1.  **Crear:** Al guardar un punto, aparece en la lista con una animación `slideIn` y borde azul.
2.  **Borrar:** Al eliminar desde la lista, el marcador desaparece del mapa en tiempo real.
3.  **Navegar:** Al hacer clic en la lista, el mapa realiza una animación de vuelo suave (`flyTo`) hacia el destino.