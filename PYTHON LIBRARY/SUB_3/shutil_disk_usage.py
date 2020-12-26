
import shutil
total_b, used_b, free_b = shutil.disk_usage('.')
gib = 2 ** 30 # GiB == gibibyte
gb = 10 ** 9 # GB == gigabyte
print('Total: {:6.2f} GB {:6.2f} GiB'.format(total_b / gb, total_b / gib))
print('Used : {:6.2f} GB {:6.2f} GiB'.format(used_b / gb, used_b / gib))
print('Free : {:6.2f} GB {:6.2f} GiB'.format(free_b / gb, free_b / gib))


# The values returned by disk_usage() are given in bytes, so the example program converts
# them to more readable units before printing them.

