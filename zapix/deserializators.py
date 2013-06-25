# -*- coding: utf-8 -*-
import xmltodict


def deserialize_point_first(value):
    """
    Deserialize xml of point to dict.
    Input value:
    <point>
        <x>X</x>
        <y>Y</y>
        <z>Z</z>
    </point>
    Output value:
    {
        'x': x,
        'y': y,
        'z': z
    }
    :param value: xml for parse
    :type value: str
    :return: built dictionary
    :rtype: dict
    """
    parsed_dict = xmltodict.parse(value)

    return {
        'x': int(parsed_dict['point']['x']),
        'y': int(parsed_dict['point']['y']),
        'z': int(parsed_dict['point']['z']),
    }


def deserialize_point_second(value):
    """
    Deserialize xml of point to dict.
    Input va;ue:
    <point>
        <values x="X", y="Y", z="Z" />
    </point>
    Output value:
    {
        'x': x,
        'y': y,
        'z': z
    }
    :param value: xml for parse
    :type value: str
    :return: built dictionary
    :rtype: dict
    """
    parsed_dict = xmltodict.parse(value)

    return {
        'x': int(parsed_dict['point']['values']['@x']),
        'y': int(parsed_dict['point']['values']['@y']),
        'z': int(parsed_dict['point']['values']['@z']),
    }
