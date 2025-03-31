import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ben/Documents/master_thesis/code/uwb_online_initialisation_simulator/src/install/online_uwb_initialisation'
