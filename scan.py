from flask import Flask, render_template
import nmap
import subprocess

app = Flask(__name__)

def ping_device(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return True 
    except subprocess.CalledProcessError:
        return False  

@app.route('/')
def index():
    network_to_scan = '40.10.7.254/21'  
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=network_to_scan, arguments='-sn')
    
 
    active_devices = []
    for host in scan_result['scan']:
        mac_address = scan_result['scan'][host]['addresses'].get('mac', None)
        if mac_address: 
            active_devices.append({
                'ip': host,
                'active': ping_device(host)  
            })
    
    return render_template('index.html', devices=active_devices, scan_result=network_to_scan)

if __name__ == '__main__':
    app.run(debug=True)
