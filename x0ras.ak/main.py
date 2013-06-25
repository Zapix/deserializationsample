# -*- coding: utf-8 -*-
import simplejson as json

import deserializators


if __name__ == '__main__':
    print "Sample of serialization"

    value = '<point><x>1</x><y>2</y><z>3</z></point>'
    print 'First method'
    print 'Input value: %s' % value
    result = deserializators.deserialize_to_point_first(value).to_dict()
    print 'Output value: %s' % result

    value = '<point><values x="4" y="5" z="6"/></point>'
    print 'Second method'
    print 'Input value: %s' % value
    result = deserializators.deserialize_to_point_second(value).to_dict()
    print 'Output value: %s' % json.dumps(result)
