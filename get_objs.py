# code from https://utcc.utoronto.ca/~cks/space/blog/python/GetAllObjects
import sys, inspect, dill
import common_cache as cc
import inspect
from boltons import gcutils


# Recursively expand slist's objects
# into olist, using seen to track
# already processed objects.


class test:
    def __init__(self):
        self.myvar = "foo"

class test6:
    def __init__(self):
        self.myvar = "foo"


test2 = test()
test2.__dict__["obj_id"]="foo2"
print(test2.obj_id)

print(cc.__active_classes__)

#print(gcutils.get_all(type_obj=test, include_subtypes= False))
#cc.write(test2)


exit()