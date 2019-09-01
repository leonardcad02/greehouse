from flask import Flask , render_template
import datetime
import temperture
app = Flask(__name__)

@app.route('/')

def hello_world():
    now = datetime.datetime.now()
    timestring = now.strftime("%c")
    temp = temperture.temperture
    hum = temperture.humidity
    temmplateData = {
        'title': 'Hello',
        'time': timestring,
        'temperature': temp,
        'humidity': hum 
    }
    return render_template ('index.html', ** temmplateData)

if __name__ == "__main__":
    app.run()