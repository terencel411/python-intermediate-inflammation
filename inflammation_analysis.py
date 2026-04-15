#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]
    
    for filename in InFiles:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data), 
            'max': models.daily_max(inflammation_data), 
            'min': models.daily_min(inflammation_data)}

        patient_data = models.daily_mean(inflammation_data)

        diff = 0
        day = 0
        previous_patient = 0
        for i in range(len(patient_data)):
            patient_diff = patient_data[i] - previous_patient
            if patient_diff > diff:
                diff = patient_diff
                day = i
            
            previous_patient = patient_data[i]
        
        print(f"Patient Average: {patient_data}")
        print(f"Day on which they become worse on average: {day}")

        views.visualize(filename, view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()
    
    main(args)
