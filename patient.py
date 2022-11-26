class Patient():

    def __init__(self, diagnosis=0, exercise=0, diet=0, medicaton=0) -> None:
        self._diagnosis = diagnosis

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
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
