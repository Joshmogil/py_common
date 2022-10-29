import common_cache as cc
import timeit, sys, inspect
from boltons import gcutils

# Recursively expand slist's objects
# into olist, using seen to track
# already processed objects.


class test67:
    pass

test2 = test67()

obj_id = cc.write(test2)

new_obj = cc.read(obj_id=obj_id)

obj_id2 = cc.write(new_obj)
print(f"\n\n {obj_id} \n\n {obj_id2}")

#num = 1
#num_objs = len(cc.get_all())
#print(f"total num of objs: {num*num_objs}")
#time = timeit.timeit(cc.get_all, number=num)
#print(time)
#cc.write(test2)
#my_objs = cc.get_all(verbose=True)

#cc.write_all(verbose=True)