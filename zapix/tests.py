# -*- coding: utf-8 -*-
import unittest

import deserializators


class DeserializatorsTestCase(unittest.TestCase):

    def is_dict_a_point(self, value):
        """
        Checks is dict have got keys 'x', 'y', 'z'
        """
        self.assertIn('x', value)
        self.assertIn('y', value)
        self.assertIn('z', value)

    def test_deserialization_first(self):
        input_xml = '<point><x>3</x><y>4</y><z>6</z></point>'
        result = deserializators.deserialize_point_first(input_xml)

        self.is_dict_a_point(result)

        for key, value in (('x', 3), ('y', 4), ('z', 6)):
            self.assertEqual(result[key], value)

    def test_deserialization_second(self):
        input_xml = '<point><values x="3" y="4" z="5"/></point>'
        result = deserializators.deserialize_point_second(input_xml)

        self.is_dict_a_point(result)

        for key, value in (('x', 3), ('y', 4), ('z', 5)):
            self.assertEqual(result[key], value)
