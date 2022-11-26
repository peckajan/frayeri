"""
dg z amb zpráv 👌
kroky 👌
energie
čas cvičení
heart rate resting
heart rate walking
ekg
váha 👌
obvod pasu 👌


"""

import json
from os.path import join as path_join
from patient import Patient

class DataLoader:
    def __init__(self, folder) -> None:
        self.folder = folder

    def MakePatient(self, folder) -> Patient:
        dg_path = path_join(folder, 'dg.txt')
        step_path = path_join(folder, 'steps.txt')
        weight_path = path_join(folder, 'weight.txt')
        waist_path = path_join(folder, 'waist.txt')

        return Patient(
             self.DgLoad(dg_path),
             self.StepLoad(step_path),
             self.WeightLoad(weight_path),
             self.WaistLoad(waist_path)
             )

    def DgLoad(self, file):
        diag = json.load(open(file, encoding='ISO-8859-2'))
        diag = [x.split(':') for x in diag]
        diag = [x if len(x) == 2 else [None, x[0]] for x in diag]
        return diag


    def StepLoad(self, file):
        pass

    def WeightLoad(self, file):
        pass

    def WaistLoad(self, file):
        pass
