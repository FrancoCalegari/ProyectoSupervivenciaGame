# 🧟 Proyecto: SupervivenciaGame (Nombre Provisional)

Bienvenido/a al repositorio oficial de **SupervivenciaGame**. Este documento sirve como guía de inducción y mapa de ruta (*roadmap*) inicial para que los pasantes y desarrolladores puedan integrarse rápidamente al proyecto y comenzar con las tareas de desarrollo.

---

## 📌 Contexto del Proyecto

> **Minuta de arranque / Kickoff:**  
> Proyecto iniciado tras la reunión de planificación con **Fabricio Lameiro**, donde se definieron el alcance técnico inicial, la visión del producto y las bases del desarrollo.

El objetivo del proyecto es construir un **videojuego web de supervivencia contra oleadas de zombies** ejecutado directamente en el navegador, con alto rendimiento, baja latencia y compatibilidad multiplataforma (escritorio y dispositivos móviles).

---

## 🛠️ Stack Tecnológico

El proyecto prescinde de motores pesados de terceros para aprovechar al máximo las APIs nativas de la web y garantizar una comprensión profunda de la arquitectura de motores de juegos:

| Tecnología | Propósito |
| :--- | :--- |
| **WebGL** | API gráfica para aceleración por hardware de renderizado 2D/3D mediante la GPU, garantizando altas tasas de cuadros por segundo (FPS). |
| **Web Audio API (`AudioContext`)** | Síntesis, reproducción, mezcla espacial y manipulación de efectos de sonido (SFX) y música interactiva en tiempo real. |
| **HTML5, CSS3, JavaScript (ES6+)** | Estructura, interfaz de usuario (HUD/UI) y lógica del cliente. |
| **Node.js & Express** | Servidor web para entrega de assets estáticos y soporte para backend/servicios futuros. |
| **Gamepad API & Touch API** | Entrada de controles multiplataforma: soporte nativo para mandos (gamepads), pantallas táctiles móviles, teclado y ratón. |

---

## 📋 Áreas Pendientes de Definición y Diseño

El equipo debe participar activamente en la propuesta y construcción de:

- [ ] **Mecánicas:** Reglas de interacción, progresión de dificultad, recarga, esquivas, crafteo.
- [ ] **Lógica del Juego:** Estados de partida (menú, juego activo, pausa, game over), bucle principal del juego (*game loop* con `requestAnimationFrame`), cálculo de físicas y colisiones.
- [ ] **Historia y Lore:** Ambientación, origen del brote zombi, contexto de los personajes y narrativa ambiental.
- [ ] **FX (Efectos, Partículas y Experiencia de Usuario):** Sangre, casquillos de bala, fogonazos de disparo, iluminación ambiental, sacudida de cámara (*screen shake*) y feedback háptico/sonoro.
- [ ] **Nombre Definitivo del Juego:** Torbellino de ideas para el título comercial final del proyecto.

---

## 🗺️ Hoja de Ruta Inicial: ¿Por dónde empezamos?

Nuestra prioridad es construir **la base técnica y las herramientas esenciales** antes de pasar a mecánicas complejas o contenido artístico final.

### Fase 1: Entorno y Visualizador Principal
- [ ] Configuración del servidor base con **Node.js** y **Express**.
- [ ] Creación del lienzo principal (`<canvas>`) e inicialización del contexto **WebGL**.
- [ ] Implementación del bucle principal de render y actualización (*Game Loop* delta-time).
- [ ] Dibujado del entorno base: obstáculos, paredes y límites perimetrales del mapa inicial.

### Fase 2: Control y Movimiento del Jugador
- [ ] Detección de entradas por Teclado/Mouse, Gamepad API y Touch API.
- [ ] Mecánicas básicas de movimiento del personaje (aceleración, fricción, rotación hacia el cursor/mando).
- [ ] Detección de colisiones contra paredes y obstáculos.

### Fase 3: Combate Básico y Supervivencia
- [ ] Mecánica de disparo: proyectiles, trayectoria, cadencia y consumo de munición.
- [ ] Spawner básico de enemigos (generación periódica por oleadas o puntos fijos).
- [ ] IA básica para enemigos (algoritmo de persecución directa hacia el jugador y evasión simple de obstáculos).
- [ ] Sistema de atributos del jugador:
  - **Vida (HP)**
  - **Escudo**
  - **Energía / Stamina**
  - **Sistema de Supervivencia: Hambre y Sed**

### Fase 4: Gestión de Recursos
- [ ] Sistema de inventario básico (almacenamiento de ítems, armas, municiones y consumibles médicos/comida).
- [ ] Interfaz gráfica (HUD) integrada para visualizar estadísticas vitales e inventario.

---

## 📂 Estructura de Proyecto Sugerida

```text
ProyectoSupervivenciaGame/
├── public/
│   ├── assets/
│   │   ├── audio/        # Efectos de sonido y pistas musicales
│   │   ├── textures/     # Texturas, sprites y atlas gráficos
│   │   └── shaders/      # Shaders GLSL (vertex y fragment shaders)
│   ├── css/
│   │   └── style.css     # Estilos de la UI y HUD
│   ├── js/
│   │   ├── core/         # Game loop, input manager, engine WebGL
│   │   ├── entities/     # Player, Enemy, Bullet, Obstacle
│   │   ├── systems/      # Audio, colisiones, supervivencia, inventario
│   │   └── main.js       # Punto de entrada de la aplicación cliente
│   └── index.html        # Página principal contenedora del canvas
├── server/
│   └── app.js            # Servidor Express para servir el proyecto
├── package.json
└── README.md
```

---

## 🚀 Guía de Primeros Pasos para Pasantes

1. **Clonar e inicializar el entorno:**
   ```bash
   git clone <url-del-repositorio>
   cd ProyectoSupervivenciaGame
   npm init -y
   npm install express
   ```

2. **Crear una rama para tu tarea:**
   ```bash
   git checkout -b feature/nombre-de-la-funcionalidad
   ```

3. **Convenciones de código:**
   - Escribir código modular y desacoplado (separar lógica de render de la lógica de entidades).
   - Documentar funciones y clases clave usando comentarios descriptivos o JSDoc.
   - Realizar commits descriptivos (`feat:`, `fix:`, `docs:`, `refactor:`).

4. **Dudas o consultas:**
   - Coordinar dudas técnicas y avances con el equipo y con **Fabricio Lameiro**.
