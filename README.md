
# WhatsApp Spammer

Este script automatiza el envío de mensajes a un contacto específico de WhatsApp a intervalos regulares utilizando WhatsApp Web.

## Requisitos

- Python 3.x
- Biblioteca `pyautogui`
- Un navegador web

## Instalación

1. Instalar la biblioteca requerida:

```bash
pip install pyautogui
```

2. Asegúrate de tener un navegador web instalado (Chrome, Firefox, etc.).

## Uso

1. Abre el script `whatsapp_spammer.py` en tu editor de texto preferido.
    
2. Reemplaza las siguientes variables con tus valores deseados:

    - `numero_telefono`: El número de teléfono del destinatario en formato internacional (por ejemplo, `+1234567890`).
    - `mensaje`: El mensaje que deseas enviar.

 3. Ejecuta el script:

```bash
python whatsapp_spammer.py
```

## Explicación del Script

El script realiza las siguientes acciones:

1. Abre WhatsApp Web con el número de teléfono especificado.
2. Envía el mensaje especificado al contacto cada 5 segundos.

## Descargo de Responsabilidad

- Este script es solo para fines educativos. Úsalo de manera responsable.
- Sé consciente de los términos de servicio de WhatsApp y evita el uso indebido.
