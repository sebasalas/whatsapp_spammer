import webbrowser
import time
import pyautogui

# El número de teléfono al que se enviarán los mensajes
numero_telefono = '+1234567890'  # Reemplazar con el número de teléfono objetivo
mensaje = 'Tu mensaje aquí'  # Reemplazar con tu mensaje

# Abrir la URL de WhatsApp Web una vez
url = f'https://web.whatsapp.com/send?phone={numero_telefono}'
webbrowser.open(url)

# Función para enviar un mensaje
def enviar_mensaje_whatsapp():
    # Escribir el mensaje
    pyautogui.typewrite(mensaje)
    # Presionar Enter para enviar el mensaje
    pyautogui.press('enter')

# Bucle principal para enviar el mensaje cada 5 segundos
while True:
    enviar_mensaje_whatsapp()
    time.sleep(5)  # Esperar 5 segundos antes de enviar el siguiente mensaje
