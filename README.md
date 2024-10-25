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
Esto lo ponemos en la terminal y lo ejecutamos con sudo (-sn es para que nos muestre las direccion ip sin puertos).

```bash
sudo nmap -sn 192.168.0.1/24
```
