import unittest
from click.testing import CliRunner
from src.cli import main

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_analyze(self):
        result = self.runner.invoke(main, ['analyze', '--scope', 'path/to/scope'])
        self.assertEqual(result.exit_code, 0)

    def test_ocr(self):
        result = self.runner.invoke(main, ['ocr', '--scope', 'path/to/scope'])
        self.assertEqual(result.exit_code, 0)

    def test_cleanup(self):
        result = self.runner.invoke(main, ['cleanup', '--scope', 'path/to/scope'])
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()