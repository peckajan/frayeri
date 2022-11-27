"""
It loads data from csv files
"""

from patient import Patient
import csv

class DataLoader:
    def __init__(self, file) -> None:
        self.file = file

    def MakePatient(self, file) -> list:
        list_patients = []
        with open("hackath_112022_-_HbA1c_IOL.csv", "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                patient_id = row['ï»¿Patient']
                HbA1c_18 = row['HbA1c_18']
                HbA1c_19 = row['HbA1c_19']
                HbA1c_20 = row['HbA1c_20']
                HbA1c_21 = row['HbA1c_21']
                HbA1c_22 = row['HbA1c_22']
                dm_type = row['diabetes type']
                list_patients.append(Patient(patient_id, HbA1c_18, HbA1c_19, HbA1c_20, HbA1c_21, HbA1c_22, dm_type))
            return list_patients