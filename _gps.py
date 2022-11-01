#!/usr/bin/env python3


from _logging import loggin
from os.path import split
from serial import Serial
from sys import exc_info


def gps_veri():
    nmea_longitude = 0
    nmea_latitude = 0
    nmea_speed = 0
    nmea_data = []

    serialPort = Serial(
        baudrate=115200,
        timeout=0.5,
        rtscts=True,
        dsrdtr=True,
        port="/dev/ttyUSB1",
    )

    try:
        for _ in range(10):
            nmea_data.append(serialPort.readline().decode("utf-8"))

        for line in nmea_data:
            if line is not None and "$GPRMC" in line:
                nmea_buffer = line.split(",")

                nmea_latitude = nmea_buffer[3]
                nmea_longitude = nmea_buffer[5]
                nmea_speed = nmea_buffer[7]

                break

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    return nmea_latitude, nmea_longitude, nmea_speed
