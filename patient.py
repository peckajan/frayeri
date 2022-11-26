class Patient():

    def __init__(self, patient_id=0, HbA1c_18=None, HbA1c_19=None, HbA1c_20=None, HbA1c_21=None, HbA1c_22=None, dm_type=None) -> None:
        self._patient_id = patient_id
        self._HbA1c_18 = HbA1c_18
        self._HbA1c_19 = HbA1c_19
        self._HbA1c_20 = HbA1c_20
        self._HbA1c_21 = HbA1c_21
        self._HbA1c_22 = HbA1c_22
    
    @property
    def patient_id(self):
        return self._patient_id
    
    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id
    
    @property
    def HbA1c_18(self):
        return self._HbA1c_18
    
    @HbA1c_18.setter
    def HbA1c_18(self, HbA1c_18):
        self._HbA1c_18 = HbA1c_18

    @property
    def HbA1c_19(self):
        return self._HbA1c_19
    
    @HbA1c_19.setter
    def HbA1c_19(self, HbA1c_19):
        self._HbA1c_19 = HbA1c_19

    @property
    def HbA1c_20(self):
        return self._HbA1c_20
    
    @HbA1c_20.setter
    def HbA1c_20(self, HbA1c_20):
        self._HbA1c_20 = HbA1c_20

    @property
    def HbA1c_21(self):
        return self._HbA1c_21
    
    @HbA1c_21.setter
    def HbA1c_21(self, HbA1c_21):
        self._HbA1c_21 = HbA1c_21

    @property
    def HbA1c_22(self):
        return self._HbA1c_22
    
    @HbA1c_22.setter
    def HbA1c_22(self, HbA1c_22):
        self._HbA1c_22 = HbA1c_22