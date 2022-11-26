import numpy as np
import time
import datetime

class Patient():

    def __init__(self, diagnosis=None, step_records=None, weight=None, HbA1c=None) -> None:
        self._diagnosis = diagnosis
        self._step_records = sorted(step_records, key=lambda item: item['date'])
        self._weight = weight
        self._HbA1c = HbA1c

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
    def step_records(self):
      return self._step_records

    def avg_steps_in_n_days(self, n):
      now = time.mktime(time.localtime())
      delta = datetime.timedelta(days=n).total_seconds()
      potential_records = np.array([x['v'] for x in self._step_records if
                                    (now - time.mktime(x['date'])) < delta])
      total = 0
      return np.mean(potential_records) #how good is the data??? are there days missing?

    def total_avg_steps(self):
      potential_records = np.array([x['v'] for x in self._step_records])
      return np.mean(potential_records)

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def HbA1c(self):
        return self._HbA1c

    @HbA1c.setter
    def diet(self, HbA1c):
        self._HbA1c = HbA1c