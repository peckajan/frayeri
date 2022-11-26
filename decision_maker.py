"""
nacteme data, potom vyhod


"""
from data_loader import DataLoader
from patient import Patient
import csv


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
            if patient.dm_type == None:
                break
            row = []
            row.append(patient.patient_id)
            row.append(patient.diagnosis)

            #jak vypocitat complience
            if patient.HbA1c_22 <= 48 or (patient.HbA1c_22 <= patient.HbA1c_21 and patient.HbA1c_22 <= 55):
                row.append("0")
                row.append("0")
            elif patient.HbA1c_22 <= patient.HbA1c_21 or (patient.HbA1c_22 >= patient.HbA1c_21 + (patient.HbA1c_21 * 0.3)):
                row.append("1")
                row.append("0")
            else:
                row.append("1")
                row.append("1")

            rows.append(row)

        with open ("output.csv", "w") as outputFile:
            outputFile.write(rows)
                



    



def main():
    ...

if __name__ == "__main__":
    main()