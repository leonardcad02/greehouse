# Fletzi IoT – Greenhouse Monitor

Dashboard web para monitorear un invernadero (temperatura y humedad) desde una Raspberry Pi. Un script en la Pi lee un sensor DHT11 y guarda las lecturas en SQLite; una app Flask expone un dashboard con el último dato y gráficos históricos.

## Arquitectura

```
Sensor DHT11 (RPi) --> WebSite/temperture.py --> Database/sensorsData.db --> WebSite/WebService.py (Flask) --> Templates/index.html
```

- **`WebSite/temperture.py`** – corre en la Raspberry Pi. Lee el sensor DHT11 cada minuto (`Adafruit_DHT`, `RPi.GPIO`) e inserta cada lectura en la tabla `DHT_data` de `Database/sensorsData.db`.
- **`WebSite/distance.py`** – lee un sensor ultrasónico HC-SR04 por GPIO en la Pi. Actualmente solo imprime la distancia por consola; no está integrado a la base de datos ni al dashboard.
- **`WebSite/WebService.py`** – servidor Flask que sirve el dashboard: última lectura, gráficos históricos de temperatura/humedad (`matplotlib`) y un formulario para ajustar el rango de tiempo mostrado.
- **`WebSite/Templates/index.html`** – plantilla del dashboard.
- **`Database/sensorsData.db`** – base de datos SQLite con la tabla `DHT_data(timestamp, temperature, humidity)`.

`temperture.py` y `distance.py` requieren hardware de Raspberry Pi (`RPi.GPIO`, `Adafruit_DHT`) y solo se ejecutan en la Pi. `WebService.py` no depende de hardware y puede correr en cualquier máquina con acceso al archivo `.db`.

## Requisitos

- Python 3.11+
- Un entorno virtual (`.venv`)

## Instalación

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS/Raspberry Pi
source .venv/bin/activate

pip install -r Requirements.txt
```

## Uso

Levantar el dashboard localmente:

```bash
cd WebSite
python WebService.py
```

Abrir [http://127.0.0.1:5000](http://127.0.0.1:5000).

En la Raspberry Pi, además del servidor web, correr por separado (requiere `RPi.GPIO` y `Adafruit_DHT`, instalables solo en la Pi):

```bash
python WebSite/temperture.py
```

## Rutas del servidor

| Ruta          | Método | Descripción                                   |
|---------------|--------|------------------------------------------------|
| `/`           | GET    | Dashboard con la última lectura                |
| `/`           | POST   | Actualiza el rango de tiempo mostrado (`rangeTime`) |
| `/plot/temp`  | GET    | Gráfico PNG del histórico de temperatura        |
| `/plot/hum`   | GET    | Gráfico PNG del histórico de humedad            |

## Estado del proyecto

- El sensor de distancia (`distance.py`) no está conectado a la base de datos ni al dashboard todavía.
- No hay pruebas automatizadas.
