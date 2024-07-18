import pysat
from pysatCDAAC.instruments import cosmic2_ivm as ivm


inst_list = list()
inst_id = 'e'

for i in range(1, 3):
    inst = pysat.Instrument(inst_module=ivm, inst_id=inst_id + str(i))
    inst_list.append(inst)
print(inst_list)
print("\n\n\n")


const = pysat.Constellation(instruments=inst_list)
const.download()
const.load(date=const.today())

print(const.instruments)

# Convert the output to an Instrument
ivm_inst = const.to_inst()
print(ivm_inst)

print("Vars: ")
print(ivm_inst.variables)

