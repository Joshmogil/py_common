# code from https://utcc.utoronto.ca/~cks/space/blog/python/GetAllObjects
import sys, inspect, dill
import common_cache as cc
import inspect
from boltons import gcutils
# Recursively expand slist's objects
# into olist, using seen to track
# already processed objects.


class test:
    pass

test2 = test()

print(gcutils.get_all(type_obj=test, include_subtypes= False))
cc.write(test2)


exit()