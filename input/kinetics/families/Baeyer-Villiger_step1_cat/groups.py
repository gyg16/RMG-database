#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step1_cat/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["ketone", "hydroperoxide", "acid"], products=["criegee", "acid2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*7', 1, '*8'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*5', -1, '*6'],
    ['CHANGE_BOND', '*5', 1, '*7'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*8'],
    ['FORM_BOND', '*4', 1, '*6']
])

entry(
    index = 1,
    label = "ketone",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2 *2 O     u0 {1,D}
3    [C,H] u0 {1,S}
4    [C,H] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "hydroperoxide",
    group =
"""
1    R u0 {2,S}
2    O u0 {1,S} {3,S}
3 *3 O u0 {2,S} {4,S}
4 *4 H u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "acid",
    group =
"""
1    R u0 {2,S}
2 *5 C u0 {1,S} {3,D} {4,S}
3 *6 O u0 {2,D}
4 *7 O u0 {2,S} {5,S}
5 *8 H u0 {4,S}
""",
    kinetics = None,
)

tree(
"""
L1: ketone
L1: hydroperoxide
L1: acid
"""
)

