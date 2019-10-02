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

        X = numpy.genfromtxt(data_file, delimiter = ',', names = True, dtype = int)
        state_names = X.dtype.names
        self.model = BayesianNetwork.from_structure(X = X.view((int, len(state_names))), structure = structure, state_names = state_names)

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
        print(self.model.predict_proba(evidence))
        self.model.predict_proba(evidence)
        return best_combo

# EU(Ad1, Ad2 | evidence) = sum over all s in S: P(S = s | evidence, Ad1, Ad2) * U(S = s)
# Need to find:
# 1. EU(Ad1 = 0, Ad2 = 0 | evidence)
# 2. EU(Ad1 = 0, Ad2 = 1 | evidence)
# 3. EU(Ad1 = 1, Ad2 = 0 | evidence)
# 4. EU(Ad1 = 1, Ad2 = 1 | evidence)
#
# 1: EU(Ad1 = 0, Ad2 = 0 | evidence) = P(S = 0 | evidence, Ad1 = 0, Ad2 = 0)*(0) + P(S = 1 | evidence, Ad1 = 0, Ad2 = 0)*(5000) + P(S = 2 | evidence, Ad1 = 0, Ad2 = 0)*(17760)
#
# --> go through the dec_vars for all the combinations we have to calculate (using itertools!)
# --> go through the util_map for each value: S = util_map[0] U(S = 0) = util_map[0] value?? idk how dictionaries work
# --> put each of the EUs into a dictionary or map and then return the combo that is max (best_combo)
# --> what does predict_proba return? Returns the probabilities of each variable in the graph given evidence.
#     - how do we get those probs?
#     - need to print what it returns

class AdEngineTests(unittest.TestCase):

    def test_defendotron_ad_engine_t1(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1", "Ad2"],
            structure = ((),(),(8, 0),(2,5),(9,1),(),(0,1),(),(1,),(6,)),
            util_map = {"S": {
                              0: 0,
                              1: 5000,
                              2: 17760
                              }
                        }
        )
        self.assertEqual(engine.decide({"T": 1}), {"Ad1": 0, "Ad2": 1})
        self.assertIn(engine.decide({"F": 1}), [{"Ad1": 1, "Ad2": 0},{"Ad1": 1, "Ad2": 1}])
        self.assertEqual(engine.decide({"G": 1, "T": 0}), {"Ad1": 1, "Ad2": 1})

    def test_defendotron_ad_engine_t2(self):
        engine = AdEngine(
            data_file = 'hw3_data.csv',
            dec_vars = ["Ad1"],
            structure = ((),(),(8, 0),(2,5),(9,1),(),(0,1),(),(1,),(6,)),
            util_map = {"S": {
                              0: 0,
                              1: 5000,
                              2: 17760
                              }
                        }
        )
        self.assertEqual(engine.decide({"A": 1}), {"Ad1": 0})
        self.assertEqual(engine.decide({"P": 1, "A": 0}), {"Ad1": 1})
        self.assertIn(engine.decide({"A": 1, "G": 0, "T": 1}), [{"Ad1": 0}, {"Ad1": 1}])

if __name__ == "__main__":
    unittest.main()
