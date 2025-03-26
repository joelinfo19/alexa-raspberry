# Configuración de Raspberry Pi para Control con Alexa

Este documento describe los pasos necesarios para configurar una Raspberry Pi con Flask y GPIO para recibir comandos de Alexa.

## Requisitos

- Raspberry Pi 4 o 5 con Raspberry Pi OS
- Python 3 instalado
- Conexión a internet
- Alexa configurado con el intent adecuado

## Instalación de Dependencias

Ejecuta los siguientes comandos en tu Raspberry Pi:

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-flask python3-libgpiod -y
```

Instala las dependencias de Python necesarias:

```sh
pip install flask gpiod
```



## Ejecutar el Servidor

Corre el siguiente comando para iniciar el servidor Flask:

```sh
python3 script_python.py
```

## Enviar una Solicitud de Prueba

Para probar el servidor, puedes usar `curl` o Postman con el siguiente JSON:

```sh
curl -X POST http://localhost:5000/alexa \
     -H "Content-Type: application/json" \
     -d '{
  "version": "1.0",
  "session": {
    "new": true,
    "sessionId": "amzn1.echo-api.session.1234567890",
    "application": {
      "applicationId": "amzn1.ask.skill.04537a1a-6234-4ced-b2fc-5c29bb36cf00"
    },
    "user": {
      "userId": "amzn1.ask.account.test-user-1234"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "amzn1.echo-api.request.9876543210",
    "timestamp": "2025-03-25T12:00:00Z",
    "locale": "es-ES",
    "intent": {
      "name": "ControlDispositivoIntent",
      "slots": {
        "action": {
          "name": "action",
          "value": "apaga"
        },
        "dispositivo": {
          "name": "dispositivo",
          "value": "ventilador"
        }
      },
      "confirmationStatus": "NONE"
    }
  }
}'
```

## Exponer el Servidor a Internet

Si deseas que Alexa pueda acceder a tu servidor, puedes usar `ngrok` o `Cloudflare Tunnel`:

```sh
ngrok http 5000
```

Esto generará una URL pública que puedes usar en la configuración de Alexa.

## Configuración en Alexa

- Configura un intent en Alexa con las frases adecuadas (Ej: "Alexa, enciende las luces").
- Apunta la URL del webhook al endpoint expuesto (`https://tu-ngrok-url/alexa`).
- Asegúrate de que el certificado HTTPS sea válido.

---
