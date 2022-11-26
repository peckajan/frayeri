class Patient():

    def __init__(self, diagnosis=0, exercise=0, diet=0, medicaton=0) -> None:
        self._diagnosis = diagnosis

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        for single_diagnosis in diagnosis:
            if "E10" in single_diagnosis[0]:
                diagnosis = 1
                break
            elif "E11" in single_diagnosis[0]:
                diagnosis = 2
                break
            else:
                diagnosis = None
        self._diagnosis = diagnosis

    @property
    def exercise(self):
        return self._exercise

    @exercise.setter
    def exercise(self, exercise):
        ...

    @property
    def diet(self):
        return self._diet

    @diet.setter
    def diet(self, diet):
        ...

    @property
    def diet(self):
        return self._diet

    @diet.setter
    def diet(self, diet):
        ...
