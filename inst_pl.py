import pysat
from pysatCDAAC.instruments import cosmic2_ivm as ivm
import datetime as dt


inst_str = 'e'
dtarr = [dt.datetime(2021, 1, 1)]

for i in range(1, 7):
    inst_id = inst_str + str(i)
    inst = pysat.Instrument(inst_module=ivm, inst_id=inst_id)
    print("downloading for " + inst_id + " ------------------------------------------------------")
    inst.download(date_array=dtarr)
    print("download for " + inst_id + " complete")



