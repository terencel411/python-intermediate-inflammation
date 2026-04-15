# Introduction
The Beginning!

This is a template software project repository used by the [Intermediate Research Software Development Skills In Python](https://github.com/carpentries-incubator/python-intermediate-development).

## Purpose

This repository is intended to be used as an example software project which is copied by learners of the 
[Intermediate Research Software Development Skills In Python](https://github.com/carpentries-incubator/python-intermediate-development) course.

This software project is not finished, does not contain a LICENCE file, the code is currently failing to run and contains some code style issues. 
It is used as a starting point for the course - issues will be fixed and code will be added in a number of places during the course by learners in their own copies of the repository, as course topics are introduced.

## Tests

Several tests have been implemented already, some of which are currently failing.
These failing tests set out the requirements for the additional code to be implemented during the workshop.

The tests should be run using `pytest`, which will be introduced during the workshop.

# Software Development as a Process

## Software Requirements

### Business Requirements

BR1: To figure out when to proactively do clinical intervention and resource allocation after first day of showing adverse symptoms (not just symptoms, but it shold be a drastic change)

### Stakeholder Requirements

SR: Implement a process to figure out how long it takes for the patient to get worse starting from day 1

### Solution Requirements

SR1: Add logic in the models.py to find out for a patient on which day the change in inflammation is the highest (difference in inflammation values)

SR2: Add logic in the models.py to find out for a list of patients, what is the average?
