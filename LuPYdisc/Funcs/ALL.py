from LuPYdisc.Funcs.Events  import __all__ as _EVENTS; import  LuPYdisc.Funcs.Events as _EVENT
from LuPYdisc.Funcs.NO_ARG  import __all__ as _XARGX ; import  LuPYdisc.Funcs.NO_ARG as _NO_ARG
from LuPYdisc.Funcs.ARGtype import __all__ as _ARGS  ; import LuPYdisc.Funcs.ARGtype as _ARGtype
from LuPYdisc.Funcs.RUNtype import __all__ as _RUN   ; import LuPYdisc.Funcs.RUNtype as _RUNtype


Events        = [getattr(_EVENT ,  f).__name__  for f in  _EVENTS if not f.startswith("_")]
No_Bracket    = [getattr(_NO_ARG,  f).__name__  for f in   _XARGX if not f.startswith("_")]
Args          = [getattr(_ARGtype, f).__name__  for f in    _ARGS if not f.startswith("_")]
Run           = [getattr(_RUNtype, f).__name__  for f in     _RUN if not f.startswith("_")]
all_functions = [      *Events,    *No_Bracket,    *Args,    *Run                         ]


_Events        = [getattr(_EVENT ,  f)  for f in  _EVENTS if not f.startswith("_")]
_No_Bracket    = [getattr(_NO_ARG,  f)  for f in   _XARGX if not f.startswith("_")]
_Args          = [getattr(_ARGtype, f)  for f in    _ARGS if not f.startswith("_")]
_Run           = [getattr(_RUNtype, f)  for f in     _RUN if not f.startswith("_")]
OBJ_function   = [*_Events, *_No_Bracket,  *_Args,  *_Run                         ]




symbols=[
    ("Lbracket", r'\['),
    ("Rbracket", r'\]')
]



newline_char="*N*"


def print_all_current_functions():
    list_of_functions = [  "Events",  "No_Bracket",  "Args",  "Run",  "all_functions" ]

    printed_funcs     = [func+": "+repr(globals()[func]) for func in list_of_functions]
    
    string            = "\n".join(printed_funcs)
    lines             = string.split("\n")
    keys              = [line.split(": ")[0] for line in lines]
    values            = [line.split(": ")[1] for line in lines]
    max_value         = max(values, key=len)
    sorted_keys       = sorted(keys, key=len)
    for key in sorted_keys:
        print((key + " ").ljust(14) + ": " + values[keys.index(key)].ljust(len(max_value) + 1))
    
    print(OBJ_function)