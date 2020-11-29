#!coding:utf-8

import os

class DataStore():
    """
    """
    def __init__(self, datadir=None, df=None, outdir=None):
        self.datadir = datadir
        self.df = df
        self.outdir = outdir

    def __str__(self):
        pass

    def listdir(self):
        """
        list folder files
        parames:
            indir: folder path
        return:
            files: file path
        """
        indir = self.datadir
        files = os.listdir(indir)
        files = [os.path.join(indir, _file) for _file in files]
        return files

    def write2csv(self, outfile):
        """
        write DataFrame data to csv filie
        """
        self.df.to_csv(outfile)
        print(outfile)

    def write2sql(self):
        pass
