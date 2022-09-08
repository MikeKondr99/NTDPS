from cmath import exp
import unittest
from src.tasks.football import GamesData

class TestFootball(unittest.TestCase):

    def test_lose_match(self) -> None:
        gd = GamesData()
        gd.add_data('Спартак',4,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 0 0 1 0')
        self.assertEqual(gd.get_info('Зенит'),'1 1 0 0 3')

    def test_win_match(self) -> None:
        gd = GamesData()
        gd.add_data('Спартак',7,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 1 0 0 3')
        self.assertEqual(gd.get_info('Зенит'),'1 0 0 1 0')

    def test_tie_match(self) -> None:
        gd = GamesData()
        gd.add_data('Спартак',6,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 0 1 0 1')
        self.assertEqual(gd.get_info('Зенит'),'1 0 1 0 1')

    def test_accumulative_win(self) -> None:
        gd = GamesData()
        gd.add_data('Спартак',7,'Зенит',6) 
        gd.add_data('Спартак',13,'',2)
        self.assertEqual(gd.get_info('Спартак'),'2 2 0 0 6')

    def test_no_info(self) -> None:
        gd = GamesData()
        self.assertEqual(gd.get_info('Спартак'),None)

    def test_example(self) -> None:
        gd = GamesData()
        gd.add_data_str('Спартак;9;Зенит;10')
        gd.add_data_str('Локомотив;12;Зенит;3')
        gd.add_data_str('Спартак;8;Локомотив;15')
        self.assertEqual(gd.get_info('Спартак'),'2 0 0 2 0')
        self.assertEqual(gd.get_info('Зенит'),'2 1 0 1 3')
        self.assertEqual(gd.get_info('Локомотив'),'2 2 0 0 6')
        self.assertEqual(gd.get_info('Челси'),None)

    def test_allinfo(self) -> None:
        gd = GamesData()
        gd.add_data_str('Спартак;9;Зенит;10')
        gd.add_data_str('Локомотив;12;Зенит;3')
        gd.add_data_str('Спартак;8;Локомотив;15')
        result = set(gd.get_all_info().split('\n'))
        expected = {'Зенит: 2 1 0 1 3','Локомотив: 2 2 0 0 6','Спартак: 2 0 0 2 0'}
        expected2 = {'Локомотив: 2 2 0 0 6','Зенит: 2 1 0 1 3','Спартак: 2 0 0 2 0'}
        self.assertEqual(result,expected)
        self.assertEqual(result,expected2)



    


if __name__ == '__main__':
    unittest.main()