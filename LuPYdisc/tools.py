from LuPYdisc.Functions      import all_functions
from LuPYdisc.Funcs.ARG_type import *
from LuPYdisc.Funcs.RUN_type import *
from LuPYdisc.Funcs.Events   import *



class FunctionHandler:

    def __init__(self):     self.functions = {}

    def register_functions(self):
        """#^"""
        for line in all_functions:
            function = eval(line)
            self.functions["#^"+line] = function

    async def execute_functions(self, keyword, args, context):
        """#^"""
        return await self.functions[keyword](args, context)