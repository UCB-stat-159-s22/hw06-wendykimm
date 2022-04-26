import pytest
import ligotools
from ligotools import readligo as rl
from ligotools import utils
import matplotlib.mlab as mlab
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import json
import h5py
import os

def test_loaddata():
    strain, time, chan_dict = rl.loaddata('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    test, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_frame('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'H1', True)
    assert strain == test

# read_frame(filename, ifo, readstrain=True)

# read_hdf5(filename, readstrain=True)

# loaddata(filename, ifo=None, tvec=True, readstrain=True)

# dq2segs(channel, gps_start)

# dq_channel_to_seglist(channel, fs=4096)

# getstrain(start, stop, ifo, filelist=None)

# getsegs(start, stop, ifo, flag='DATA', filelist=None)