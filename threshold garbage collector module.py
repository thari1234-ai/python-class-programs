import gc
gc.enable()  # Enable garbage collection
gc.disable()  # Disable garbage collection temporarily
l1 = [1, 2, 3]
d1 = {'a': 1, 'b': 2}
s1 = "garbage collection"
# Deleting the objects
del l1
del d1
del s1
# Set custom garbage collection thresholds
gc.set_threshold(700, 10, 10)
# Print the current garbage collection thresholds
print(gc.get_threshold())
# Trigger garbage collection manually and get the number of collected objects
collected = gc.collect()
print(collected)  # Print the number of collected objects
