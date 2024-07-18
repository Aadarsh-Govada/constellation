import pysat
from pysatCDAAC.instruments import cosmic2_ivm as ivm


inst_list = list()
inst_id = 'e'

for i in range(1, 7):
    inst = pysat.Instrument(inst_module=ivm, inst_id=inst_id + str(i))
    inst_list.append(inst)
print(inst_list)




ivm_const = pysat.Constellation(instruments=inst_list)

for i, inst in enumerate(ivm_const.instruments):
    print(ivm_const.names[i], inst.files.files[-1])