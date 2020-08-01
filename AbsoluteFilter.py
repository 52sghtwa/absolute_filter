# based on 23.2.2.11 Writing a Frame Filter in version 10.0.50.20200731-git

import gdb

class FrameFilter():

    def __init__(self):
        # Frame filter attribute creation.
        #
        # 'name' is the name of the filter that GDB will display.
        #
        # 'priority' is the priority of the filter relative to other
        # filters.
        #
        # 'enabled' is a boolean that indicates whether this filter is
        # enabled and should be executed.

        self.name = "AbsoluteFilter"
        self.priority = 100
        self.enabled = False

        # Register this frame filter with the global frame_filters
        # dictionary.
        gdb.frame_filters[self.name] = self

    def filter(self, frame_iter):
        # Just return the iterator.
        return ElidingAbsolutesIterator(frame_iter)

class ElidingAbsolutesIterator:
    def __init__(self, ii):
        self.input_iterator = ii
        self.bottom = True
        self.skipped = False

    def __iter__(self):
        return self

    def __next__(self):
        frame = next(self.input_iterator)

        bottom = self.bottom
        self.bottom = False

        if bottom or not frame.filename().startswith("/"):
            self.skipped = False
            return frame
        else:
            if not self.skipped:
                print("...")
            self.skipped = True
            return next(self)

FrameFilter()
