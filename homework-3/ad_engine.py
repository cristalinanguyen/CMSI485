'''
ad_engine.py

CMSI 485 HW 3: Advertisement engine that selects from two
ad traits to maximize expected utility of converting a sale
for the Forney Industries Protectron 3001
'''

import itertools
import unittest
import math
import numpy as np
from pomegranate import *

class AdEngine:

    def __init__(self, data_file, structure, dec_vars, util_map):
        """
        Responsible for initializing the Decision Network of the
        AdEngine from the structure discovered by Tetrad
        """

        self.data_file = data_file
        self.structure = structure
        self.dec_vars = dec_vars
        self.util_map = util_map

        state_names = ["P","A","G","I","T","F","H","S","Ad1","Ad2"]

        P = State(P, name = "P")
        A = State(A, name = "A")
        G = State(G, name = "G")
        I = State(I, name = "I")
        T = State(T, name = "T")
        F = State(F, name = "F")
        H = State(H, name = "H")
        S = State(S, name = "S")
        Ad1 = State(Ad1, name = "Ad1")
        Ad2 = State(Ad2, name = "Ad2")

        X = numpy.genfromtxt('hw3_data.csv', delimiter = ',')
        model = BayesianNetwork.from_structure(X, structure, state_names)
        model.add_states(P, A, G, I, T, F, H, S, Ad1, Ad2)

    def decide(self, evidence):
        """
        Given some observed demographic "evidence" about a potential
        consumer, selects the ad content that maximizes expected utility
        and returns a dictionary over any decision variables and their
        best values

        :param dict evidence: dict mapping network variables to their
        observed values, of the format: {"Obs1": val1, "Obs2": val2, ...}
        :return: dict of format: {"DecVar1": val1, "DecVar2": val2, ...}
        """
        best_combo, best_util = None, -math.inf
        return best_combo


class AdEngineTests(unittest.TestCase):
    def test_defendotron_ad_engine_t1(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1", "Ad2"],
            structure = ((),(),("Ad1", "P"),("G","F"),("Ad2","A"),(),("P","A"),(),("A"),("H")),
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"T": 1}), {"Ad1": 0, "Ad2": 1})
        self.assertIn(engine.decide({"F": 1}), [{"Ad1": 1, "Ad2": 0},{"Ad1": 1, "Ad2": 1}])
        self.assertEqual(engine.decide({"G": 1, "T": 0}), {"Ad1": 1, "Ad2": 1})

    def test_defendotron_ad_engine_t2(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            # [!] Note: in this example, say we are only deciding upon the ad
            # video (Ad1); our engine's results should adapt accordingly (see
            # tests below)
            dec_vars = ["Ad1"],
            structure = ((),(),("Ad1", "P"),("G","F"),("Ad2","A"),(),("P","A"),(),("A"),("H")),
            # TODO: Decide what the utility map should be for the Defendotron
            # example; see format of util_map in spec and above!
            util_map = {"S": {0: 0, 1: 5000, 2: 17760}}
        )
        self.assertEqual(engine.decide({"A": 1}), {"Ad1": 0})
        self.assertEqual(engine.decide({"P": 1, "A": 0}), {"Ad1": 1})
        self.assertIn(engine.decide({"A": 1, "G": 0, "T": 1}), [{"Ad1": 0}, {"Ad1": 1}])

if __name__ == "__main__":
    unittest.main()
