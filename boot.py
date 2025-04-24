# executed on every boot

import config
import network
import gc

sta_if = network.WLAN(network.WLAN.IF_STA)
sta_if.active(True)
sta_if.connect(config.station_ssid, config.station_password)

ap_if = network.WLAN(network.WLAN.IF_AP)
ap_if.active(False)

while sta_if.isconnected() == False:
    pass

print("connected to wifi")

gc.collect()
