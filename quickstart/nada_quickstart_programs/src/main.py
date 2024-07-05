from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    bp = SecretInteger(Input(name="BloodPressure", party=party1))
    glucose = SecretInteger(Input(name="GlucoseLevel", party=party1))
    disease = SecretInteger(Input(name="Disease", party=party2))

    condition_met = bp.greater_than(140).and_(glucose.greater_than(150)).and_(disease.equal(1))

    return [Output(condition_met, "condition_met", party3)]
