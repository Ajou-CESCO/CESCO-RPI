sudo cp sensor.service /etc/systemd/system/sensor.service
sudo chmod 644 /etc/systemd/system/sensor.service
sudo systemctl daemon-reload
sudo systemctl enable sensor.service