# Bitácora de Diseño UX - Actividad 2: Lienzo del Mapa

## 1. Prompt Utilizado
> "Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de alto (o 'h-screen'). Inicializa el mapa centrado en TIJUANA con un tilelayer de OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de alcanzar."

## 2. Decisiones de UX (Ley de Fitts)
* **Ubicación del Zoom:** Moví los botones de zoom (+/-) a la esquina **inferior derecha**. Según la Ley de Fitts, esta zona es mucho más accesible para el dedo pulgar cuando se usa el teléfono con una sola mano, reduciendo el esfuerzo del usuario para navegar.
* **Densidad de Información:** Inicié el mapa con un zoom nivel 13 sobre la Zona Centro/Río de Tijuana para que el usuario vea calles principales de inmediato sin estar abrumado por demasiados marcadores iniciales.