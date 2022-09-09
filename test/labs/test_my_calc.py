
from ast import expr_context
import unittest
import math
import src.labs.my_calc as calc

class TestSum(unittest.TestCase):

    def test_eval_one_number(self) -> None:
        self.assertAlmostEqual(calc.eval('42'),42)

    def test_eval_variables(self) -> None:
        self.assertAlmostEqual(calc.eval('e'),math.e)
        self.assertAlmostEqual(calc.eval('pi'),math.pi)
        self.assertAlmostEqual(calc.eval('tau'),math.tau)

    def test_eval_two(self) -> None:
        self.assertAlmostEqual(calc.eval('42 + 12'),42 + 12)
        self.assertAlmostEqual(calc.eval('42 * 12'),42 * 12)
        self.assertAlmostEqual(calc.eval('42 - 12'),42 - 12)
        self.assertAlmostEqual(calc.eval('42 / 12'),42 / 12)
        self.assertAlmostEqual(calc.eval('42 ^ 2'),42 ** 2)

    def test_priority(self) -> None:
        self.assertAlmostEqual(calc.eval('2 + 2 * 2'),6)
        self.assertAlmostEqual(calc.eval('2 + 2 ^ 3'),10)
        self.assertAlmostEqual(calc.eval('2 + 2 / 3'),2.666666666666666666666)
        self.assertAlmostEqual(calc.eval('5 + 4 * 3 ^ 2'),41)
    
    def test_parentheses(self) -> None:
        self.assertAlmostEqual(calc.eval('(2 + 2) * 2'),8)
        self.assertAlmostEqual(calc.eval('(2 + 2) ^ 3'),4 ** 3)
        self.assertAlmostEqual(calc.eval('(2 + 2) / 3'),4/3)
        self.assertAlmostEqual(calc.eval('((5 + 4) * 3) ^ 2'),27 ** 2)

    def test_bracket_not_closed(self) -> None:
        with self.assertRaises(Exception,) as context:
            calc.eval('(2 + 2')
        expected = "'(' has not been closed"
        self.assertEqual(expected,str(context.exception))

    def test_bracket_more_closed(self) -> None:
        with self.assertRaises(Exception) as context:
            calc.eval('2 + 2)')
        self.assertEqual("')' is unexpected ",str(context.exception))

    def test_unary_plus(self) -> None:
        self.assertEqual(calc.eval('2 + + 2'),4)

    def test_unary_minus(self) -> None:
        self.assertEqual(calc.eval('2 + - 3'),-1)

    def test_double_operator(self) -> None:
        with self.assertRaises(Exception) as context:
            calc.eval('2 * * 2')
        self.assertEqual(f"expected operand not '*'",str(context.exception))

    def test_double_operator_at_end(self) -> None:
        with self.assertRaises(Exception) as context:
            calc.eval('1 + 3 + 5 +')
        self.assertEqual(f"expected operand at the end",str(context.exception))

    def test_double_operator_at_end(self) -> None:
        with self.assertRaises(Exception) as context:
            calc.eval('4 / (5 - 3 - 2)')
        self.assertEqual(f"division by zero",str(context.exception))

    def test_double_operator_at_end(self) -> None:
        with self.assertRaises(Exception) as context:
            calc.eval('a')
        self.assertEqual(f"incorrect operand 'a'",str(context.exception))

if __name__ == '__main__':
    unittest.main()


