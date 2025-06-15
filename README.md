# Simulador de Cartas – Póker

Una librería en Python que simula el tradicional juego de cartas **Póker**. Permite crear cartas, barajas y evaluar manos de forma sencilla y extensible.

## Características

- Generación de cartas con palo, valor y nombre.
- Creación y mezcla de una o más barajas.
- Evaluación de manos de Póker (escalera, color, par, etc.).
- Fácil de integrar y personalizar.

## Estructura del Proyecto

```
simulador-cartas/
├── src/
│   └── cartas/
│       ├── crear_baraja.py       # Lógica para crear y manejar barajas
│       ├── crear_cartas.py       # Definición de cartas individuales
│       └── evaluar_mano.py       # Análisis de manos de Póker
├── main.py                       # Ejemplo de ejecución
├── setup.py                      # Configuración del paquete
└── README.md
```

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/JorgeGutierrez3/simulador-cartas.git
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala la librería en modo desarrollo:**
   ```bash
   pip install -e simulador-cartas
   ```

##  Uso

###  Crear una carta
```python
from cartas import Carta

carta = Carta()
print(carta)
```

###  Crear y usar una baraja
```python
from cartas import Baraja

baraja = Baraja(num_barajas=2)  # Crear 2 barajas
baraja.barajar()                # Mezclar las cartas
mano = baraja.repartir(5)       # Repartir 5 cartas
```

### Analizar una mano
```python
from cartas import Analizar

mano = baraja.repartir(5)
resultado = Analizar(mano)
print(f"Resultado: {resultado}")  # Devuelve el tipo de mano (ej. par, full house, etc.)
```

## Ejemplo completo de una mano de Póker

```python
from cartas import Baraja, Analizar

def main():
    baraja = Baraja(num_barajas=1)
    baraja.barajar()
    mano = baraja.repartir(5)
    resultado = Analizar(mano)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
```