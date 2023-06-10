
async def Send(text: tuple, Context):
    ID   = text[0]
    text = text[1]
    from LuPYdisc.Class.LuPYClient import _client

    try:
        channel = await _client.fetch_channel(int(ID))
        message = text.replace(_client.newline_char+" ", "\n").replace(_client.newline_char, "\n")
        await channel.send(message)
    except:
        raise SyntaxError("Can't send empty message!")
    return