
import Adafruit_DHT
import time

#time in seconds ==> Sample each 1 min
sampleFrecuencia = 1*60

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
DHTpin=17
 

# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.

def run():
    while True:
        temperature()
        time.sleep(sampleFrecuencia)

# get data of temperture and humidity

def temperture():
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHTpin)
        if humidity is not None and temperature is not None:
            print('Temperatura ={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')


if __name__ == "__main__":
    run()



