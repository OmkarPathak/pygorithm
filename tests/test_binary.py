import unittest

from pygorithm.binary import (
    ascii,
    base2,
    base10,
    base16
)


class TestBase2(unittest.TestCase):
    def test_base2_to_ascii(self):
        array = ['01010100', '01101000', '01100101', '00100000', '01010001', '01110101', '01101001',
                 '01100011',
                 '01101011', '00100000', '01000010', '01110010', '01101111', '01110111', '01101110',
                 '00100000',
                 '01000110', '01101111', '01111000', '00100000', '01001010', '01110101', '01101101',
                 '01110000',
                 '01110011', '00100000', '01001111', '01110110', '01100101', '01110010', '00100000',
                 '01110100',
                 '01101000', '01100101', '00100000', '01001100', '01100001', '01111010', '01111001',
                 '00100000',
                 '01000100', '01101111', '01100111']

        self.assertEqual(base2.to_ascii(array), "The Quick Brown Fox Jumps Over the Lazy Dog")

    def test_base2_to_base10(self):
        self.assertEqual(base2.to_base10(1101001000101001), 53801)
        self.assertEqual(base2.to_base10(101111101011110000011111111), 99999999)
        self.assertEqual(base2.to_base10(10011110110001100001010001100101000000110001), 10910848929841)

    def test_base2_to_base16(self):
        self.assertEqual(base2.to_base16(1101001000101001), 'D229')
        self.assertEqual(base2.to_base16(101111101011110000011111111), '5F5E0FF')
        self.assertEqual(base2.to_base16(10011110110001100001010001100101000000110001), '9EC61465031')


class TestBase10(unittest.TestCase):
    def test_base10_to_base2(self):
        self.assertEqual(base10.to_base2(10), 1010)
        self.assertEqual(base10.to_base2(99999999), 101111101011110000011111111)
        self.assertEqual(base10.to_base2(1234567890), 1001001100101100000001011010010)

    def test_base10_to_base16(self):
        self.assertEqual(base10.to_base16(99999999), '5F5E0FF')
        self.assertEqual(base10.to_base16(1111111111111111111), 'F6B75AB2BC47207')
        self.assertEqual(base10.to_base16(34875439754935739457), '1E3FE73ADDA7B2001')
        self.assertEqual(base10.to_base16(3735928559), 'DEADBEEF')


class TestBase16(unittest.TestCase):
    def test_base16_to_base2(self):
        self.assertEqual(base16.to_base2('DEADBEEF'), 11011110101011011011111011101111)
        self.assertEqual(base16.to_base2('FFFFFFFFFFFFFFF'),
                         111111111111111111111111111111111111111111111111111111111111)
        self.assertEqual(base16.to_base2('23F235E865A45C'), 100011111100100011010111101000011001011010010001011100)

    def test_base16_to_base10(self):
        self.assertEqual(base16.to_base10('DEADBEEF'), 3735928559)
        self.assertEqual(base16.to_base10('FFFFFFFFFFFFFFF'), 1152921504606846976)
        self.assertEqual(base16.to_base10('23F235E865A45C'), 10117937531036764)

    def test_base16_to_ascii(self):
        array = ['54', '68', '65', '20', '51', '75', '69', '63', '6B', '20', '42', '72', '6F', '77', '6E', '20', '46',
                 '6F', '78', '20', '4A', '75', '6D', '70', '73', '20', '4F', '76', '65', '72', '20', '74', '68', '65',
                 '20', '4C', '61', '7A', '79', '20', '44', '6F', '67']

        array_2 = ['77', '48', '40', '74', '20', '5F', '54', '2D', '68', '33', '20', '2F', '2F', '2D', '46', '3D', '7E',
                   '21', '63', '6B']

        self.assertEqual(base16.to_ascii(array), "The Quick Brown Fox Jumps Over the Lazy Dog")
        self.assertEqual(base16.to_ascii(array_2), "wH@t _T-h3 //-F=~!ck")


class TestASCII(unittest.TestCase):
    def test_ascii_to_base16(self):
        array = ['54', '68', '65', '20', '51', '75', '69', '63', '6B', '20', '42', '72', '6F', '77', '6E', '20', '46',
                 '6F', '78', '20', '4A', '75', '6D', '70', '73', '20', '4F', '76', '65', '72', '20', '74', '68', '65',
                 '20', '4C', '61', '7A', '79', '20', '44', '6F', '67']

        array_2 = ['77', '48', '40', '74', '20', '5F', '54', '2D', '68', '33', '20', '2F', '2F', '2D', '46', '3D', '7E',
                   '21', '63', '6B']

        self.assertEqual(ascii.to_base16("The Quick Brown Fox Jumps Over the Lazy Dog"), array)
        self.assertEqual(ascii.to_base16("wH@t _T-h3 //-F=~!ck"), array_2)

    def test_ascii_to_base2(self):
        array = ['01010100', '01101000', '01100101', '00100000', '01010001', '01110101', '01101001',
                 '01100011',
                 '01101011', '00100000', '01000010', '01110010', '01101111', '01110111', '01101110',
                 '00100000',
                 '01000110', '01101111', '01111000', '00100000', '01001010', '01110101', '01101101',
                 '01110000',
                 '01110011', '00100000', '01001111', '01110110', '01100101', '01110010', '00100000',
                 '01110100',
                 '01101000', '01100101', '00100000', '01001100', '01100001', '01111010', '01111001',
                 '00100000',
                 '01000100', '01101111', '01100111']

        array_2 = ['01110111', '01001000', '01000000', '01110100', '00100000', '01011111', '01010100', '00101101',
                   '01101000',
                   '00110011', '00100000', '00101111', '00101111', '00101101', '01000110', '00111101', '01111110',
                   '00100001',
                   '01100011', '01101011']

        self.assertEqual(ascii.to_base2("wH@t _T-h3 //-F=~!ck"), array_2)
        self.assertEqual(ascii.to_base2("The Quick Brown Fox Jumps Over the Lazy Dog"), array)

if __name__ == '__main__':
    unittest.main()
