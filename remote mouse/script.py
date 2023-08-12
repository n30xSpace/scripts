import socket
import pyautogui

# Obtener la dirección IP de la máquina local
host = socket.gethostbyname(socket.gethostname())
port = 9999

# Crear un objeto de socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar al servidor
    s.connect((host, port))
    print("Conexión exitosa con el servidor.")

    # Esperar a recibir datos del servidor
    while True:
        data = s.recv(1024).decode()

        # Si no hay datos, salir del bucle
        if not data:
            break

        # Analizar los datos recibidos y mover el mouse
        x, y = map(int, data.split(','))
        pyautogui.moveTo(x, y)

except ConnectionRefusedError:
    print("Error: No se pudo establecer conexión con el servidor.")
except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar la conexión
    s.close()
    print("Conexión cerrada.")