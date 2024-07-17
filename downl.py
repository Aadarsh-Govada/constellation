import pysat
import pysatSpaceWeather
import matplotlib.pyplot as plt
import datetime as dt

'''
import pysatNASA
# Initalize the DE2 Constellation using the DE2 constellation module
de2 = pysat.Constellation(const_module=pysatNASA.constellations.de2)
'''

# Now initialize the ACE real-time Constellation
ace_rt = pysat.Constellation(platforms=['ace'], tags=['realtime'])
# ace_rt.download()
ace_rt.load(date=ace_rt.today())

for i, inst in enumerate(ace_rt.instruments):
    print(ace_rt.names[i], inst.files.files[-1])

# Convert the output to an Instrument
rt_inst = ace_rt.to_inst()
print(rt_inst)

print(rt_inst.variables)

start = dt.datetime(2001, 1, 1)
stop = dt.datetime(2001, 1, 2)
plt.plot(rt_inst['sw_proton_dens'], '--', label='sw_proton_dens')
plt.show()
