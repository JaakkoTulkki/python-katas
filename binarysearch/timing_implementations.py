import timeit

s = """
from binarysearch.while_loop import chop as while_chop
huge_list = list(range(10000))
assert(while_chop(7778, huge_list) == 7778)
"""

while_loop_time = timeit.timeit(stmt=s, number=1000)

s = """
from binarysearch.recursive import chop as recursive_chop
huge_list = list(range(10000))
assert(recursive_chop(7778, huge_list) == 7778)
"""

recursive_loop = timeit.timeit(stmt=s, number=1000)

s = """
huge_list = list(range(10000))
assert(huge_list.index(7778) == 7778)
"""

index_time = timeit.timeit(stmt=s, number=1000)

order = (('while_loop', while_loop_time), ('recursive loop', recursive_loop), ('index_time', index_time))

order = sorted(order, key=lambda x: x[1])
for index, value in enumerate(order):
    print("On position {} {} with time {}".format(str(index + 1), value[0], str(value[1])))
