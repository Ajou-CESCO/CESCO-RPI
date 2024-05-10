sudo cp lte.service /etc/systemd/system/lte.service
sudo chmod 644 /etc/systemd/system/lte.service
sudo systemctl daemon-reload
sudo systemctl enable lte.service