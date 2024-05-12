cat /proc/cpuinfo | grep Serial | awk '{print $3}' > /home/rpi/Cesco/PillinTime-RPi/serial/temp.txt
tr -d "\n" < temp.txt > serialnumber.txt
rm temp.txt