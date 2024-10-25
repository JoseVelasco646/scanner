# Network Scanner con Flask y Nmap

Este proyecto es una aplicación web construida con Flask que permite escanear una red local para detectar dispositivos activos. Utiliza `nmap` para identificar dispositivos y `ping` para verificar su disponibilidad. La información de los dispositivos escaneados se muestra en una página web.

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

- Python 3.7 o superior
- Flask
- nmap
- Subprocess (incluido en Python)
- Un entorno de red local para probar el escaneo

Para instalar las dependencias de Python:

```bash
pip pip install python-nmap
```

Una vez descargado todo procedemos a obtener nuestra ip que vamos a escanear con el siguiente comando:  
Esto lo ponemos en la terminal para obtener nuestra direccion ip que usaremos para escanear

```bash
ip route | grep default
```

Nos dara una direccion ip en este caso es `192.168.0.0`.  
Ahora nos iremos a nuestro programa y cambiamos el valor de nuestra variable `network_to_scan` y le agregamos la direccion que obtuvimos `192.168.0.1/24` y le agregamos que muestre las direccion ip en el rango 24 que nmap escaneará.
