import unittest
import tests_12_1
import tests_12_2

file_testST = unittest.TestSuite()
file_testST.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
file_testST.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(file_testST)