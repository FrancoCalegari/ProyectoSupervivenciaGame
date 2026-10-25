# 🧟 SupervivenciaGame

## Documento de Arquitectura

### Versión
v0.1.0

---

# 1. Visión General

SupervivenciaGame es un videojuego web de supervivencia ambientado en un mundo postapocalíptico con amenazas zombies.

El proyecto busca funcionar directamente desde navegador con compatibilidad para PC y dispositivos móviles.

La arquitectura está diseñada para ser modular y permitir futuras expansiones.

---

# 2. Arquitectura General

El videojuego estará dividido en módulos independientes:

## Motor del Juego

Responsable de:

- Game Loop
- Renderizado
- Actualización de estados
- Gestión del tiempo
- Física básica

---

## Entidades

Elementos que existen dentro del mundo:

- Jugador
- Zombies
- NPC
- Objetos
- Vehículos
- Construcciones

---

## Sistemas

Módulos encargados de las mecánicas:

- Movimiento
- Combate
- Inventario
- Supervivencia
- IA
- Misiones
- Guardado

---

## Mundo

Representa el entorno donde ocurre la supervivencia:

- Mapas
- Zonas explorables
- Recursos
- Eventos dinámicos
- Clima

---

## Servidor

Tecnología:

- Node.js
- Express

Funciones:

- Servir archivos del juego
- Preparar servicios futuros
- Gestionar comunicación online

---

# 3. Objetivo de la versión v0.1.0

Crear la base técnica del videojuego:

- Estructura del proyecto
- Primer mapa
- Sistema básico de jugador
- Preparación del motor
- Base para futuras mecánicas

---

# 4. Principios del Proyecto

- Código modular
- Versiones actualizables
- Separación de sistemas
- Documentación constante
- Compatibilidad multiplataforma

