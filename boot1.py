import _thread
import socket
import network
from machine import Pin

update = Pin(5, Pin.IN, Pin.PULL_UP)
if update.value() == 0 or True:
	wlan = network.WLAN(network.AP_IF)
	wlan.config(essid="esp32")
	wlan.ifconfig(("192.168.5.1", "255.255.255.0", "192.168.5.1", "114.114.114.114"))
	wlan.active(True)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("0.0.0.0", 5000))
	s.listen(1)

	data = ""
	while True:
		conn, addr = s.accept()

		while True:
			temp = conn.recv(1024)
			if len(temp) == 0:
				conn.close()
				break
			data += temp.decode()

		# 解析

