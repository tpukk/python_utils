import numpy as np


def round_to_n_significant_digits(x, n=3):
    """
    Rounds the given float to n significant digits
    Parameters
    ----------
    x : float
    n : int
    Returns
    -------
    x : float
    """
    return round(x, -int(np.floor(np.log10(abs(x))))+n-1)