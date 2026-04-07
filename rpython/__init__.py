# XXX Check for win64:
# The win64 port of PyPy/RPython requires sys.maxint == sys.maxsize,
# this differs from the CPython implementation
# see comment at the top of rpython.rlib.rarithmetic for details
import sys
import builtins
builtins.unicode = str
builtins.unichr = chr
builtins.long = int
builtins.xrange = range
builtins.basestring = str
builtins.intern = sys.intern
builtins.cmp = lambda a, b: (a > b) - (a < b)
builtins.coerce = lambda a, b: (float(a), float(b)) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else NotImplemented
builtins.buffer = memoryview
sys.maxint = sys.maxsize
if hasattr(sys, "maxint") and hasattr(sys, "maxsize"):
    if sys.maxint != sys.maxsize:
        raise Exception(
            "Translating on win64 requires either a modified CPython "
            "(so-called CPython64/64) or a working win64 build of PyPy2.")
