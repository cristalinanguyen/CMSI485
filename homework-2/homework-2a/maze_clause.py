# AUTHORS: CRISTALINA NGUYEN, AMELIA JAY
'''
maze_clause.py

Specifies a Propositional Logic Clause formatted specifically
for Grid Maze Pathfinding problems. Clauses are a disjunction of
MazePropositions (2-tuples of (symbol, location)) mapped to
their negated status in the sentence.
'''
import unittest

class MazeClause:

    def __init__(self, props):
        """
        Constructor parameterized by the propositions within this clause;
        argument props is a list of MazePropositions, like:
        [(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)]
        """
        self.props = {}
        self.valid = False
        for p in props:
            if p[0] in self.props and self.props[p[0]] != p[1]:
                self.valid = True
                self.props = {}
                break
            self.props[p[0]] = p[1]

    def get_prop(self, prop):
        """
        Returns:
          - None if the requested prop is not in the clause
          - True if the requested prop is positive in the clause
          - False if the requested prop is negated in the clause
        """
        if self.valid:
            return None
        return self.props[prop] if prop in self.props else None

    def is_valid(self):
        """
        Returns:
          - True if this clause is logically equivalent with True
          - False otherwise
        """
        return self.valid

    def is_empty(self):
        """
        Returns:
          - True if this is the Empty Clause
          - False otherwise
        (NB: valid clauses are not empty)
        """
        if self.valid or bool(self.props):
            return False
        return True

    def __eq__(self, other):
        """
        Defines equality comparator between MazeClauses: only if they
        have the same props (in any order) or are both valid
        """
        return self.props == other.props and self.valid == other.valid

    def __hash__(self):
        """
        Provides a hash for a MazeClause to enable set membership
        """
        # Hashes an immutable set of the stored props for ease of
        # lookup in a set
        return hash(frozenset(self.props.items()))

    # Hint: Specify a __str__ method for ease of debugging (this
    # will allow you to "print" a MazeClause directly to inspect
    # its composite literals)
    # def __str__ (self):
    #     return ""

    @staticmethod
    def resolve(c1, c2):
        """
        Returns a set of MazeClauses that are the result of resolving
        two input clauses c1, c2 (Hint: result will only ever be a set
        of 0 or 1 MazeClause, but it being a set is convenient for the
        inference engine)
        """
        def not_resolved(p, combined):
            result = set()
            for x in combined:
                if x[0] != p:
                    result.add(x)
            return result

        for p in c1.props:
            c1prop = c1.get_prop(p)
            c2prop = c2.get_prop(p)
            if c2prop is not None and c1prop != c2prop:
                combined = list(c1.props.items()) + list(c2.props.items())
                newClause = MazeClause(not_resolved(p, combined))
                if not newClause.is_valid():
                    return {newClause}
        return set()

class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        self.assertTrue(mc.get_prop(("X", (1, 1))))
        self.assertTrue(mc.get_prop(("X", (2, 1))))
        self.assertFalse(mc.get_prop(("Y", (1, 2))))
        self.assertTrue(mc.get_prop(("X", (2, 2))) is None)
        self.assertFalse(mc.is_empty())

    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.get_prop(("X", (1, 1))))
        self.assertFalse(mc.is_empty())

    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.is_valid())
        self.assertTrue(mc.get_prop(("X", (1, 1))) is None)
        self.assertFalse(mc.is_empty())

    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.is_valid())
        self.assertTrue(mc.is_empty())

    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)

    def test_mazeprops7(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)

    def test_mazeprops8(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops9(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops10(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True), (("W", (1, 1)), False)]) in res)

if __name__ == "__main__":
    unittest.main()
