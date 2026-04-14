"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array 

    Parameters
    ----
    data: numpy.array(dtype=int, ndim=2) 
        2d inflammation data array, which is the patient data across all days
    
    Returns
    ----
    mean: numpy.array(dtype=float, ndim=1)
        Returns a column-wise mean of the data

    Raise
    ----
    ValueError:
        Description
    """
    return np.mean(data, axis=0)

def daily_max(data):
    """Summary or Description of the Function

    Parameters
    ----------
    argument1 (int) : Description of arg1

    Returns
    ----------
    int:Returning value

   """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the nth Fibonacci number.

    A recursive implementation of Fibonacci array elements.

    :param data (int): integer gfgfinteger
    :param y: integer
    :raises ValueError: raised if n is less than zero
    :returns: Fibonacci number
    """
    return np.min(data, axis=0)

