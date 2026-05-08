# 🧹 deduper — Servicio de deduplicación para suite-media

`deduper` es un servicio independiente dentro de la suite **suite-media**, diseñado para
detectar ficheros duplicados dentro de una carpeta concreta y moverlos a un directorio
centralizado de revisión manual.

Este servicio sigue una **arquitectura limpia**, separando dominio, aplicación e
infraestructura, y está preparado para crecer hacia funcionalidades más avanzadas
(indexado global, base de datos, políticas de deduplicación, API, etc.).

---

## ✨ Características

- Detección de duplicados mediante **hash perceptual (dHash)**.
- Procesamiento de **una carpeta concreta** (ideal para limpieza manual por meses/años).
- Movimiento automático de duplicados a un directorio configurable (`duplicates/`).
- Logs claros y legibles.
- Servicio completamente independiente, ejecutable desde CLI o Docker.
- Estructura modular y extensible.

---

## 📁 Estructura del proyecto


---

## 🚀 Instalación con Poetry

Dentro del directorio `deduper`:

```bash
poetry install
