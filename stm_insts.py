import pysat
from pysat import constellations

inst = list(constellations.testing.instruments)



const = pysat.Constellation(instruments=inst)
ref_time = pysat.instruments.pysat_testing._test_dates['']['']
attrs = ["platforms", "names", "tags", "inst_ids", "instruments",
              "bounds", "empty", "empty_partial", "index_res",
              "common_index", "date", "yr", "doy", "yesterday", "today",
              "tomorrow", "variables"]
inst_attrs = ['platform', 'name', 'tag', 'inst_id', 'clean_level',
                   'pandas_format', "empty", "yr", 'pad', 'date',
                   'doy', 'acknowledgements', 'references']
dims = ['time', 'x', 'y', 'z', 'profile_height', 'latitude',
             'longitude', 'altitude']