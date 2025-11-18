from ligotools import readligo
import numpy as np
import h5py
import os
import pytest

@pytest.fixture(scope='module')
def test_data():
    strain_data = np.random.rand(1000)
    dq_mask = np.random.randint(0, 2, size=1000) 
    inj_mask = np.random.randint(0, 2, size=1000)

    filename = 'test_data.hdf5'

    with h5py.File(filename, 'w') as f:
        strain_group = f.create_group('strain')
        dset = strain_group.create_dataset('Strain', data=strain_data)
        dset.attrs['Xspacing'] = 1.0
    
        quality_group = f.create_group('quality')
        dq_group = quality_group.create_group('simple')
        dq_group.create_dataset('DQmask', data=dq_mask)
        dq_group.create_dataset('DQShortnames', data=np.array(['DATA', 'GLITCH'], dtype='S'))

        inj_group = quality_group.create_group('injections')
        inj_group.create_dataset('Injmask', data=inj_mask)
        inj_group.create_dataset('InjShortnames', data=np.array(['INJECTION'], dtype='S'))
    
        meta_group = f.create_group('meta')
        meta_group.create_dataset('GPSstart', data=1234567890)

        yield filename

        if os.path.exists(filename):
            os.remove(filename)

def test_read_hdf5(test_data):
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = readligo.read_hdf5(test_data)

    assert strain is not None

def test_loaddata(test_data):
    strain, time, channel_dict = readligo.loaddata(test_data)

    assert strain is not None  
    assert time is not None
    assert 'DEFAULT' in channel_dict