import os
import re
import patient
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



class DataManger:
    def __init__(self, root=r"C:\Users\janpe\Downloads\xd\hackathon.tar\hackathon") -> None:
        self.root = root
        self.patients = []
        for dirname in os.listdir(self.root):
            f = os.path.join(self.root, dirname)
            for file in os.listdir(f):
                print(file)
                if file == "dg.txt":
                    self.DgLoad(os.path.join(f, file))
                
            break
            
        # checking if it is a file

    def GetPatient(self):
        pass

    def DgLoad(self, filepath):
        if re.search("E10|E11")
        pass

    def StepLoad(self):
        pass

    def WeightLoad(self):
        pass

    def WaistLoad(self):
        pass

    





    
def main():
    d = DataManger()
    
if __name__ == "__main__":
    main()