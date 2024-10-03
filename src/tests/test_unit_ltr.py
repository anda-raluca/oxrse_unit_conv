import unittest
from oxrse_unit_conv.units import ltr, meter_cu


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(ltr.si_unit.matches(meter_cu))

    def test_basic_conversion(self):
        self.assertEqual(ltr.to_si(1), 0.001)
        self.assertAlmostEqual(ltr.to_unit(10, ltr), 10, 8)


if __name__ == '__main__':
    unittest.main()
