
from ast import expr_context
from unicodedata import numeric
import unittest
import math
import src.labs.my_calc as calc

class TestSum(unittest.TestCase):

    def _testing(self,expr:str,rpn:str,answer: str | float | None = None) -> None:
        if answer is None:
            with self.assertRaises(Exception) as context:
                calc.rpn(expr)
            self.assertEqual(rpn,str(context.exception))
            with self.assertRaises(Exception) as context:
                calc.eval(expr)
            self.assertEqual(rpn,str(context.exception))
        else:
            self.assertEqual(rpn,' '.join(calc.rpn(expr)))
            if isinstance(answer,str):
                with self.assertRaises(Exception) as context:
                    calc.eval(expr)
                self.assertEqual(answer,str(context.exception))
            elif isinstance(answer,float):
                self.assertAlmostEqual(calc.eval(expr),answer)
        

    def test_eval_one_number(self) -> None:
        self._testing('42','42',42)

    def test_eval_variables(self) -> None:
        self._testing('e','e',math.e)
        self._testing('pi','pi',math.pi)
        self._testing('tau','tau',math.tau)

    def test_eval_two(self) -> None:
        self._testing('42 + 12','42 12 +',42 + 12)
        self._testing('42 * 12','42 12 *',42 * 12)
        self._testing('42 - 12','42 12 -',42 - 12)
        self._testing('42 / 12','42 12 /',42 / 12)
        self._testing('42 ^ 2','42 2 ^',42 ** 2)

    def test_priority(self) -> None:
        self._testing('2 + 2 * 2','2 2 2 * +',6)
        self._testing('2 + 2 ^ 3','2 2 3 ^ +',10)
        self._testing('2 + 2 / 3','2 2 3 / +',2.666666666666666666666)
        self._testing('5 + 4 * 3 ^ 2','5 4 3 2 ^ * +',41)
    
    def test_parentheses(self) -> None:
        self._testing('(2 + 2) * 2','2 2 + 2 *',8)
        self._testing('(2 + 2) ^ 3','2 2 + 3 ^',4 ** 3)
        self._testing('(2 + 2) / 3','2 2 + 3 /',4/3)
        self._testing('((5 + 4) * 3) ^ 2','5 4 + 3 * 2 ^',27 ** 2)

    def test_bracket_not_closed(self) -> None:
        self._testing('(2 + 2',"Скобка не была закрыта")

    def test_bracket_more_closed(self) -> None:
        self._testing('2 + 2)',"Лишняя закрывающая скобка")

    def test_unary_plus(self) -> None:
        self._testing('2 + + 2','2 2 u+ +',4)

    def test_unary_minus(self) -> None:
        self._testing('2 + - 3','2 3 u- +',-1)

    def test_double_operator(self) -> None:
        self._testing('2 * * 2',"Ожидался операнд, вместо '*'")

    def test_operator_at_end(self) -> None:
        self._testing('1 + 3 + 5 +',"Ожидался операнд в конце")

    def test_division_by_zero(self) -> None:
        self._testing('1/0','1 0 /','Деление на ноль')

    def test_incorrect_operand(self) -> None:
        self._testing('a','a',"Неизвестный операнд 'a'")

    def test_left_sub(self) -> None:
        self._testing('2 - 3 - 4','2 3 - 4 -',2 - 3 - 4)

    def test_left_div(self) -> None:
        self._testing('2 / 3 / 4','2 3 / 4 /',2 / 3 / 4)

    def test_right_pow(self) -> None:
        self._testing('3 ^ 3 ^ 3','3 3 3 ^ ^',3 ** (3 ** 3))

    def test_empty_string(self) -> None:
        self._testing('','Пустая строка')
        self._testing('   \t  ','Пустая строка')

if __name__ == '__main__':
    unittest.main()

