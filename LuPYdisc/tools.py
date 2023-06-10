from LuPYdisc.Funcs    import OBJ_function

class FunctionHandler:

    def __init__(self):     self.functions = {}

    def register_functions(self):
        """#^"""
        for func in OBJ_function:
            self.functions["#^"+func.__name__] = func

    async def execute_functions(self, keyword, args, context):
        """#^"""
        try:
            return await self.functions[keyword](args, context)
        except Exception as e:
            print(e, "In command", context.command.name)

def _ARGS(args, ctx):
    print(args)