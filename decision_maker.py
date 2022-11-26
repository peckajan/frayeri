"""
nacteme data, potom vyhod


"""
from data_loader import DataLoader
from patient import Patient
import csv
import numpy as np


class DecisionMaker:
    
    def __init__(self) -> None:
        dl = DataLoader("xdddddd")
        self._patients = dl.MakePatient("sssssss")
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
                #jak vypocitat complience
                if int(patient.HbA1c_22) <= 48 or (int(patient.HbA1c_22) <=int(patient.HbA1c_21) and int(patient.HbA1c_22) <= 55):
                    row.append("0")
                    row.append("0")
                elif int(patient.HbA1c_22) <= int(patient.HbA1c_21) or (int(patient.HbA1c_22) >= int(patient.HbA1c_21) + (int(patient.HbA1c_21) * 0.3)):
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
                



    



def main():
    dm = DecisionMaker()

if __name__ == "__main__":
    main()