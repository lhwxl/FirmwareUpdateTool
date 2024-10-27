from machine import Pin
from microdot import Microdot

update = Pin(5, Pin.IN, Pin.PULL_UP)
if update.value() == 0:
	app = Microdot()


	@app.route("/")
	def index():
		return ""


	@app.route("/update")
	def up():
		return ""
