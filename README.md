# 🚀 Astroflight: Enhanced Asteroids Clone

A feature-rich, high-performance **Asteroids** space arcade clone built from scratch using Python 3 and **Pygame**. This project demonstrates clean Object-Oriented Programming (OOP) architectures, customized 2D vector kinematics, asset rendering natively via vector primitives, and modular decoupled entity management via Pygame sprite tracking systems.

---

## 🕹️ Game Features Overview

### 🪐 Core Gameplay Archetype
* **Sprite Group Container Architecture:** Dynamically filters, updates, and draws decoupled object groups (`updatable`, `drawable`, `asteroids`, `shots`, and `particles`) synchronously without hardcoding indexes.
* **Pixel-Perfect Circular Hitboxes:** Scaled distance calculations compute accurate multi-element intersection conditions smoothly across arbitrary coordinate variations.

### 🔥 Advanced Features Supported
* **Vector Acceleration & Momentum:** The player ship features physics modeling utilizing continuous forward vectors combined with a decaying friction coefficient to mimic spatial weight and drift mechanics.
* **Dynamic Asteroid Splitting:** Large drifting obstacles dynamically split into smaller, accelerated target configurations when intercepted by ammunition elements.
* **Radial Particle Explosion Effects:** Vaporized objects erupt into complex fading particle shards that trace expansion drift lines across the spatial framework.
* **Adaptive Scoring HUD Interface:** High-contrast text layout gauges destruction yields directly by rewarding bonus weighting to hits on high-velocity smaller asteroid sizes.
* **Multi-Life Respawning System:** Players run a structural configuration tracking remaining hulls alongside full visual blinking invulnerability timers to ensure clean recovery states.

---

## 🛠️ Controls Reference

| Input Key | Core System Mapping / Action |
| :---: | --- |
| <kbd>W</kbd> | Accelerate Ship Forward (Adds to velocity Vector) |
| <kbd>S</kbd> | Accelerate Ship Backward / Reverse Thrusters |
| <kbd>A</kbd> | Rotate Ship Counter-Clockwise |
| <kbd>D</kbd> | Rotate Ship Clockwise |
| <kbd>Spacebar</kbd> | Fire Laser (Rate-limited via Cooldown Timers) |

---

## 📁 Codebase Layout

```text
├── constants.py       # Centralized engine configurations & metrics
├── circleshape.py     # Base abstract class for generic circular physics
├── player.py          # Player kinematics, acceleration, & state logic
├── asteroid.py        # Obstacle geometry management & division behaviors
├── asteroidfield.py   # Automated runtime margin spawner algorithms
├── shot.py            # Active structural weapon projection element
├── particle.py        # Vector shard visual explosion systems
├── logger.py          # Debug telemetry engine tracking tools
└── main.py            # Primary runtime event orchestrator loop
```

---

## ⚡ Setup & Run Instructions

### 📥 Prerequisites
Ensure you have Python 3.10+ and the modern fast Python package manager **`uv`** installed on your workstation environment.

### 🚀 Running the Game
1. Clone this repository to your local path directory.
2. Initialize and spin up the runtime engine directly using the following execution instruction:

```bash
uv run main.py
```

### 🧪 Automated Tests Verification
To verify code modifications against the telemetry log test configurations, use your integrated grading framework suite:

```bash
# Clear historical telemetry log cycles
rm game_state.jsonl
```
