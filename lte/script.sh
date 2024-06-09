sudo socat - /dev/ttyUSB2,crlf < input.txt
sudo dhclient -v usb0
ping -c 10 -I usb0 8.8.8.8