#!/usr/bin/env python3


from _logging import loggin
from os.path import isfile, join, split
from m_id import M_ID
from time import time
from sys import exc_info


def file_rfid(file_path, temp_path, gun, ay, yil, sam):
    liste_gps = []

    gps_path = join(
        join(
            join(
                join(
                    join(
                        join(
                            "/",
                            "home",
                        ),
                        "arge",
                    ),
                    "gps",
                ),
                f"{yil}",
            ),
            f"{ay:02}",
        ),
        f"{M_ID}_arac_{yil}_{ay:02}_{gun:02}_{sam}",
    )

    if isfile(path=file_path):
        try:
            with open(file=file_path) as file:
                liste_eski = file.readlines()

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        try:
            if isfile(path=gps_path):
                try:
                    with open(file=gps_path) as file:
                        liste_gps = file.readlines()

                except Exception as error:
                    exc_type, _, exc_tb = exc_info()
                    fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                    loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        liste_yeni = []
        liste_yeni.append("tarih,kart_id,enlem,boylam\n")

        if len(liste_eski) > 0:
            if len(liste_gps) == 0:
                for k in range(1, len(liste_eski)):
                    kart = liste_eski[k].replace("\n", "").split(sep=",")
                    liste_yeni.append(f"{kart[0]},{kart[1]},0,0\n")

            else:
                s = 0
                for k in range(1, len(liste_eski)):
                    kart = liste_eski[k].replace("\n", "").split(sep=",")

                    for g in range(s, len(liste_gps)):
                        try:
                            gps = liste_gps[g].replace("\n", "").split(sep=",")

                            if float(gps[0]) >= float(kart[0]):
                                liste_yeni.append(
                                    f"{kart[0]},{kart[1]},{gps[1]},{gps[2]}\n"
                                )
                                s = g
                                break

                        except Exception as error:
                            exc_type, _, exc_tb = exc_info()
                            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                            loggin(
                                content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}"
                            )

        try:
            if len(liste_yeni) > 0:
                with open(file=temp_path, mode="w") as file:
                    for kart in liste_yeni:
                        file.write(f"{kart}")

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    return temp_path
