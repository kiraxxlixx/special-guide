# Bitácora de Diseño UX - Actividad 3: Micro-interacciones y Feedback

## 1. Prompt Utilizado
> "Escribe un script en JS para Leaflet. Cuando el usuario haga clic en el mapa: 1. Ponga un marcador temporal inmediatamente. 2. Abra un popup que pregunte '¿Guardar este punto?'. 3. Al confirmar, envíe las coordenadas (lat, long) a un endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de 'Guardando...' mientras se procesa."

## 2. Decisiones de UX (Estados del Sistema)
Para cumplir con la heurística de "Visibilidad del estado del sistema", implementé tres estados visuales claros durante la interacción de guardar un punto:

### A. Prevención de Errores (Marcador Temporal)
En lugar de guardar el punto inmediatamente al hacer clic, decidí poner un **marcador temporal** (color azul por defecto) con un Popup de confirmación.
* **Justificación:** Esto evita que el usuario guarde puntos por error si su dedo resbala en la pantalla (muy común en móviles). El botón "Cancelar" permite corregir el error sin consecuencias.

### B. Estado de Carga (Latency Feedback)
Cuando el usuario confirma, el servidor tarda 1 segundo artificialmente (simulado con `time.sleep` en Python).
* **Solución Visual:** Despliego un **Toast** (notificación inferior) con un **spinner giratorio** y el texto "Guardando ubicación...".
* **Justificación:** Si no mostramos esto, el usuario podría pensar que la app se trabó y haría clic muchas veces. El spinner le dice "estoy trabajando, espera".

### C. Estado de Éxito/Error
* **Éxito:** El Toast cambia a un mensaje verde con un "Check" ✅ ("Punto guardado exitosamente") y desaparece automáticamente después de 3 segundos.
* **Robustez:** Si el servidor falla (error de red), el sistema lo atrapa (`.catch` en JS) y muestra una alerta visual para que el usuario no se quede esperando eternamente.