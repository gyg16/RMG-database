#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "CH3OCH2O2 + CH3OCH2O2 <=> CH3OCH2O + O2 + CH3OCH2O",
    degeneracy = 1.0,
    kinetics=Arrhenius(
        A = (1.547e+23, 'cm^3/(mol*s)'),
        n = -4.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: CurranPentane""",
    longDesc =
u"""
Taken from entry: CH3OCH2O2 + CH3OCH2O2 <=> O2 + CH3OCH2O + CH3OCH2O
""",
)

entry(
    index = 2,
    label = "CH3O2 + CH3O2 <=> CH3O + O2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: CurranPentane""",
    longDesc = 
u"""
Taken from entry: CH3O2 + CH3O2 <=> O2 + CH3O + CH3O
""",
)

entry(
    index = 3,
    label = "C2H5O2 + C2H5O2 <=> C2H5O + O2 + C2H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (408, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc = 
u"""
Taken from entry: CH3CH2OO + CH3CH2OO <=> CH3CH2O + CH3CH2O + O2
""",
)

entry(
    index = 4,
    label = "C2H3O3 + CH3O2 <=> C2H3O2 + O2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc = 
u"""
Taken from entry: CH3C(O)OO + CH3OO <=> CH3C(O)O + CH3O + O2
""",
)

entry(
    index = 5,
    label = "C2H3O3 + HO2 <=> C2H3O2 + O2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1950, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry: CH3C(O)OO + HO2 <=> CH3C(O)O + OH + O2
""",
)
