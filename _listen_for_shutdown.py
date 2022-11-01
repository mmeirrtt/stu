#!/usr/bin/env python3


from _pin_numbers import BUZZER_PIN, ONAY_PIN, POWER_PIN, RED_PIN, SHUTDOWN_PIN
from subprocess import call
from _upload import main
from _pin import m_pin
from RPi.GPIO import (
    wait_for_edge,
    setwarnings,
    FALLING,
    setmode,
    PUD_UP,
    BOARD,
    setup,
    IN,
)


setwarnings(False)
setmode(BOARD)
setup(SHUTDOWN_PIN, IN, pull_up_down=PUD_UP)


m_pin(pin=BUZZER_PIN, value=False)
m_pin(pin=POWER_PIN, value=True)
m_pin(pin=ONAY_PIN, value=False)
m_pin(pin=RED_PIN, value=False)


wait_for_edge(SHUTDOWN_PIN, FALLING)
main(bugun=True)


m_pin(pin=POWER_PIN, value=False)


call(["shutdown", "-h", "now"], shell=False)
