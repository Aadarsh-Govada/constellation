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

const = pysat.Constellation(instruments=inst_list, date_array = dtarr)
'''print("directly downloading -------------------------------------------------------------------------------------------------------------------")
const.download()
print("download complete")
const.load(date=const.today())

'''
# Instrument level download
for inst in const.instruments:
    inst.download(date_array=dtarr)