#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "CH3O2 + CH3O2-2 <=> CH2O + O2 + CH4O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc = 
u"""
Taken from entry: CH3OO + CH3OO <=> CH3OH + CH2O + O2
""",
)

entry(
    index = 2,
    label = "C2H5O2 + C2H5O2-2 <=> C2H4O + O2 + C2H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.3e+09, 'cm^3/(mol*s)'), n=0, Ea=(-850, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc = 
u"""
Taken from entry: CH3CH2OO + CH3CH2OO <=> CH3CHO + CH3CH2OH + O2
""",
)
