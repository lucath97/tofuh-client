# executed after boot

import machine
import umqtt.simple
import config
import time

pin0 = machine.Pin(5, machine.Pin.OUT)
pin1 = machine.Pin(4, machine.Pin.OUT)
pin2 = machine.Pin(0, machine.Pin.OUT)


def get_bit(byte_data: bytes, bit_index: int) -> int:
    byte_index = bit_index // 8
    local_bit_index = bit_index % 8
    target_byte_value = byte_data[byte_index]
    bit_value = (target_byte_value >> local_bit_index) & 1
    return bit_value


def set_pin(pin: machine.Pin, val: int):
    if val == 1:
        pin.on()
    else:
        pin.off()


def on_msg_received(_, msg: bytes):
    print("received msg")

    state0 = get_bit(msg, config.state_offset)
    state1 = get_bit(msg, config.state_offset + 1)
    state2 = get_bit(msg, config.state_offset + 2)

    set_pin(pin0, state0)
    set_pin(pin1, state1)
    set_pin(pin2, state2)
    print("updated pins")


def main():
    mqtt = umqtt.simple.MQTTClient(
        config.mqtt_client_id,
        config.mqtt_broker,
        port=config.mqtt_port,
        user=config.mqtt_username,
        password=config.mqtt_password,
    )
    mqtt.set_callback(on_msg_received)
    mqtt.connect()
    print(f"connected to mqtt broker {config.mqtt_broker}")

    mqtt.subscribe(config.mqtt_subscribe_topic)
    print(f"subscribed to topic {config.mqtt_subscribe_topic}")

    while True:
        mqtt.check_msg()
        time.sleep_ms(config.mqtt_check_msg_interval_ms)


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"an unexpected error ocurred: {e}")
        print("resetting machine")
        machine.reset()
