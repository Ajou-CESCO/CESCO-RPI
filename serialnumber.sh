cat /proc/cpuinfo | grep Serial | awk '{print $3}' > serialnumber.txt