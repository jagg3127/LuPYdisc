all_functions=[]

no_bracket=[
    "channelID"
]

events=[
    "OnReady"
]



func_ARGtype=[
    #--Built IN--
    "_ARGS",

    #--Channels--
    "channelCreated"

]

func_RUNtype=[
    "Send"
]

symbols=[
    ("Lbracket", r'\['),
    ("Rbracket", r'\]')
]

newline_char="*N*"




def all_things(all): all_functions.append(all)


def setup_functions():

    for nb    in no_bracket:   func_ARGtype.append(nb)



    for event in events:       all_things(event)
    for fun   in func_ARGtype: all_things( fun )
    for fun   in func_RUNtype: all_things( fun )
    
    
    

