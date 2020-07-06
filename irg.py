# coding: utf-8


class CalculIRGTotal:
    def calculeIRG(self, salaireImposable, nbrjourtravaille, nbrJourATravaille):
        irg = 0
        Abattement = 0
        TauxAbattement = 0.40
        # salaireImposable -= (salaireImposable* 10/100)   #Arrondir à la dizaine inférieur
        TranchIRG = [10000, 30000, 120000]
        pourcentage = [0, 0.20, 0.30, 0.35]
        AbattementMinMAX = [1000, 1500]


        if (salaireImposable <= TranchIRG[0]):  # inférieur à 10 000 DA
            irg = 0


        elif (salaireImposable <= TranchIRG[1]):  # Entre 10 000 et 30 000 DA
            irg = (salaireImposable - TranchIRG[0]) * pourcentage[1]



        elif (salaireImposable <= TranchIRG[2]):  # Entre 30 000 et 120 000 DA
            irg = ((TranchIRG[1] - TranchIRG[0]) * pourcentage[1]) + (
            (salaireImposable - TranchIRG[1]) * pourcentage[2])


        else:  # supérieur à 120 000 DA
            irg = ((TranchIRG[1] - TranchIRG[0]) * pourcentage[1]) + ((TranchIRG[2] - TranchIRG[1]) * pourcentage[2]) + \
                  ((salaireImposable - TranchIRG[2]) * pourcentage[3])

        Abattement = irg * TauxAbattement

        if (Abattement < AbattementMinMAX[0]):
            Abattement = AbattementMinMAX[0]

        if (Abattement > AbattementMinMAX[1]):
            Abattement = AbattementMinMAX[1]

        irg -= Abattement

        if (irg < 0):
            irg = 0
        elif (salaireImposable <= 30000):
            irg = 0
        elif (30000 < salaireImposable < 35000 ):
            irg = round(irg * 8/3 - (6666.6666),2)
            


        return irg


s = CalculIRGTotal()
print s.calculeIRG(30040, 0, 0)