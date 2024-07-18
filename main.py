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

'-------------------------------Define local methods/params---------------------------------------------------'
'''

def _call_inst_method(instruments, method, *args, **kwargs):
        """Call a method across all instrumennts.

        Parameters
        ----------
        instruments: list-like
            List of instruments
        method : str
            Instrument method name
        *args : list-like
            Optional list of arguments for the method
        **kwargs : dict-like
            Optional dict of keyword arguments for the method

        Raises
        ------
        AttributeError
            If `method` is missing from any Constellation Instrument.

        """

        for instrument in instruments:
            # Test to see that method exists
            if not hasattr(instrument, method):
                raise AttributeError(
                    'unknown method {:} in Instrument {:}'.format(
                        repr(method), repr(instrument)))

            # Apply method to Instrument
            inst_method = getattr(instrument, method)
            inst_method(*args, **kwargs)

        return


'-------------------------------Initialize Constellation---------------------------------------------------'




_call_inst_method(instruments=inst_list, method='download', date_array = dtarr)
print("done")'''

dtarr = [dt.datetime(2021, 1, 1)]

const = pysat.Constellation(instruments=inst_list)
#print("downloading -------------------------------------------------------------------------------------------------------------------")
#const.download(date_array = dtarr)
#print("download complete")
const.load(date=dtarr[0])


'''
# Instrument level download
for inst in const.instruments:
    print("downloading for " + inst.inst_id)
    inst.download(date_array=dtarr)
    print("done")'''

print("Variables by inst: ")
for inst in const.instruments:
    print("Vars for " + inst.inst_id)
    print(inst.variables)


# convert to instrument
inst = const.to_inst()
print("Variables:")
print(inst.variables)


