class State(object):
    def __init__(self, initial):
        self.val = initial

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        self.val = val
        obj._update()
