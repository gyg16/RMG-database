#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product38 <=> product39
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product39 <=> product37
""",
)

entry(
    index = 2,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 3,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 4,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt55 <=> pdt58
""",
)

entry(
    index = 5,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod5
""",
)



entry(
    index = 6,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e+10, 's^-1'),
        n = 0,
        Ea = (28.6604, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 7,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (108.156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHDe
""",
)

entry(
    index = 8,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra;radadd_intra_cs
""",
)

entry(
    index = 9,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSM_D;doublebond_intra;radadd_intra_cs
""",
)

entry(
    index = 10,
    label = "C7H11 <=> C7H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SD_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 11,
    label = "C4H7O <=> C4H7O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.724e+10, 's^-1', '*|/', 3),
        n = 0.478,
        Ea = (122.043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
u"""
Taken from entry: MRH CBS-QB3 calculations for the reaction CH2=CH-CH2-OO => *CH2-cycle(CH-CH2-O-O)

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.724e+10 * (T/1K)^0.478 * exp(-29.169 kcal/mol / RT) cm3/mol/s.

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_O
""",
)

entry(
    index = 12,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 13,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (167.36, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 14,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_MSMS;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 15,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (167.36, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SMSM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 16,
    label = "C14H13 <=> C14H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R7_MMSR;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 17,
    label = "C14H13-3 <=> C14H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (167.36, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R7_RSMM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 18,
    label = "C14H13-5 <=> C14H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.21,
        Ea = (188.28, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R7_SMMS;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 19,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        Ea = (53.5552, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_DS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 20,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.73e+09, 's^-1'),
        n = 0.21,
        Ea = (16.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_DSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 21,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        Ea = (53.5552, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess, i.e. 821""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_MS;multiplebond_intra;radadd_intra_cdsingle
""",
)

entry(
    index = 22,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.73e+09, 's^-1'),
        n = 0.21,
        Ea = (16.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess, i.e. 822""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_MSR;multiplebond_intra;radadd_intra_cdsingle
""",
)

entry(
    index = 23,
    label = "C7H13 <=> C7H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.35e+09, 's^-1'),
        n = 0.21,
        Ea = (31.4218, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHNd
""",
)

entry(
    index = 24,
    label = "C8H15 <=> C8H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+09, 's^-1'),
        n = 0.21,
        Ea = (29.6227, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 25,
    label = "C8H13 <=> C8H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.08e+09, 's^-1'),
        n = 0.21,
        Ea = (65.647, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd
""",
)

entry(
    index = 26,
    label = "C9H15 <=> C9H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+09, 's^-1'),
        n = 0.21,
        Ea = (68.1992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 27,
    label = "C8H11 <=> C8H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.45e+09, 's^-1'),
        n = 0.21,
        Ea = (54.392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHCt
""",
)

entry(
    index = 28,
    label = "C9H13 <=> C9H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+09, 's^-1'),
        n = 0.21,
        Ea = (58.6597, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 29,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.68e+09, 's^-1'),
        n = 0.21,
        Ea = (19.7485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 30,
    label = "C7H13-3 <=> C7H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.26e+09, 's^-1'),
        n = 0.21,
        Ea = (29.9574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 31,
    label = "C8H15-3 <=> C8H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.52e+10, 's^-1'),
        n = 0.21,
        Ea = (30.8779, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 32,
    label = "C9H17 <=> C9H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+10, 's^-1'),
        n = 0.21,
        Ea = (29.0788, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 33,
    label = "C9H15-3 <=> C9H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.44e+10, 's^-1'),
        n = 0.21,
        Ea = (65.103, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 34,
    label = "C10H17 <=> C10H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.09e+10, 's^-1'),
        n = 0.21,
        Ea = (67.6553, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 35,
    label = "C9H13-3 <=> C9H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+10, 's^-1'),
        n = 0.21,
        Ea = (53.8481, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 36,
    label = "C10H15 <=> C10H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.7e+10, 's^-1'),
        n = 0.21,
        Ea = (58.1158, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 37,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02e+11, 's^-1'),
        n = 0.21,
        Ea = (19.2046, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 38,
    label = "C8H15-5 <=> C8H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.81e+09, 's^-1'),
        n = 0.21,
        Ea = (28.8278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 39,
    label = "C9H17-3 <=> C9H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.89e+10, 's^-1'),
        n = 0.21,
        Ea = (29.7482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 40,
    label = "C10H19 <=> C10H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.85e+10, 's^-1'),
        n = 0.21,
        Ea = (27.9491, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 41,
    label = "C10H17-3 <=> C10H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+11, 's^-1'),
        n = 0.21,
        Ea = (63.9315, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 42,
    label = "C11H19 <=> C11H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.83e+10, 's^-1'),
        n = 0.21,
        Ea = (66.4838, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 43,
    label = "C10H15-3 <=> C10H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.31e+10, 's^-1'),
        n = 0.21,
        Ea = (52.7184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 44,
    label = "C11H17 <=> C11H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.53e+10, 's^-1'),
        n = 0.21,
        Ea = (56.9442, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 45,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+11, 's^-1'),
        n = 0.21,
        Ea = (18.0749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 46,
    label = "C8H13-3 <=> C8H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.04e+09, 's^-1'),
        n = 0.21,
        Ea = (17.1544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 47,
    label = "C9H15-5 <=> C9H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.04e+10, 's^-1'),
        n = 0.21,
        Ea = (18.0749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 48,
    label = "C10H17-5 <=> C10H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.38e+09, 's^-1'),
        n = 0.21,
        Ea = (16.2758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 49,
    label = "C10H15-5 <=> C10H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.31e+10, 's^-1'),
        n = 0.21,
        Ea = (52.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 50,
    label = "C11H17-3 <=> C11H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.33e+09, 's^-1'),
        n = 0.21,
        Ea = (54.8522, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 51,
    label = "C10H13 <=> C10H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+10, 's^-1'),
        n = 0.21,
        Ea = (41.045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 52,
    label = "C11H15 <=> C11H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.57e+10, 's^-1'),
        n = 0.21,
        Ea = (45.3127, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 53,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.89e+10, 's^-1'),
        n = 0.21,
        Ea = (6.40152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 54,
    label = "C9H15-7 <=> C9H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.65e+09, 's^-1'),
        n = 0.21,
        Ea = (18.1586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 55,
    label = "C10H17-7 <=> C10H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.44e+10, 's^-1'),
        n = 0.21,
        Ea = (19.079, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 56,
    label = "C11H19-3 <=> C11H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.65e+09, 's^-1'),
        n = 0.21,
        Ea = (17.2799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 57,
    label = "C11H17-5 <=> C11H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.16e+10, 's^-1'),
        n = 0.21,
        Ea = (53.2623, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 58,
    label = "C12H19 <=> C12H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.58e+09, 's^-1'),
        n = 0.21,
        Ea = (55.8146, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 59,
    label = "C11H15-3 <=> C11H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.78e+10, 's^-1'),
        n = 0.21,
        Ea = (42.0492, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 60,
    label = "C12H17 <=> C12H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.88e+10, 's^-1'),
        n = 0.21,
        Ea = (46.275, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 61,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.06e+10, 's^-1'),
        n = 0.21,
        Ea = (7.40568, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 62,
    label = "C8H11-3 <=> C8H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.6e+09, 's^-1'),
        n = 0.21,
        Ea = (16.4431, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 63,
    label = "C9H13-5 <=> C9H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.41e+10, 's^-1'),
        n = 0.21,
        Ea = (17.3636, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 64,
    label = "C10H15-7 <=> C10H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+10, 's^-1'),
        n = 0.21,
        Ea = (15.5645, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 65,
    label = "C10H13-3 <=> C10H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.34e+10, 's^-1'),
        n = 0.21,
        Ea = (51.5469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 66,
    label = "C11H15-5 <=> C11H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.37e+10, 's^-1'),
        n = 0.21,
        Ea = (54.0991, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 67,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.22e+10, 's^-1'),
        n = 0.21,
        Ea = (40.3338, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 68,
    label = "C11H13 <=> C11H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.39e+10, 's^-1'),
        n = 0.21,
        Ea = (44.5596, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 69,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+11, 's^-1'),
        n = 0.21,
        Ea = (5.69024, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 70,
    label = "C9H13-7 <=> C9H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.84e+09, 's^-1'),
        n = 0.21,
        Ea = (17.6146, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 71,
    label = "C10H15-9 <=> C10H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+10, 's^-1'),
        n = 0.21,
        Ea = (18.5351, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 72,
    label = "C11H17-7 <=> C11H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.06e+09, 's^-1'),
        n = 0.21,
        Ea = (16.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 73,
    label = "C11H15-7 <=> C11H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.44e+10, 's^-1'),
        n = 0.21,
        Ea = (52.7602, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 74,
    label = "C12H17-3 <=> C12H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.99e+09, 's^-1'),
        n = 0.21,
        Ea = (55.3125, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 75,
    label = "C11H13-3 <=> C11H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.88e+10, 's^-1'),
        n = 0.21,
        Ea = (41.5053, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 76,
    label = "C12H15 <=> C12H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+10, 's^-1'),
        n = 0.21,
        Ea = (45.773, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 77,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.44e+10, 's^-1'),
        n = 0.21,
        Ea = (6.86176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 78,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.84e+10, 's^-1'),
        n = 0.21,
        Ea = (36.7355, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 79,
    label = "C5H9 <=> C5H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+11, 's^-1'),
        n = 0.21,
        Ea = (37.656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHNd
""",
)

entry(
    index = 80,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.06e+10, 's^-1'),
        n = 0.21,
        Ea = (35.8569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 81,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.44e+11, 's^-1'),
        n = 0.21,
        Ea = (71.8811, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHCd
""",
)

entry(
    index = 82,
    label = "C7H11-3 <=> C7H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.99e+10, 's^-1'),
        n = 0.21,
        Ea = (74.4334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 83,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.88e+11, 's^-1'),
        n = 0.21,
        Ea = (60.6262, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHCt
""",
)

entry(
    index = 84,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+11, 's^-1'),
        n = 0.21,
        Ea = (64.8938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 85,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.44e+11, 's^-1'),
        n = 0.21,
        Ea = (25.9826, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 86,
    label = "C5H9-3 <=> C5H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.04e+11, 's^-1'),
        n = 0.21,
        Ea = (36.1916, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 87,
    label = "C6H11-5 <=> C6H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.7e+12, 's^-1'),
        n = 0.21,
        Ea = (37.1121, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 88,
    label = "C7H13-5 <=> C7H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.47e+11, 's^-1'),
        n = 0.21,
        Ea = (35.313, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 89,
    label = "C7H11-5 <=> C7H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.72e+12, 's^-1'),
        n = 0.21,
        Ea = (71.3372, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 90,
    label = "C8H13-5 <=> C8H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.39e+11, 's^-1'),
        n = 0.21,
        Ea = (73.8894, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 91,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.97e+12, 's^-1'),
        n = 0.21,
        Ea = (60.0822, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 92,
    label = "C8H11-5 <=> C8H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+12, 's^-1'),
        n = 0.21,
        Ea = (64.3499, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 93,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.81e+12, 's^-1'),
        n = 0.21,
        Ea = (25.4387, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 94,
    label = "C6H11-7 <=> C6H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.77e+11, 's^-1'),
        n = 0.21,
        Ea = (35.0619, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 95,
    label = "C7H13-7 <=> C7H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.53e+12, 's^-1'),
        n = 0.21,
        Ea = (35.9824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 96,
    label = "C8H15-7 <=> C8H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.42e+12, 's^-1'),
        n = 0.21,
        Ea = (34.1833, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 97,
    label = "C8H13-7 <=> C8H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.58e+12, 's^-1'),
        n = 0.21,
        Ea = (70.1657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 98,
    label = "C9H15-9 <=> C9H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.41e+12, 's^-1'),
        n = 0.21,
        Ea = (72.7179, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 99,
    label = "C8H11-7 <=> C8H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+12, 's^-1'),
        n = 0.21,
        Ea = (58.9526, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 100,
    label = "C9H13-9 <=> C9H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.48e+12, 's^-1'),
        n = 0.21,
        Ea = (63.1784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 101,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+13, 's^-1'),
        n = 0.21,
        Ea = (24.309, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 102,
    label = "C6H9-9 <=> C6H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.34e+11, 's^-1'),
        n = 0.21,
        Ea = (23.3886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 103,
    label = "C7H11-7 <=> C7H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+12, 's^-1'),
        n = 0.21,
        Ea = (24.309, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 104,
    label = "C8H13-9 <=> C8H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.9e+11, 's^-1'),
        n = 0.21,
        Ea = (22.5099, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 105,
    label = "C8H11-9 <=> C8H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+12, 's^-1'),
        n = 0.21,
        Ea = (58.5342, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 106,
    label = "C9H13-11 <=> C9H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.86e+11, 's^-1'),
        n = 0.21,
        Ea = (61.0864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 107,
    label = "C8H9 <=> C8H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+12, 's^-1'),
        n = 0.21,
        Ea = (47.2792, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 108,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+12, 's^-1'),
        n = 0.21,
        Ea = (51.5469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 109,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.52e+12, 's^-1'),
        n = 0.21,
        Ea = (12.6357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 110,
    label = "C7H11-9 <=> C7H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.8e+11, 's^-1'),
        n = 0.21,
        Ea = (24.3927, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 111,
    label = "C8H13-11 <=> C8H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.87e+12, 's^-1'),
        n = 0.21,
        Ea = (25.3132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 112,
    label = "C9H15-11 <=> C9H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.88e+11, 's^-1'),
        n = 0.21,
        Ea = (23.5141, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 113,
    label = "C9H13-13 <=> C9H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.97e+12, 's^-1'),
        n = 0.21,
        Ea = (59.4965, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 114,
    label = "C10H15-11 <=> C10H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.82e+11, 's^-1'),
        n = 0.21,
        Ea = (62.0487, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 115,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.37e+12, 's^-1'),
        n = 0.21,
        Ea = (48.2834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 116,
    label = "C10H13-5 <=> C10H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+12, 's^-1'),
        n = 0.21,
        Ea = (52.5092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 117,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.42e+12, 's^-1'),
        n = 0.21,
        Ea = (13.6398, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 118,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.07e+11, 's^-1'),
        n = 0.21,
        Ea = (22.6773, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 119,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.39e+12, 's^-1'),
        n = 0.21,
        Ea = (23.5978, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 120,
    label = "C8H11-11 <=> C8H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.06e+12, 's^-1'),
        n = 0.21,
        Ea = (21.7986, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 121,
    label = "C8H9-3 <=> C8H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.17e+12, 's^-1'),
        n = 0.21,
        Ea = (57.781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 122,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+12, 's^-1'),
        n = 0.21,
        Ea = (60.3333, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 123,
    label = "C8H7 <=> C8H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.48e+12, 's^-1'),
        n = 0.21,
        Ea = (46.5679, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 124,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.61e+12, 's^-1'),
        n = 0.21,
        Ea = (50.7938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 125,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.81e+12, 's^-1'),
        n = 0.21,
        Ea = (11.9244, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 126,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.95e+11, 's^-1'),
        n = 0.21,
        Ea = (23.8488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 127,
    label = "C8H11-13 <=> C8H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.97e+12, 's^-1'),
        n = 0.21,
        Ea = (24.7693, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 128,
    label = "C9H13-15 <=> C9H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        Ea = (22.9702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 129,
    label = "C9H11-7 <=> C9H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.18e+12, 's^-1'),
        n = 0.21,
        Ea = (58.9944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 130,
    label = "C10H13-7 <=> C10H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.13e+11, 's^-1'),
        n = 0.21,
        Ea = (61.5466, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 131,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+12, 's^-1'),
        n = 0.21,
        Ea = (47.7394, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 132,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52e+12, 's^-1'),
        n = 0.21,
        Ea = (52.0071, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 133,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.71e+12, 's^-1'),
        n = 0.21,
        Ea = (13.0959, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 134,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52e+10, 's^-1'),
        n = 0.21,
        Ea = (71.0862, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 135,
    label = "C6H11-9 <=> C6H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02e+11, 's^-1'),
        n = 0.21,
        Ea = (72.0066, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHNd
""",
)

entry(
    index = 136,
    label = "C7H13-9 <=> C7H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.19e+10, 's^-1'),
        n = 0.21,
        Ea = (70.2075, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 137,
    label = "C7H11-11 <=> C7H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.15e+11, 's^-1'),
        n = 0.21,
        Ea = (106.232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHCd
""",
)

entry(
    index = 138,
    label = "C8H13-13 <=> C8H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.16e+10, 's^-1'),
        n = 0.21,
        Ea = (108.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 139,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.43e+10, 's^-1'),
        n = 0.21,
        Ea = (94.9768, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHCt
""",
)

entry(
    index = 140,
    label = "C8H11-15 <=> C8H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.82e+10, 's^-1'),
        n = 0.21,
        Ea = (99.2445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 141,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.94e+11, 's^-1'),
        n = 0.21,
        Ea = (60.3333, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 142,
    label = "C6H11-11 <=> C6H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+11, 's^-1'),
        n = 0.21,
        Ea = (70.5422, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 143,
    label = "C7H13-11 <=> C7H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+12, 's^-1'),
        n = 0.21,
        Ea = (71.4627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 144,
    label = "C8H15-9 <=> C8H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.35e+11, 's^-1'),
        n = 0.21,
        Ea = (69.6636, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 145,
    label = "C8H13-15 <=> C8H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+12, 's^-1'),
        n = 0.21,
        Ea = (105.688, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 146,
    label = "C9H15-13 <=> C9H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.32e+11, 's^-1'),
        n = 0.21,
        Ea = (108.24, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 147,
    label = "C8H11-17 <=> C8H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.81e+11, 's^-1'),
        n = 0.21,
        Ea = (94.4329, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 148,
    label = "C9H13-17 <=> C9H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.22e+11, 's^-1'),
        n = 0.21,
        Ea = (98.7006, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 149,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.09e+12, 's^-1'),
        n = 0.21,
        Ea = (59.7894, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 150,
    label = "C7H13-13 <=> C7H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.68e+11, 's^-1'),
        n = 0.21,
        Ea = (69.4126, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 151,
    label = "C8H15-11 <=> C8H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.79e+12, 's^-1'),
        n = 0.21,
        Ea = (70.333, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 152,
    label = "C9H17-5 <=> C9H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.62e+11, 's^-1'),
        n = 0.21,
        Ea = (68.5339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 153,
    label = "C9H15-15 <=> C9H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.79e+12, 's^-1'),
        n = 0.21,
        Ea = (104.516, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 154,
    label = "C10H17-9 <=> C10H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.57e+11, 's^-1'),
        n = 0.21,
        Ea = (107.069, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 155,
    label = "C9H13-19 <=> C9H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+12, 's^-1'),
        n = 0.21,
        Ea = (93.3032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 156,
    label = "C10H15-13 <=> C10H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+12, 's^-1'),
        n = 0.21,
        Ea = (97.529, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 157,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.18e+12, 's^-1'),
        n = 0.21,
        Ea = (58.6597, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 158,
    label = "C7H11-13 <=> C7H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.25e+10, 's^-1'),
        n = 0.21,
        Ea = (57.7392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 159,
    label = "C8H13-17 <=> C8H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        Ea = (58.6597, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 160,
    label = "C9H15-17 <=> C9H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.94e+11, 's^-1'),
        n = 0.21,
        Ea = (56.8606, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 161,
    label = "C9H13-21 <=> C9H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+12, 's^-1'),
        n = 0.21,
        Ea = (92.843, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 162,
    label = "C10H15-15 <=> C10H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.92e+11, 's^-1'),
        n = 0.21,
        Ea = (95.437, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 163,
    label = "C9H11-9 <=> C9H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.52e+11, 's^-1'),
        n = 0.21,
        Ea = (81.6298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 164,
    label = "C10H13-9 <=> C10H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.76e+11, 's^-1'),
        n = 0.21,
        Ea = (85.8975, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 165,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.79e+12, 's^-1'),
        n = 0.21,
        Ea = (46.9863, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 166,
    label = "C8H13-19 <=> C8H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.11e+11, 's^-1'),
        n = 0.21,
        Ea = (58.7434, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 167,
    label = "C9H15-19 <=> C9H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.41e+11, 's^-1'),
        n = 0.21,
        Ea = (59.6638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 168,
    label = "C10H17-11 <=> C10H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.32e+11, 's^-1'),
        n = 0.21,
        Ea = (57.8647, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 169,
    label = "C10H15-17 <=> C10H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.57e+12, 's^-1'),
        n = 0.21,
        Ea = (93.8471, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 170,
    label = "C11H17-9 <=> C11H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.3e+11, 's^-1'),
        n = 0.21,
        Ea = (96.3994, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 171,
    label = "C10H13-11 <=> C10H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.42e+11, 's^-1'),
        n = 0.21,
        Ea = (82.634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 172,
    label = "C11H15-9 <=> C11H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.7e+11, 's^-1'),
        n = 0.21,
        Ea = (86.8598, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 173,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.14e+12, 's^-1'),
        n = 0.21,
        Ea = (47.9905, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 174,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        Ea = (57.0279, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 175,
    label = "C8H11-19 <=> C8H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.34e+12, 's^-1'),
        n = 0.21,
        Ea = (57.9484, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 176,
    label = "C9H13-23 <=> C9H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.21e+11, 's^-1'),
        n = 0.21,
        Ea = (56.1493, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 177,
    label = "C9H11-11 <=> C9H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.84e+12, 's^-1'),
        n = 0.21,
        Ea = (92.1317, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 178,
    label = "C10H13-13 <=> C10H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.17e+11, 's^-1'),
        n = 0.21,
        Ea = (94.6839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 179,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.8e+11, 's^-1'),
        n = 0.21,
        Ea = (80.9186, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 180,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+12, 's^-1'),
        n = 0.21,
        Ea = (85.1444, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 181,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.88e+12, 's^-1'),
        n = 0.21,
        Ea = (46.275, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 182,
    label = "C8H11-21 <=> C8H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.17e+11, 's^-1'),
        n = 0.21,
        Ea = (58.1994, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 183,
    label = "C9H13-25 <=> C9H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.81e+11, 's^-1'),
        n = 0.21,
        Ea = (59.1199, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 184,
    label = "C10H15-19 <=> C10H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.45e+11, 's^-1'),
        n = 0.21,
        Ea = (57.3208, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 185,
    label = "C10H13-15 <=> C10H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.65e+12, 's^-1'),
        n = 0.21,
        Ea = (93.3032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 186,
    label = "C11H15-11 <=> C11H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.43e+11, 's^-1'),
        n = 0.21,
        Ea = (95.8973, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 187,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.71e+11, 's^-1'),
        n = 0.21,
        Ea = (82.0901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 188,
    label = "C11H13-5 <=> C11H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.01e+11, 's^-1'),
        n = 0.21,
        Ea = (86.3159, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 189,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+12, 's^-1'),
        n = 0.21,
        Ea = (47.4466, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 190,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.69e+10, 's^-1'),
        n = 0.21,
        Ea = (91.6714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 191,
    label = "C7H11-15 <=> C7H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.13e+11, 's^-1'),
        n = 0.21,
        Ea = (92.5919, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHNd
""",
)

entry(
    index = 192,
    label = "C8H13-21 <=> C8H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.55e+10, 's^-1'),
        n = 0.21,
        Ea = (90.7928, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 193,
    label = "C8H11-23 <=> C8H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+11, 's^-1'),
        n = 0.21,
        Ea = (126.775, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHCd
""",
)

entry(
    index = 194,
    label = "C9H13-27 <=> C9H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.52e+10, 's^-1'),
        n = 0.21,
        Ea = (129.327, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 195,
    label = "C8H9-5 <=> C8H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.27e+10, 's^-1'),
        n = 0.21,
        Ea = (115.562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHCt
""",
)

entry(
    index = 196,
    label = "C9H11-13 <=> C9H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.7e+10, 's^-1'),
        n = 0.21,
        Ea = (119.788, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 197,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.27e+11, 's^-1'),
        n = 0.21,
        Ea = (80.9186, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 198,
    label = "C7H11-17 <=> C7H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.78e+11, 's^-1'),
        n = 0.21,
        Ea = (91.1275, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 199,
    label = "C8H13-23 <=> C8H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+12, 's^-1'),
        n = 0.21,
        Ea = (92.048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 200,
    label = "C9H15-21 <=> C9H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.73e+11, 's^-1'),
        n = 0.21,
        Ea = (90.2489, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 201,
    label = "C9H13-29 <=> C9H13-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.52e+12, 's^-1'),
        n = 0.21,
        Ea = (126.231, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 202,
    label = "C10H15-21 <=> C10H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.69e+11, 's^-1'),
        n = 0.21,
        Ea = (128.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 203,
    label = "C9H11-15 <=> C9H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.69e+11, 's^-1'),
        n = 0.21,
        Ea = (115.018, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 204,
    label = "C10H13-17 <=> C10H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.14e+11, 's^-1'),
        n = 0.21,
        Ea = (119.244, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 205,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.44e+12, 's^-1'),
        n = 0.21,
        Ea = (80.3746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 206,
    label = "C8H13-25 <=> C8H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.98e+11, 's^-1'),
        n = 0.21,
        Ea = (89.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 207,
    label = "C9H15-23 <=> C9H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.99e+12, 's^-1'),
        n = 0.21,
        Ea = (90.8765, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 208,
    label = "C10H17-13 <=> C10H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.25e+11, 's^-1'),
        n = 0.21,
        Ea = (89.0774, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 209,
    label = "C10H15-23 <=> C10H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.22e+12, 's^-1'),
        n = 0.21,
        Ea = (125.102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 210,
    label = "C11H17-11 <=> C11H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        Ea = (127.654, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 211,
    label = "C10H13-19 <=> C10H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+12, 's^-1'),
        n = 0.21,
        Ea = (113.847, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 212,
    label = "C11H15-13 <=> C11H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.53e+12, 's^-1'),
        n = 0.21,
        Ea = (118.114, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 213,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.77e+12, 's^-1'),
        n = 0.21,
        Ea = (79.2031, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 214,
    label = "C8H11-25 <=> C8H11-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+11, 's^-1'),
        n = 0.21,
        Ea = (78.2826, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 215,
    label = "C9H13-31 <=> C9H13-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.88e+11, 's^-1'),
        n = 0.21,
        Ea = (79.2031, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 216,
    label = "C10H15-25 <=> C10H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.16e+11, 's^-1'),
        n = 0.21,
        Ea = (77.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 217,
    label = "C10H13-21 <=> C10H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+12, 's^-1'),
        n = 0.21,
        Ea = (113.428, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 218,
    label = "C11H15-15 <=> C11H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.14e+11, 's^-1'),
        n = 0.21,
        Ea = (115.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 219,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.03e+11, 's^-1'),
        n = 0.21,
        Ea = (102.173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 220,
    label = "C11H13-7 <=> C11H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.29e+11, 's^-1'),
        n = 0.21,
        Ea = (106.441, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 221,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.99e+12, 's^-1'),
        n = 0.21,
        Ea = (67.5298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 222,
    label = "C9H13-33 <=> C9H13-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.23e+11, 's^-1'),
        n = 0.21,
        Ea = (79.2868, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 223,
    label = "C10H15-27 <=> C10H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.25e+11, 's^-1'),
        n = 0.21,
        Ea = (80.2073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 224,
    label = "C11H17-13 <=> C11H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+11, 's^-1'),
        n = 0.21,
        Ea = (78.4082, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 225,
    label = "C11H15-17 <=> C11H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75e+12, 's^-1'),
        n = 0.21,
        Ea = (114.432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 226,
    label = "C12H17-5 <=> C12H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.56e+11, 's^-1'),
        n = 0.21,
        Ea = (116.985, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 227,
    label = "C11H13-9 <=> C11H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+11, 's^-1'),
        n = 0.21,
        Ea = (103.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 228,
    label = "C12H15-3 <=> C12H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.34e+11, 's^-1'),
        n = 0.21,
        Ea = (107.445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 229,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.39e+12, 's^-1'),
        n = 0.21,
        Ea = (68.5339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 230,
    label = "C8H9-7 <=> C8H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.23e+11, 's^-1'),
        n = 0.21,
        Ea = (77.5714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 231,
    label = "C9H11-17 <=> C9H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+12, 's^-1'),
        n = 0.21,
        Ea = (78.4918, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 232,
    label = "C10H13-23 <=> C10H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.68e+11, 's^-1'),
        n = 0.21,
        Ea = (76.6927, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 233,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.16e+12, 's^-1'),
        n = 0.21,
        Ea = (112.717, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 234,
    label = "C11H13-11 <=> C11H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.64e+11, 's^-1'),
        n = 0.21,
        Ea = (115.269, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 235,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.09e+12, 's^-1'),
        n = 0.21,
        Ea = (101.462, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 236,
    label = "C11H11 <=> C11H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+12, 's^-1'),
        n = 0.21,
        Ea = (105.73, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 237,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.32e+12, 's^-1'),
        n = 0.21,
        Ea = (66.8185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 238,
    label = "C9H11-19 <=> C9H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+11, 's^-1'),
        n = 0.21,
        Ea = (78.7429, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 239,
    label = "C10H13-25 <=> C10H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.69e+11, 's^-1'),
        n = 0.21,
        Ea = (79.6634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 240,
    label = "C11H15-19 <=> C11H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.73e+11, 's^-1'),
        n = 0.21,
        Ea = (77.8642, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 241,
    label = "C11H13-13 <=> C11H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+12, 's^-1'),
        n = 0.21,
        Ea = (113.888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 242,
    label = "C12H15-5 <=> C12H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.7e+11, 's^-1'),
        n = 0.21,
        Ea = (116.441, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 243,
    label = "C11H11-3 <=> C11H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.35e+11, 's^-1'),
        n = 0.21,
        Ea = (102.634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 244,
    label = "C12H13 <=> C12H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.68e+11, 's^-1'),
        n = 0.21,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 245,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e+12, 's^-1'),
        n = 0.21,
        Ea = (67.99, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 246,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+09, 's^-1'),
        n = 0.21,
        Ea = (36.61, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 247,
    label = "C8H15-13 <=> C8H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+10, 's^-1'),
        n = 0.21,
        Ea = (37.5305, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHNd
""",
)

entry(
    index = 248,
    label = "C9H17-7 <=> C9H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.59e+09, 's^-1'),
        n = 0.21,
        Ea = (35.7314, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 249,
    label = "C9H15-25 <=> C9H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.42e+10, 's^-1'),
        n = 0.21,
        Ea = (71.7556, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd
""",
)

entry(
    index = 250,
    label = "C10H17-15 <=> C10H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.56e+09, 's^-1'),
        n = 0.21,
        Ea = (74.3078, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 251,
    label = "C9H13-35 <=> C9H13-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.36e+09, 's^-1'),
        n = 0.21,
        Ea = (60.5006, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHCt
""",
)

entry(
    index = 252,
    label = "C10H15-29 <=> C10H15-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.8e+09, 's^-1'),
        n = 0.21,
        Ea = (64.7683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 253,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+10, 's^-1'),
        n = 0.21,
        Ea = (25.8571, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 254,
    label = "C8H15-15 <=> C8H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+10, 's^-1'),
        n = 0.21,
        Ea = (36.0661, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 255,
    label = "C9H17-9 <=> C9H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0.21,
        Ea = (36.9866, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 256,
    label = "C10H19-3 <=> C10H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.77e+10, 's^-1'),
        n = 0.21,
        Ea = (35.1874, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 257,
    label = "C10H17-17 <=> C10H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.54e+11, 's^-1'),
        n = 0.21,
        Ea = (71.2117, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 258,
    label = "C11H19-5 <=> C11H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.74e+10, 's^-1'),
        n = 0.21,
        Ea = (73.7639, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 259,
    label = "C10H15-31 <=> C10H15-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.78e+10, 's^-1'),
        n = 0.21,
        Ea = (59.9567, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 260,
    label = "C11H17-15 <=> C11H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.24e+10, 's^-1'),
        n = 0.21,
        Ea = (64.2244, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 261,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.48e+11, 's^-1'),
        n = 0.21,
        Ea = (25.3132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 262,
    label = "C9H17-11 <=> C9H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.01e+10, 's^-1'),
        n = 0.21,
        Ea = (34.9364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 263,
    label = "C10H19-5 <=> C10H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        Ea = (35.8569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 264,
    label = "C11H21 <=> C11H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.32e+10, 's^-1'),
        n = 0.21,
        Ea = (34.0578, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 265,
    label = "C11H19-7 <=> C11H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.26e+11, 's^-1'),
        n = 0.21,
        Ea = (70.0402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 266,
    label = "C12H21 <=> C12H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.26e+10, 's^-1'),
        n = 0.21,
        Ea = (72.5924, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 267,
    label = "C11H17-17 <=> C11H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.47e+11, 's^-1'),
        n = 0.21,
        Ea = (58.827, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 268,
    label = "C12H19-3 <=> C12H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.55e+11, 's^-1'),
        n = 0.21,
        Ea = (63.0529, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 269,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.83e+11, 's^-1'),
        n = 0.21,
        Ea = (24.1835, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 270,
    label = "C9H15-27 <=> C9H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+10, 's^-1'),
        n = 0.21,
        Ea = (23.263, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 271,
    label = "C10H17-19 <=> C10H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.96e+10, 's^-1'),
        n = 0.21,
        Ea = (24.1835, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 272,
    label = "C11H19-9 <=> C11H19-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.18e+10, 's^-1'),
        n = 0.21,
        Ea = (22.3844, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 273,
    label = "C11H17-19 <=> C11H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.47e+11, 's^-1'),
        n = 0.21,
        Ea = (58.3668, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 274,
    label = "C12H19-5 <=> C12H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.16e+10, 's^-1'),
        n = 0.21,
        Ea = (60.9609, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 275,
    label = "C11H15-21 <=> C11H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.08e+10, 's^-1'),
        n = 0.21,
        Ea = (47.1537, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 276,
    label = "C12H17-7 <=> C12H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.35e+10, 's^-1'),
        n = 0.21,
        Ea = (51.4214, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 277,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        Ea = (12.5102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 278,
    label = "C10H17-21 <=> C10H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+10, 's^-1'),
        n = 0.21,
        Ea = (24.2672, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H
""",
)

entry(
    index = 279,
    label = "C11H19-11 <=> C11H19-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.34e+10, 's^-1'),
        n = 0.21,
        Ea = (25.1877, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 280,
    label = "C12H21-3 <=> C12H21-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+10, 's^-1'),
        n = 0.21,
        Ea = (23.3886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 281,
    label = "C12H19-7 <=> C12H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.77e+11, 's^-1'),
        n = 0.21,
        Ea = (59.371, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd
""",
)

entry(
    index = 282,
    label = "C13H21 <=> C13H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+10, 's^-1'),
        n = 0.21,
        Ea = (61.9232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 283,
    label = "C12H17-9 <=> C12H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.09e+10, 's^-1'),
        n = 0.21,
        Ea = (48.1578, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt
""",
)

entry(
    index = 284,
    label = "C13H19 <=> C13H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.41e+10, 's^-1'),
        n = 0.21,
        Ea = (52.3837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 285,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+11, 's^-1'),
        n = 0.21,
        Ea = (13.5143, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 286,
    label = "C9H13-37 <=> C9H13-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+10, 's^-1'),
        n = 0.21,
        Ea = (22.5518, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 287,
    label = "C10H15-33 <=> C10H15-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0.21,
        Ea = (23.4722, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 288,
    label = "C11H17-21 <=> C11H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.73e+10, 's^-1'),
        n = 0.21,
        Ea = (21.6731, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 289,
    label = "C11H15-23 <=> C11H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.19e+11, 's^-1'),
        n = 0.21,
        Ea = (57.6555, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 290,
    label = "C12H17-11 <=> C12H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.69e+10, 's^-1'),
        n = 0.21,
        Ea = (60.2078, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 291,
    label = "C11H13-15 <=> C11H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+11, 's^-1'),
        n = 0.21,
        Ea = (46.4424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 292,
    label = "C12H15-7 <=> C12H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.16e+11, 's^-1'),
        n = 0.21,
        Ea = (50.6682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 293,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.37e+11, 's^-1'),
        n = 0.21,
        Ea = (11.7989, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 294,
    label = "C10H15-35 <=> C10H15-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+10, 's^-1'),
        n = 0.21,
        Ea = (23.7233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H
""",
)

entry(
    index = 295,
    label = "C11H17-23 <=> C11H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.79e+10, 's^-1'),
        n = 0.21,
        Ea = (24.6438, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd
""",
)

entry(
    index = 296,
    label = "C12H19-9 <=> C12H19-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.76e+10, 's^-1'),
        n = 0.21,
        Ea = (22.8446, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd
""",
)

entry(
    index = 297,
    label = "C12H17-13 <=> C12H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.86e+11, 's^-1'),
        n = 0.21,
        Ea = (58.827, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd
""",
)

entry(
    index = 298,
    label = "C13H19-3 <=> C13H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.73e+10, 's^-1'),
        n = 0.21,
        Ea = (61.4211, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd
""",
)

entry(
    index = 299,
    label = "C12H15-9 <=> C12H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.42e+10, 's^-1'),
        n = 0.21,
        Ea = (47.6139, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt
""",
)

entry(
    index = 300,
    label = "C13H17 <=> C13H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.76e+10, 's^-1'),
        n = 0.21,
        Ea = (51.8816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt
""",
)

entry(
    index = 301,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.54e+11, 's^-1'),
        n = 0.21,
        Ea = (12.9704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH
""",
)

