import pysat
from pysatCDAAC.instruments import cosmic2_ivm as ivm
import datetime as dt



'-------------------------------Initialize Instruments---------------------------------------------------'
inst_list = list()
inst_id = 'e'

for i in range(1, 7):
    inst = pysat.Instrument(inst_module=ivm, inst_id=inst_id + str(i))
    inst_list.append(inst)
print(inst_list)
print("\n\n\n")

'-------------------------------Initialize Constellation---------------------------------------------------'


dtarr = [dt.datetime(2021, 1, 1)]
kwargs = {'date_array' : dtarr}



const = pysat.Constellation(instruments=inst_list)
print("downloading --------------------------------------------------------------------------------------------------------------------------")
const.download()
print("download complete")
const.load(date=const.today())

'''
print(const.instruments)

# Convert the output to an Instrument
ivm_inst = const.to_inst()
print(ivm_inst)

print("Vars: ")
print(ivm_inst.variables)

'''