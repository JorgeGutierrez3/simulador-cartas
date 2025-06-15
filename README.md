# Simulador-cartas
Una libreria que simula el juego de cartas tradicional Póker. 

## Características

### Cartas
Las cartas tienen tres atributos principales, su palo, su número y el valor real de su número, ejemplo: Q --> 12, K --> 13.  

### Funciones básicas
- Crear Cartas.
- Crear Bajara.
- Evaluar Mano.

## Estructura del Proyecto

```
simulador-cartas/
├── src/
│   └── cartas/
│       ├── crear_baraja.py
│       ├── crear_cartas.py
│       └── evaluar_mano.py
├── setup.py
└── README.md
```

## Uso

### Calculadora Básica
```python
from calculadora import CalculadoraBasica

# Crear una instancia de la calculadora básica
calc_basica = CalculadoraBasica()

# Realizar operaciones
resultado = calc_basica.sumar(5, 3)  # Retorna 8
resultado = calc_basica.restar(10, 4)  # Retorna 6
resultado = calc_basica.multiplicar(2, 3)  # Retorna 6
resultado = calc_basica.dividir(10, 2)  # Retorna 5.0
```

### Calculadora Trigonométrica
```python
from calculadora import CalculadoraTrigonometrica
import math

# Crear una instancia de la calculadora trigonométrica
calc_trig = CalculadoraTrigonometrica()

# Realizar operaciones trigonométricas
resultado = calc_trig.seno(math.pi/2)  # Retorna 1.0
resultado = calc_trig.coseno(0)  # Retorna 1.0
resultado = calc_trig.tangente(math.pi/4)  # Retorna 1.0

# Convertir entre grados y radianes
radianes = calc_trig.grados_a_radianes(180)  # Retorna π
grados = calc_trig.radianes_a_grados(math.pi)  # Retorna 180.0
```

## Desarrollo

1. Clona este repositorio

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e simulador-cartas
   ```
