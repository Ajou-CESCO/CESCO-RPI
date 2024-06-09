sudo cp server.service /etc/systemd/system/server.service
sudo chmod 644 /etc/systemd/system/server.service
sudo systemctl daemon-reload
sudo systemctl enable server.service