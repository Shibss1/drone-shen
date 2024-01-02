# Drone Shenanigans: Flight or Plight?
REDTEECON 1 Conference Talk (18th August 2023)
- Researchers
  - Tan Sheng Yu
  - Jovin Choo Shue Jin
 
## Overview of Research
This research documents the vulnerabilites and security concerns with the DJI x Tello Drone. <br>
By utilising unencrypted traffic and insecure configurations, this drone is susceptible to many forms of attacks. In this research, we have tackled on the following:
  - De-Authentication 
  - WPA2-PSK Wi-Fi password cracking
  - Tello SDK

<p align="center"><img src="https://stormsend1.djicdn.com/tpc/uploads/carousel/image/82192d33e2da1445e5a7cc0f60ff138b@ultra.jpg" height=250 width=250><br>DJI X Tello Drone</p>

## Using exploit.py
In the file, there are two values to be changed, ```pcap_file``` and ```wlist```: <br>
1) ```pcap_file``` is a packet capture file that contains the WPA2 handshake of the Wi-Fi network that you want to crack. <br>
2) ```wlist``` is a word list you provide for the dictionary attack.

### Summary of exploit.py
This file contains 3 different ways to mess with the drone. <br>
The 1st is utilising aireplay-ng to launch a deauthentication attack on the drone. <br>
The 2nd and 3rd is utilising the TELLO SDK to immediately stop the drone's motors as well as change its Wi-Fi name and password

## Future Improvements
~~1) Compile the different attacks into one file, making it a interactive tool.~~ <br>
2) We have yet to try a UDP packet replay attack. The unencrypted UDP traffic sends information about the drone (temp, battery etc.). This can be taken advantage of by sending false packets.
3) nmcli connection is iffy, maybe try find an alternative

## References/Links
https://www.aircrack-ng.org/ <br>
https://www.aircrack-ng.org/doku.php?id=aireplay-ng <br>
https://hashcat.net/wiki/doku.php?id=cracking_wpawpa2 <br>
https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf <br>
https://www.ryzerobotics.com/tello
