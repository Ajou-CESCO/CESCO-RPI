sudo cp client.service /etc/systemd/system/client.service
sudo chmod 644 /etc/systemd/system/client.service
sudo systemctl daemon-reload
sudo systemctl enable client.service