# 🧟 SupervivenciaGame

## Documento de Arquitectura

### Versión
v0.1.1

---

# 1. Visión General

SupervivenciaGame es un videojuego web de supervivencia ambientado en un mundo postapocalíptico con amenazas zombies.

El proyecto busca funcionar directamente desde navegador con compatibilidad para PC y dispositivos móviles.

La arquitectura está diseñada para ser modular y permitir futuras expansiones.

---

# 2. Arquitectura General

El videojuego estará dividido en módulos independientes:

---

# Motor del Juego

Responsable de:

- Game Loop principal
- Renderizado gráfico
- Actualización de estados
- Gestión del tiempo
- Física básica
- Comunicación entre sistemas

---

# Entidades

Elementos que existen dentro del mundo:

- Jugador
- Zombies
- NPC
- Objetos
- Vehículos
- Construcciones
- Recursos del mundo

---

# Sistemas

Módulos encargados de las mecánicas principales:

- Movimiento
- Combate
- Inventario
- Supervivencia
- Misiones
- Guardado de partidas
- Progresión del jugador
- Gestión de recursos

---

# Inteligencia Artificial

Responsable de los comportamientos inteligentes del mundo:

- Comportamiento de zombies
- Persecución del jugador
- Reacción al sonido y estímulos
- Comportamiento de NPC
- Decisiones dinámicas de enemigos y supervivientes
- Eventos generados por inteligencia artificial

---

# Mundo

Representa el entorno donde ocurre la supervivencia:

- Mapas
- Zonas explorables
- Recursos
- Eventos dinámicos
- Clima
- Ciclo día y noche
- Lugares abandonados

---

# Servidor

Tecnología:

- Node.js
- Express

Funciones:

- Servir archivos del videojuego
- Gestionar recursos del proyecto
- Preparar servicios futuros
- Permitir comunicación online

---

# 3. Objetivo de la versión v0.1.1

Mejorar la organización inicial del proyecto:

- Arquitectura definida
- Sistemas separados
- Base preparada para desarrollo
- Inteligencia artificial planificada
- Documentación inicial completa

---

# 4. Principios del Proyecto

El desarrollo seguirá estos principios:

- Código modular
- Versiones actualizables
- Separación de sistemas
- Documentación constante
- Compatibilidad multiplataforma
- Escalabilidad futura
- Organización profesional del proyecto

---

# 5. Estructura General del Proyecto

```text
SupervivenciaGame/

├── engine/
│   ├── core/
│   ├── physics/
│   └── audio/
│
├── gameplay/
│   ├── combate/
│   ├── supervivencia/
│   ├── inventario/
│   └── progreso/
│
├── entities/
│   ├── jugador/
│   ├── npc/
│   ├── zombies/
│   ├── objetos/
│   └── vehiculos/
│
├── ia/
│   ├── enemigos/
│   ├── npc/
│   └── comportamientos/
│
├── world/
│   ├── mapas/
│   ├── zonas/
│   ├── clima/
│   └── eventos/
│
├── ui/
│
├── assets/
│
├── server/
│
└── docs/
