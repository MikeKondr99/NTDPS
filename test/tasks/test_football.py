import unittest
from src.tasks.football import GamesData

class TestSum(unittest.TestCase):

    def test_lose_match(self):
        gd = GamesData()
        gd.add_data('Спартак',4,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 0 0 1 0')
        self.assertEqual(gd.get_info('Зенит'),'1 1 0 0 3')

    def test_win_match(self):
        gd = GamesData()
        gd.add_data('Спартак',7,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 1 0 0 3')
        self.assertEqual(gd.get_info('Зенит'),'1 0 0 1 0')

    def test_tie_match(self):
        gd = GamesData()
        gd.add_data('Спартак',6,'Зенит',6) 
        self.assertEqual(gd.get_info('Спартак'),'1 0 1 0 1')
        self.assertEqual(gd.get_info('Зенит'),'1 0 1 0 1')

    def test_accumulative_win(self):
        gd = GamesData()
        gd.add_data('Спартак',7,'Зенит',6) 
        gd.add_data('Спартак',13,'',2)
        self.assertEqual(gd.get_info('Спартак'),'2 2 0 0 6')

    def test_no_info(self):
        gd = GamesData()
        self.assertEqual(gd.get_info('Спартак'),None)

    def test_example(self):
        gd = GamesData()
        gd.add_data_str('Спартак;9;Зенит;10')
        gd.add_data_str('Локомотив;12;Зенит;3')
        gd.add_data_str('Спартак;8;Локомотив;15')
        self.assertEqual(gd.get_info('Спартак'),'2 0 0 2 0')
        self.assertEqual(gd.get_info('Зенит'),'2 1 0 1 3')
        self.assertEqual(gd.get_info('Локомотив'),'2 2 0 0 6')
        self.assertEqual(gd.get_info('Челси'),None)

    def test_allinfo(self):
        gd = GamesData()
        gd.add_data_str('Спартак;9;Зенит;10')
        gd.add_data_str('Локомотив;12;Зенит;3')
        gd.add_data_str('Спартак;8;Локомотив;15')
        self.assertEqual(gd.get_all_info(),"Зенит: 2 1 0 1 3\nЛокомотив: 2 2 0 0 6\nСпартак: 2 0 0 2 0")



    


if __name__ == '__main__':
    unittest.main()