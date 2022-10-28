import common_cache as cc
import timeit
from boltons import gcutils
# Recursively expand slist's objects
# into olist, using seen to track
# already processed objects.


class test:
    pass

test2 = test()


#num = 1
#num_objs = len(cc.get_all())
#print(f"total num of objs: {num*num_objs}")
#time = timeit.timeit(cc.get_all, number=num)
#print(time)

my_objs = cc.get_all(verbose=True)

cc.write_all(verbose=True)