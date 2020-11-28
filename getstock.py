#!coding:utf-8

import sys
import datetime
import baostock as bs
import pandas as pd
import argparse

__author__ = "hanwei"
__date__ = "20201128"
__email__ = "hanwei@shangshaitech.edu.cn"


class ArgParse(object):
    """
    parse command line class
    """
    def __init__(self):
        self.args = ''

    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
                "-s", "--summaryfile",
                help="stock list file, tushare outpu file")
        parser.add_argument(
                "-o", "--output",
                help="output file path")
        parser.add_argument(
                "-c", "--code",
                help="stock code")
        self.args = parser.parse_args()


class ObtainData(object):
    """
    get data, use baostock
    Parames:
        filename: stock list file that from tushare
        summary: stock summary data
    """
    def __init__(self, filename):
        self.filename = filename
        self.summary = None
        self.codelist = None
    
    def __str__(self):
        return "Runing date {}".format(self.getdate())

    def getdate(self, days=0, weeks=0, years=0):
        """
        get date, default is current date
        days: before days
        weeks: before weeks
        years: before years
        """
        date = datetime.datetime.now()
        if days or weeks:
            date = date - datetime.timedelta(
                    days=days,
                    weeks=weeks)
        date = date.strftime("%Y-%m-%d")
        if years:
            dates = date.split("-")
            year = str(int(dates[0]) - int(years))
            dates[0] = year
            date = "-".join(dates)
        return date

    def getsummary(self):
        """
        tushare stock list data
        """
        self.summary = pd.read_csv(self.filename)

    def getlist(self):
        if self.summary is None:
            # get summary data first
            self.getsummary()
        self.codelist = self.summary.ts_code
        self.codelist = list(self.codelist.values)

    def refomatcode(self):
        """
        tushare codes are different from baostock.
        translate tushare code to baostock code.
        """
        codes = []
        for _code in self.codelist:
            _code, area = _code.split(".")
            _code = area.lower() + "." + _code
            codes.append(_code)
        self.codelist = codes

    def download(self):
        """
        download data from baostock
        """
        curdate = getdate()
        lg = bs.login()
        rs = bs.query_history_k_data_plus(
            code = "sh.600000",
            fields = "date, code, open,\
                    high, low, close,\
                    preclose, volume,\
                    amount, adjustflag,\
                    turn, tradestatus,\
                    pctChg,isST",
            start_date='2017-07-01',
            end_date=curdate,
            frequency="d",
            adjustflag="2")
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        data = pd.DataFrame(data_list, columns=rs.fields)
        bs.logout()
        return data

if __name__ == "__main__":
    Args = ArgParse()
    Args.parse()
    Obt = ObtainData(Args.args.summaryfile)
    Obt.getsummary()
    Obt.getlist()
    Obt.refomatcode()
    print(Obt.getdate(days=10, weeks=1, years=1))
    print(Obt)
