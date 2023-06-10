async def channelID(empty, ctx):
    try:
        int(ctx.channel.id)
    except ValueError:
        raise SyntaxError("NONE")
    return ctx.channel.id