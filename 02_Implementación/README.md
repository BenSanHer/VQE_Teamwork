# 02_implementación

## Propósito
Este espacio contiene las **implementaciones funcionales y limpias** del proyecto.

Aquí solo entra código que:
- funciona
- es claro
- puede explicarse completamente

---

## Estructura

Cada implementación debe indicar:

- Quién la desarrolló
- Qué experimento representa

```
nombre_persona/
└── nombre_experimento/
    ├── notebook.ipynb
    └── README.md
```

---

## Ejemplo

```
benjamin/
└── vqe_minimal/
    ├── vqe.ipynb
    └── README.md

ivan/
└── ansatz_test/
    ├── ansatz.ipynb
    └── README.md
```

---

## Contenido esperado

### notebook.ipynb
- Implementación completa
- Debe correr de inicio a fin
- Comentado y entendible

### README.md (dentro de cada experimento)
Debe explicar:
- Qué hace el experimento
- Qué se está probando
- Qué resultados se obtuvieron

---

## Flujo de trabajo

1. El trabajo inicia en `01_trabajo_individual`
2. Cuando algo funciona y se entiende:
   - se limpia
   - se documenta
   - se sube aquí

---

## Regla importante

No subir código aquí si:
- no se entiende completamente
- no corre
- no puede explicarse

---

## Objetivo

Construir implementaciones que:
- representen el aprendizaje real del equipo
- puedan presentarse
- sirvan como base para lo que sigue