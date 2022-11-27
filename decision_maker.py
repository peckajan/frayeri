"""
This class is responsible for choosing suitable patients for an education.

"""
from data_loader import DataLoader
from patient import Patient
import csv
import numpy as np


class DecisionMaker:
    
    def __init__(self) -> None:
        dl = DataLoader()
        self._patients = dl.MakePatient()
        self.Decisions()
        

    def Decisions(self):
        fields = ["Patient_id", "Diagnosis", "Education", "Meeting"]
        
        rows = []
        rows.append(fields)
        for patient in self._patients:
            #diabetes
            if patient.dm_type == "":
                continue
            row = []
            row.append(patient.patient_id)
            row.append(patient.dm_type)

            try:
                currentValue = int(patient.HbA1c_22)
                previousValue = int(patient.HbA1c_21)
                if currentValue <= 48 or (currentValue <= previousValue and currentValue <= 55):
                    row.append("0")
                    row.append("0")
                elif currentValue <= previousValue or (currentValue >= previousValue + (previousValue * 0.3)):
                    row.append("1")
                    row.append("0")
                else:
                    row.append("1")
                    row.append("1")
            except:
                row.append("0")
                row.append("0")
            rows.append(row)

        np.savetxt("output.csv",
            rows,
            delimiter =", ",
            fmt ='% s')
                