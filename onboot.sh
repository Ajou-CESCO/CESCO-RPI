sudo vi /etc/rc.local

# 
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

(
sleep 10
sudo pppd call gprs&
sleep 5
sudo route add default ppp0
) > /tmp/rc.log 2>&1


exit 0