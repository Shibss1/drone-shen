# Drone Shenanigans: Flight or Plight?
REDTEECON 1 Conference Talk (18th August 2023)
- Researchers
  - Tan Sheng Yu
  - Jovin Choo Shue Jin
 
## Overview of Research
This research documents the vulnerabilites and security concerns with the DJI x Tello Drone. By utilising unencrypted traffic and insecure configurations, this drone is susceptible to many forms of attacks. In this research, we have tackled on the following:
  - De-authentication
  - WPA2-PSK Wi-Fi password cracking
  - Tello SDK

This repository includes files that execute said attacks:
 1) ```attack.py``` - Utilses the drone's SDK after gaining initial access to crash the physical drone and then reconfigure its Wi-Fi settings.
 2) ```sniff.py``` - Essential script required in order for attack.py to function; Outputs a pcapng file
 3) ```deauth.py``` - Simple de-authentication script

## Additional sub topics
### Using attack.py
1) Use ```sniff.py``` to sniff the network traffic. Manually stop the script when you have successfully captured the 4-way handshake of a successful authentication to the drone's network.
2) In ```attack.py```, change the 'file' variable to match the path of the file obtained from ```sniff.py``` (in this case, demo.pcapng).
3) In the same file, change the 'wlist' variable to match the path of your own dictionary.

### Explanation
In this sub-section, the attack is further explained. Future enhancements to the script and research as a whole are brought up here as well.

1) ```sniff.py``` <br>
This script utilises hcxdumptool to sniff network traffic. The purpose of this script is to acquire the 4-way handshake of, in this context, successful authentications into the targeted drone's network. It will then output a pcapng file, which is utilised in ```attack.py```

2) ```sampleDict.txt``` <br>
A sample dictionary passed through hashcat to attempt to crack the Wi-Fi password.

3) ```capHash.22000 / sampleCap.pcapng``` #I think can remove this file, serves no purpose for people who download the tool directly <br>
The pcapng file captured from ```sniff.py``` and the converted .22000 from hcxdumptool.

4) ```attack.py``` <br>
This script utilses the pcapng file obtained from ```sniff.py``` to reformat the 4-way handshake into the .22000 file format (using hcxpcapngtool) to facilitate the cracking of the password through hashcat.
After gaining access into the drone, the script stops the physical motors of the drone, causing it to flop to the surface, and then changes the drone's Wi-Fi name and password through all through its own SDK.

5) ```deauth.py``` <br>
A script that utilises aireplay-ng to deauthenticate the drone.

### Future Improvements
1) Compile the different attacks into one file, making it a interactive tool.
2) One limitation of the sniffing portion of the attack is that it has to be manually stopped after capturing the 4-way handshake.
3) Another limitation is that since each attack is its own file currently (16/10/2023), the files variable in some files have to manually changed
4) We have yet to try a UDP packet replay attack. The unencrypted UDP traffic sends information about the drone (temp, battery etc.). This can be taken advantage of by sending false packets. 


## References/Links
https://www.aircrack-ng.org/ <br>
https://www.aircrack-ng.org/doku.php?id=aireplay-ng <br>
https://hashcat.net/wiki/doku.php?id=cracking_wpawpa2

