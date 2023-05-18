#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass

    # initialize properties 
    def __init__(self, name = "Sofia", job = "Admin"):
        self.name = name
        self.job = job

    # set name method 
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    # get name method 
    def get_name (self) :
        return self._name 
    
    # name property constructor
    name = property(get_name, set_name)

    # set job method 
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    # get job method 
    def get_job(self):
        return self._job

    # job property constructor 
    job = property(get_job, set_job)



