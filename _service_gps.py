#!/usr/bin/env python3


from _gps_save import gps_save
from _logging import loggin
from os.path import split
from serial import Serial
from time import localtime, sleep, strftime, time
from _gps import gps_veri
from sys import exc_info


def main():
    try:
        serialPort = Serial(
            port="/dev/ttyUSB2", baudrate=115200, timeout=1, rtscts=True, dsrdtr=True
        )

        serialPort.write("AT+QGPS=1\r".encode())
        serialPort.close()
        sleep(1)

        while True:
            enlem, boylam, hiz = gps_veri()

            if enlem or boylam or hiz:
                try:
                    if float(enlem) != 0 and float(boylam) != 0 or int(hiz) != 0:
                        gps_save(
                            enlem=enlem,
                            boylam=boylam,
                            hiz=hiz,
                            zaman=int(time()),
                            gun=localtime().tm_mday,
                            ay=localtime().tm_mon,
                            yil=localtime().tm_year,
                            am_pm=strftime("%p", localtime()),
                        )

                except Exception as error:
                    exc_type, _, exc_tb = exc_info()
                    fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                    loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

            sleep(10)

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")


if __name__ == "__main__":
    main()
