import subprocess

output_file = "demo.pcapng"

def on_monitor():
    try:
        cmd = """systemctl stop NetworkManager wpa_supplicant && 
            ip link set wlan0 down && 
            iw dev wlan0 set type monitor && 
            ip link set wlan0 up"""
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print("Error", {e})

def dump():
    try:
        cmd = "hcxdumptool -o " + output_file + " -i wlan0 --enable_status=1 --disable_ap_attacks"
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print("Error", {e})

def main():
    on_monitor()
    dump()

main()
