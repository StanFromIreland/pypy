class InstanceMethod(object):
    "Like types.InstanceMethod, but with a reasonable (structural) equality."

    def __init__(self, im_func, im_self, im_class):
        self.__func__ = im_func
        self.__self__ = im_self
        self.__self__.__class__ = im_class

    def __call__(self, *args, **kwds):
        firstarg = self.__self__
        if firstarg is None:
            if not args or not isinstance(args[0], self.__self__.__class__):
                raise TypeError(
                    "must be called with %r instance as first argument" % (
                    self.__self__.__class__,))
            firstarg = args[0]
            args = args[1:]
        return self.__func__(firstarg, *args, **kwds)

    def __eq__(self, other):
        return isinstance(other, InstanceMethod) and (
            self.__func__ == other.__func__ and
            self.__self__ == other.__self__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__func__, self.__self__))
