import sys
import ctypes
import struct


a = 1


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__itet__'):
      if hasattr(x, 'items'):
          for xx in x.items():
              show_size(xx, level +1)
      elif not isinstance(x, str):
          for xx in x:
              show_size(xx, level + 1)


show_size(a)