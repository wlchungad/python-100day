import gc

# manually trigger:
gc.collect()

# to disable automatic garbage collection
gc.disable()

# to enable:
gc.enable()

# to get all object monitered by GC
all_objects = gc.get_objects()
print(f"Number of tracked objects: {len(all_objects)}")

# some_object = list([])
# referrers = gc.get_referrers(some_object)

# print(f"Object is being referenced by: {referrers[:10]}")

