import unittest
from unittest import mock
from unittest.mock import MagicMock
from input_text import read_input, print_text


class Test(unittest.TestCase):

    def test_input1(self):
         with mock.patch('builtins.input', return_value='test'):
             assert read_input() == 'test'


    @mock.patch('builtins.input', lambda *args: 'test')
    def test_input2(self):
        assert read_input() == 'test'



    @mock.patch('builtins.input', return_value='test')
    def test_input3(self, mock_input):
        assert read_input() == 'test'
        assert mock_input.call_count == 1
        assert mock_input.called


    def test_input4(self):

        mock_input = MagicMock(return_value='test')
        with mock.patch('builtins.input', mock_input):
            assert read_input() == 'test'



    def test_input5(self):
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'test'
    assert read_input() == 'test'


if __name__ == '__main__':
    unittest.main()
