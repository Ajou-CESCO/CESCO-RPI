import requests
import datetime
pin_num=1
serial_number="100000006c14dcf1"
msg=" / ".join([str(datetime.datetime.now()),str(pin_num),serial_number])

data=msg.split(" / ")
json_dict={
    # "date":data[0],
    "serial":data[2],
    "index":data[1]
}
res=requests.patch(url="http://175.45.205.29:8080/api/dose/log",
                  json=json_dict,
                  timeout=3
                  )

print(res.status_code)
print(res.text)