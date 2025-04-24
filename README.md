# TofUH Client for ESP8266

A MicroPython based client for the TofUH system. This software was developed to run on the ESP8266 microcontroller. It has not been tested on any other machines.

## Setup

1. Flash the ESP8266 with the MicroPython firmware (https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro)

2. Install the MicroPython remote control on your machine (https://docs.micropython.org/en/latest/reference/mpremote.html)

3. Create a file named `config.py` in the repository root and insert a config like this:

```python
station_ssid = ""               # string: SSID of your wireless access point"
station_password = ""           # string: password for your wireless access point

mqtt_broker = ""                # string: host of the MQTT broker
mqtt_port = 0                   # int: port of the MQTT broker
mqtt_client_id = ""             # string: MQTT client id for this machine
mqtt_username = ""              # string: MQTT username (empty string if not applicable)
mqtt_password = ""              # string: MQTT password (empty string if not applicable)
mqtt_subscribe_topic = ""       # string: name of the MQTT state queue
mqtt_check_msg_interval_ms = 0  # int: interval in which to check for new messages

state_offset = 0                # int: bit offset for the state

```

4. Deploy the software to the microcontroller with the `deploy.sh` script
