sudo cp serial.service /etc/systemd/system/serial.service
sudo chmod 644 /etc/systemd/system/serial.service
sudo systemctl daemon-reload
sudo systemctl enable serial.service