import eventlet
import json
from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = '10.42.0.1' 
app.config['MQTT_BROKER_PORT'] = '1883'
app.config['MQTT_KEEPALIVE'] = 5

mqtt_client = Mqtt()
socketio = SocketIO(app)

dataJson = {
    "topic": "chat",
    "payload": {
        "name": "Vini",
        "id": "xxxxxxx"
    }    
}

json_str = json.dumps(dataJson)

@app.route("/")
def index():
#    handle_publish(json_str);
    return {"Hello":"World"}

@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    print(data)
    mqtt_client.publish(data['topic'], data['payload'])

@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt_client.subscribe(data['topic'])

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt_client.unsubscribe_all()

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)

@mqtt_client.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)
