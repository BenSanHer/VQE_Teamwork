# Contributing Guide

## Propósito
Este documento define las **reglas de trabajo del repositorio**, en particular cómo hacer commits de forma clara y ordenada.

El objetivo es mantener un historial limpio que refleje el proceso de aprendizaje y desarrollo.

---

## Estructura de commits

Formato obligatorio:

```
tipo: descripción corta
```

---

## Tipos de commit

- `feat` → nueva funcionalidad
- `fix` → corrección de errores
- `docs` → documentación
- `exp` → experimentos
- `refactor` → limpieza o mejora de código

---

## Ejemplos

```
docs: add week 01 objectives and scope
exp: test simple ansatz
feat: implement basic VQE loop
fix: correct expectation value calculation
refactor: clean notebook structure
```

---

## Convención por persona

Para mayor claridad, usar:

```
exp(nombre): descripción
```

Ejemplo:

```
exp(benjamin): test simple ansatz
exp(ivan): explore expectation value
exp(said): initial optimization test
```

---

## Flujo de trabajo

### 1. No trabajar en main

Cada integrante debe trabajar en su propia rama:

```
feature/nombre-descripcion
```

Ejemplo:

```
feature/benjamin-vqe
feature/ivan-ansatz
```

---

### 2. Commits frecuentes

- Hacer commits pequeños
- Un commit = una idea

---

### 3. Subir cambios regularmente

```
git push origin nombre-de-tu-rama
```

---

### 4. Integración

Cuando algo:
- funciona
- se entiende
- está limpio

puede integrarse a `main`.

---

## Buenas prácticas

- Mensajes claros y descriptivos
- Commits pequeños
- Subir avances de forma constante
- Separar exploración de implementación

---

## Qué NO hacer

- No usar mensajes como "cambios", "update", "final"
- No hacer commits gigantes
- No subir código que no entiendes
- No romper la rama principal (`main`)

---

## Regla de oro

> Un commit debe representar una idea clara.

---

## Objetivo

Construir un historial que permita:

- entender el proceso de aprendizaje
- rastrear decisiones
- identificar qué funcionó y qué no