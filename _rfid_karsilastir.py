#!/usr/bin/env python3


from _logging import loggin
from os.path import isfile, join, split
from sys import exc_info


def is_personel(uid):
    liste = []

    try:
        file_path = join(
            join(
                join(
                    join(
                        "/",
                        "home",
                    ),
                    "arge",
                ),
                "personel",
            ),
            "personel",
        )
        if isfile(path=file_path):
            with open(file=file_path) as file:
                liste = file.readlines()

            for index in range(len(liste)):
                liste[index] = liste[index].replace("\n", "")

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    uid = uid.upper() if len(uid) == 14 else uid.upper() + "000000"

    return uid in liste
