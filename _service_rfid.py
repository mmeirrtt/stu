#!/usr/bin/env python3


from _rfid_karsilastir import is_personel
from _pin_numbers import BUZZER_INTERVAL, BUZZER_TIME, BUZZER_PIN, ONAY_PIN, RED_PIN
from _rfid_save import rfid_save
from RPi.GPIO import BOARD, setmode, setwarnings
from binascii import hexlify
from _logging import loggin
from pn532pi import Pn532, pn532, Pn532Spi
from os.path import split
from time import localtime, sleep, strftime, time
from _pin import m_pin
from sys import exc_info


def main():
    try:
        setwarnings(False)
        setmode(BOARD)

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        nfc = Pn532(Pn532Spi(Pn532Spi.SS0_GPIO8))
        nfc.begin()

        try:
            nfc.SAMConfig()

            while True:
                try:
                    success, uid = nfc.readPassiveTargetID(
                        pn532.PN532_MIFARE_ISO14443A_106KBPS
                    )

                    if success:
                        try:
                            uid = str(hexlify(data=uid).decode()).upper()

                        except Exception as error:
                            exc_type, _, exc_tb = exc_info()
                            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                            loggin(
                                content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}"
                            )

                        try:
                            rfid_save(
                                uid=uid,
                                zaman=int(time()),
                                gun=localtime().tm_mday,
                                ay=localtime().tm_mon,
                                yil=localtime().tm_year,
                                am_pm=strftime("%p", localtime()),
                            )

                        except Exception as error:
                            exc_type, _, exc_tb = exc_info()
                            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                            loggin(
                                content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}"
                            )

                        try:
                            if is_personel(uid=uid):
                                m_pin(pin=ONAY_PIN, value=True)

                                m_pin(pin=BUZZER_PIN, value=True)
                                sleep(BUZZER_TIME / 2)
                                m_pin(pin=BUZZER_PIN, value=False)

                            else:
                                m_pin(pin=RED_PIN, value=True)

                                for _ in range(BUZZER_INTERVAL):
                                    m_pin(pin=BUZZER_PIN, value=True)
                                    sleep(BUZZER_TIME / (BUZZER_INTERVAL * 2))
                                    m_pin(pin=BUZZER_PIN, value=False)
                                    sleep(BUZZER_TIME / (BUZZER_INTERVAL * 2))

                            sleep(1 - BUZZER_TIME)
                            m_pin(pin=RED_PIN, value=False)
                            m_pin(pin=ONAY_PIN, value=False)

                        except Exception as error:
                            exc_type, _, exc_tb = exc_info()
                            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                            loggin(
                                content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}"
                            )

                except Exception as error:
                    exc_type, _, exc_tb = exc_info()
                    fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                    loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

                sleep(0.1)

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")


if __name__ == "__main__":
    main()
