# -*- coding: utf-8 -*-
import deserializators

if __name__ == '__main__':
    print "Sample of serialization"

    value = '<point><x>1</x><y>2</y><z>3</z></point>'
    print 'First method'
    print 'Input value: ', value
    print 'Output value: ', deserializators.deserialize_point_first(value)

    value = '<point><values x="4" y="5" z="6"/></point>'
    print 'Second method'
    print 'Input value: ', value
    print 'Output value:', deserializators.deserialize_point_second(value)
