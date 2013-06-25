# -*- coding: utf-8 -*-
import unittest

import point
import deserializators


class PointTestCase(unittest.TestCase):

    def test_point_to_dict(self):
        new_point = point.Point(1, 2, 3)
        point_dict = new_point.to_dict()

        for key in ('x', 'y', 'z'):
            self.assertIn(key, point_dict)

        for key, value in (('x', 1), ('y', 2), ('z', 3)):
            self.assertEqual(point_dict[key], value)


class DeserializatorsTestCase(unittest.TestCase):

    def test_first_method(self):
        value = '<point><x>1</x><y>2</y><z>3</z></point>'
        result = deserializators.deserialize_to_point_first(value)
        self.assertTrue(isinstance(result, point.Point))

    def test_second_method(self):
        value = '<point><values x="1", y="2", z="3"/></point>'