"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
from typing import Optional, List, Tuple

class Patient:
    def __init__(self, name):
        self.name = name

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: np.array) -> np.array:
    """Calculate the daily mean of a 2d inflammation data array 

    Parameters
    ----
    data: np.array(dtype=int, ndim=2) 
        2d inflammation data array, which is the patient data across all days
    
    Returns
    ----
    mean: np.array(dtype=float, ndim=1)
        Returns a column-wise mean of the data

    Raise
    ----
    ValueError:
        Raises an error if data is not of type np.ndarray
    """
    if not isinstance(data, np.ndarray):  
        raise ValueError("data should be of type np.ndarray")
    
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

# def test_func1(data: np.ndarray) -> Tuple[str, str]:
#     return ("A", "B")

# def test_func2(data: np.ndarray) -> List[str, str]:
#     if not isinstance(data, np.ndarray):  
#         raise ValueError("data should be of type np.array")

#     return ["A", "B"]

# def test_func3(data: np.ndarray) -> Optional[str]:
#     return None if data == [0] else "A"

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    max = np.max(data, axis=1)
    return data / max[:, np.newaxis]