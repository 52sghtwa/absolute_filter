# absolute_filter
drop frames referring to sources in absolute paths

# use
add `source AbsoluteFilter.py` to your ~/.gdbinit

# motivation
debugging tokio programs in rust pollutes the stack trace with irrelevant frames, this simple heuristic of removing frames with absolute paths produces a reasonably clean stack trace
