#!/usr/bin/env python3


from _ftp_multi import multi_dates
from datetime import datetime, timedelta
from _logging import loggin
from os.path import basename, split
from time import localtime, perf_counter
from sys import exc_info


def main(bugun=False):
    try:
        # TODAY
        if bugun or localtime().tm_hour > 12:
            try:
                multi_dates(tarih=datetime.today())

            except Exception as error:
                exc_type, _, exc_tb = exc_info()
                fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        # YESTERDAY
        try:
            multi_dates(tarih=datetime.today() - timedelta(days=1))

        except Exception as error:
            exc_type, _, exc_tb = exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

        if datetime.today().weekday() == 0:
            # SATURDAY
            try:
                multi_dates(tarih=datetime.today() - timedelta(days=2))

            except Exception as error:
                exc_type, _, exc_tb = exc_info()
                fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

            # FRIDAY
            try:
                multi_dates(tarih=datetime.today() - timedelta(days=3))

            except Exception as error:
                exc_type, _, exc_tb = exc_info()
                fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
                loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")

    except Exception as error:
        exc_type, _, exc_tb = exc_info()
        fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
        loggin(content=f"{fname}, {exc_tb.tb_lineno}, {exc_type}, {error}")


if __name__ == "__main__":
    loggin(content=f"{basename(__file__)}, Start: {perf_counter()}")
    main()
    loggin(content=f"{basename(__file__)}, End: {perf_counter()}")
