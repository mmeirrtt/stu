#!/usr/bin/env python3


from _logging import loggin
from os.path import exists, isfile, join, split
from pathlib import Path
from m_id import M_ID
from sys import exc_info


def rfid_save(uid, zaman, gun, ay, yil, am_pm):
    for _ in range(14 - len(uid)):
        uid = uid + "0"

    folder = join(
        join(
            join(
                join(
                    join(
                        "/",
                        "home",
                    ),
                    "arge",
                ),
                "kart",
            ),
            f"{yil}",
        ),
        f"{ay:02}",
    )
    file_path = join(folder, f"{M_ID}_kart_{yil}_{ay:02}_{gun:02}_{am_pm}")
    backup_path = join(folder, f"{M_ID}_kart_{yil}_{ay:02}_{gun:02}_{am_pm}_backup")

    try:
        if not exists(path=folder):
            Path(folder).mkdir(parents=True, exist_ok=True)

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        if isfile(path=file_path) is False:
            with open(file=file_path, mode="w") as file:
                file.write("tarih,kart_id")

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        if isfile(path=backup_path) is False:
            with open(file=backup_path, mode="w") as file:
                file.write("tarih,kart_id")

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        if isfile(path=file_path):
            with open(file=file_path) as file:
                liste_file = file.readlines()

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        if isfile(path=backup_path):
            with open(file=backup_path) as file:
                liste_backup = file.readlines()

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    try:
        liste = (
            liste_backup.copy()
            if len(liste_backup) > len(liste_file)
            else liste_file.copy()
        )

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    if len(liste) > 0:
        if (
            liste[-1].split(sep=",")[1] != uid
            or zaman - int(liste[-1].split(sep=",")[0]) > 60 * 60
        ):
            try:
                with open(file=file_path, mode="a") as file:
                    file.write(f"\n{zaman},{uid}")

            except Exception as error:
                exc_type, _, exc_tb = exc_info()
                fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

            try:
                with open(file=backup_path, mode="a") as backup:
                    backup.write(f"\n{zaman},{uid}")

            except Exception as error:
                exc_type, _, exc_tb = exc_info()
                fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")
    else:
        try:
            with open(file=file_path, mode="a") as file:
                file.write(f"\n{zaman},{uid}")

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        try:
            with open(file=backup_path, mode="a") as backup:
                backup.write(f"\n{zaman},{uid}")

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")
