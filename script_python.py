from flask import Flask, request, jsonify
import gpiod
import os

app = Flask(__name__)

# Simulación si no hay Raspberry Pi
SIMULATE = "True"

if not SIMULATE:
    CHIP = "gpiochip4"  # Raspberry Pi 5
    PIN_VENTILADOR = 17
    PIN_LUZ = 27

    chip = gpiod.Chip(CHIP)
    ventilador = chip.get_line(PIN_VENTILADOR)
    luz = chip.get_line(PIN_LUZ)

    ventilador.request(consumer="ventilador", type=gpiod.LINE_REQ_DIR_OUT)
    luz.request(consumer="luz", type=gpiod.LINE_REQ_DIR_OUT)


@app.route('/alexa', methods=['POST'])
def alexa_control():
    data = request.json
    comando = data.get("request", {}).get("intent", {}).get("name", "").lower()  # Recibe el intent como string

    if comando == "enciende el ventilador":
        if not SIMULATE:
            ventilador.set_value(1)
        return jsonify({"respuesta": "El ventilador ha sido encendido"})

    elif comando == "apaga el ventilador":
        if not SIMULATE:
            ventilador.set_value(0)
        return jsonify({"respuesta": "El ventilador ha sido apagado"})

    elif comando == "enciende las luces":
        if not SIMULATE:
            luz.set_value(1)
        return jsonify({"respuesta": "Las luces han sido encendidas"})

    elif comando == "apaga las luces":
        if not SIMULATE:
            luz.set_value(0)
        return jsonify({"respuesta": "Las luces han sido apagadas"})

    return jsonify({"respuesta": "No entendí el comando"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
