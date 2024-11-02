import unittest
from runner import Runner
class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf( is_frozen, 'Тесты в этом кейсе замороженны' )
    def test_walk(self):
        walker_obj = Runner('Student')
        for i in range(10):
            walker_obj.walk()
        self.assertEqual(walker_obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе замороженны')
    def test_run(self):
        runner_obj = Runner('Sportsman')
        for i in range(10):
            runner_obj.run()
        self.assertEqual(runner_obj.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе замороженны')
    def test_challenge(self):
        walker_obj = Runner('Student')
        runner_obj = Runner('Sportsman')
        for i in range(10):
            walker_obj.walk()
            runner_obj.run()
        self.assertNotEqual(walker_obj.distance, runner_obj.distance)




