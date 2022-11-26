from patient import Patient
from data_loader import DataLoader

class DecisionMaker:
    
    def __init__(self) -> None:
        dl = DataLoader()
        self._patient = dl.MakePatient(...)

    def decisions(self):
        ...




def main():
    ...

if __name__ == "__main__":
    main()