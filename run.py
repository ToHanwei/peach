#!coding: utf-8

import os
import sys

from getstock import ArgParse
from getstock import ObtainData
from datastore import DataStore


__author__ = "hanwei"
__date__ = "20201128"
__email__ = "hanwei@shanghaitech.edu.cn"

if len(sys.argv) == 1:
    os.system("python run.py -h")
    sys.exit()

Args = ArgParse()
Args.parse()
infile = Args.args.summaryfile
code = Args.args.code
outfile = Args.args.output
outdir = Args.args.outdir
start = Args.args.start
end = Args.args.end

if code:
    Obt = ObtainData()
    data = Obt.download(code)
    Data = DataStore(df=data)
    if outfile:
        Data.write2csv(outfile)
    else:
        Data.write2csv(code+".csv")
if infile:
    if not outdir:
        outdir = "output"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    Obt = ObtainData(infile)
    Obt.getlist()
    Obt.refomatcode()
    for _code in Obt.codelist:
        outname = os.path.join(outdir, _code+".csv")
        df = Obt.download(_code)
        Data = DataStore(df=df)
        Data.write2csv(outname)
        #df.to_csv(outname)

