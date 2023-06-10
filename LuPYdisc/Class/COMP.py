from rply import LexerGenerator, ParserGenerator
from LuPYdisc.Funcs.ALL import all_functions, symbols, No_Bracket, Run
from LuPYdisc.tools import FunctionHandler
import asyncio

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        for func in No_Bracket:
            self.lexer.add("##"+func, r'{}'.format(func))
        
        # functions
        for func in all_functions:
            self.lexer.add("^^"+func, r'{}'.format(func))
        
        

        
        
        # accept spaces
        self.lexer.add('SPACE', ' ')
        self.lexer.add("NEWLINE", '\n')


        for symbol in symbols:
            self.lexer.add(symbol[0], symbol[1])

        self.lexer.add('LINE_ARG', r"\*\*Line\d+")
        self.lexer.add('Text', r'[^;\[\]]+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()








async def token_file(line: int, ctx, client):
    line=client.FILE_LIST_OF_LINES[line-1]
    await format_command(line, ctx)





def words_in_string(word_list, a_string):
    for word in word_list:
        if word in a_string:
            return True
    return False

async def format_command(text:str, ctx=None):
    from LuPYdisc.Class.LuPYClient import _client
    stripped_command=[line.strip() for line in text.strip().split("\n") if line.strip() != '']; stripped_command.append("**")

    for num, line in enumerate(stripped_command):
        try:
            if (not words_in_string(Run, stripped_command[num+1]) and stripped_command[num+1].strip()!="**"):
                line+=" "+stripped_command[num+1]
                stripped_command.pop(num+1)
        except:pass
        if line == "**":continue

        lexer=Lexer().get_lexer()
        if line.strip() is None:continue
        tokens = lexer.lex(line.strip()+"\n")


        token_set1=[]
        for token in tokens:
            if token.gettokentype() == "LINE_ARG": await token_file(int(token.getstr().replace("**Line", "").strip()), ctx, _client)
            token_set1.append(
                {
                    token.gettokentype(): token.getstr()
                }
            )
        await find_brackets(token_set1, ctx)



def filter_brackets(text):
    results = {}
    filtered_text = text
    start = text.find('Lbracket')
    while start != -1:
        key_start = text.rfind('^^', 0, start)
        if key_start == -1:
            key_start = 0
        key_end = start
        key = text[key_start:key_end].strip()
        start += len('Lbracket')
        end = text.find('Rbracket', start)
        if end == -1:
            break
        value = text[start:end].strip()
        results[key] = value
        filtered_text = filtered_text.replace(text[start-len('Lbracket'):end+len('Rbracket')], '')
        start = text.find('Lbracket', end + len('Rbracket'))
    return results, filtered_text



async def find_brackets(tokens:list, ctx):
    string=""
    for token in tokens:
        token=dict(token)
        SYMBOL=str(list(token.keys())[0]).strip()
        TEXT  =str(list(token.values())[0])

        if SYMBOL in ["Text", "SPACE"]: string+=TEXT       ;continue
        else: string+=SYMBOL+" "

    string=string.replace("NEWLINE", " NEWLINE")
    key_pairs, string = filter_brackets(string)
    #print(key_pairs, "\n"+string)
    await run_funcs(string, key_pairs, ctx)

    
    
        
async def run_funcs(text:str, key_pairs, ctx):
    from LuPYdisc.Class.LuPYClient import _client
    text=text.replace("Rbracket", "").replace("Lbracket", "").strip()
    full_text=""
    Functions:FunctionHandler=_client.LUPY_FUNCS
    for words in text.split():
        if words in key_pairs and words.replace("^^", "") not in Run:
            arg=""
            for word in key_pairs[words].split():
                if word.startswith("##"):
                    word = str(await Functions.execute_functions(word.replace("##", "#^").strip(), None, ctx))
                arg+=word+" "
            words = str(await Functions.execute_functions(words.replace("^^", "#^").strip(), arg.strip(), ctx))
        
        elif words.startswith("##"):
            words = str(await Functions.execute_functions(words.replace("##", "#^").strip(), None, ctx))
        
        full_text+=words+" "

    for words in text.split():
        if words in key_pairs and words.replace("^^", "") in Run:
            arg2=""
            for word in key_pairs[words].split():
                if word.startswith("##"):
                    word = str(await Functions.execute_functions(word.replace("##", "#^").strip(), None, ctx))
                arg2+=word+" "
            await Functions.execute_functions(words.replace("^^", "#^").strip(), (arg2, full_text.replace(words, "").replace("NEWLINE", "").strip()), ctx)
       
    

        

