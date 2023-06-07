all_functions=[]

no_bracket=[
    "channelID"
]

events=[
    "OnReady"
]

func_ARGtype=[
    "channelCreated"
]

func_RUNtype=[
    "Send"
]

symbols=[
    ("Lbracket", r'\['),
    ("Rbracket", r'\]'),
]

accepted_symbols=[
    "SPACE",
    "NEWLINE",
    "Text"
]

newline_char="*N*"


def all_things(all):
    all_functions.append(all)
    accepted_symbols.append(all)



def setup_symbols():
    for symbol in symbols: accepted_symbols.append(symbol)

def setup_functions():
    setup_symbols()

    for nb    in no_bracket:   func_ARGtype.append(nb)



    for event in events:       all_things(event)
    for fun   in func_ARGtype: all_things( fun )
    for fun   in func_RUNtype: all_things( fun )
    
    
    

