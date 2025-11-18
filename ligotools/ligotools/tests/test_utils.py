from ligotools.utils import whiten, write_wavfile, reqshift, plot_psd
import numpy as np
from scipy.interpolate import interp1d

def test_whiten():
    data = np.random.randn(1000)
    fs = 4096
    Pxx = np.ones(500)
    dt = 1.0 / fs
    freqs = np.linspace(0, 2048, 500)
    interp_psd = interp1d(freqs, Pxx, bounds_error=False, fill_value="extrapolate")
    white_ht = whiten(data, interp_psd, dt)
    assert white_ht is not None

def test_reqshift():
    data = np.arange(100)
    shifted = reqshift(data, 100, 10)
    assert shifted.shape == data.shape