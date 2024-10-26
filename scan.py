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
    network_to_scan = '140.10.7.1/21'  
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=network_to_scan, arguments='-sn')
    
    active_devices = []
    active_count = 0
    inactive_count = 0

    for host in scan_result['scan']:
        if len(active_devices) >= 25:  
            break

        mac_address = scan_result['scan'][host]['addresses'].get('mac', None)
        if mac_address:
            is_active = ping_device(host)
            active_devices.append({
                'ip': host,
                'active': is_active
            })

            if is_active:
                active_count += 1
            else:
                inactive_count += 1

    return render_template(
        'index.html',
        devices=active_devices,
        scan_result=network_to_scan,
        active_count=active_count,
        inactive_count=inactive_count
    )

if __name__ == '__main__':
    app.run(debug=True)
