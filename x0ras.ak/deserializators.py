# -*- coding: utf-8 -*-
import xmltodict

import point


def deserialize_to_point_first(value):
    """
    Deserialize xml to point
    Input value:
    <point>
        <x>X</x>
        <y>Y</y>
        <z>Z</z>
    </point>
    :param value: xml for parse
    :type value: str
    :return: created point
    :rtype: :class:`point.Point`
    """
    parsed_dict = xmltodict.parse(value)

    return point.Point(
        x=parsed_dict['point']['x'],
        y=parsed_dict['point']['y'],
        z=parsed_dict['point']['z']
    )


def deserialize_to_point_second(value):
    """
    Deserialize xml to point
    Input value:
    <point>
        <values x="X" y="Y" z="Z"/>
    </point>
    :param value: xml for parse
    :type value: str
    :return: created point
    :rtype: :class:`point.Point`
    """
    parsed_dict = xmltodict.parse(value)
    return point.Point(
        x=parsed_dict['point']['values']['@x'],
        y=parsed_dict['point']['values']['@y'],
        z=parsed_dict['point']['values']['@z']
    )
