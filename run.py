#!coding: utf-8

from peach.getstock import ArgParse
from peach.getstock import ObtainData

Args = ArgParse()
Args.parse()
infile = Args.args.summaryfile
code = Args.args.code
outfile = Args.args.output

Obtain = ObtainData(infile)
if code:

