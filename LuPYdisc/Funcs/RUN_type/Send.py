from LuPYdisc.Functions import newline_char

async def Send(text: tuple, Context):
    ID   = text[0]
    text = text[1]
    from LuPYdisc.Class.LuPYClient import client

    try:
        
        channel = await client.fetch_channel(int(ID))
        message = text.replace(newline_char, "\n")
        await channel.send(message)
    except:
        raise SyntaxError("Can't send empty message!")
    return