from datetime import datetime as D_T
from pytz import timezone

timezones = (
    timezone('EST'),
    timezone('UTC'),
    timezone('US/Pacific')
)

def format_datetime(datetime: D_T, FORM: str, TIMEZONE):
    UnformatedDatetime = datetime.astimezone(TIMEZONE)
    UnformatedDatetimeTuple = (
        UnformatedDatetime.year, UnformatedDatetime.month, UnformatedDatetime.day, UnformatedDatetime.hour, UnformatedDatetime.minute,
        UnformatedDatetime.second, UnformatedDatetime.microsecond)
    year, month, day, hour, minute, second, microsecond = UnformatedDatetimeTuple

    AM_PM = "AM" if hour < 12 else "PM"
    hour = hour if hour < 12 else hour - 12
    hour+=1

    FORM = FORM.lower().strip()

    if FORM == "full":
        desiredDateForm = f"USA: {month}/{day}/{year} at {hour} :{minute} :{second} :{microsecond} {AM_PM}"
    elif FORM == "year":
        desiredDateForm = str(year)
    elif FORM == "month":
        desiredDateForm = str(month)
    elif FORM == "day":
        desiredDateForm = str(day)
    elif FORM == "hour":
        desiredDateForm = str(hour)
    elif FORM == "minute":
        desiredDateForm = str(minute)
    elif FORM == "second":
        desiredDateForm = str(second)
    elif FORM == "microsecond":
        desiredDateForm = str(microsecond)
    elif FORM == "ampm":
        desiredDateForm = AM_PM
    else:
        desiredDateForm = "ERROR"
    return desiredDateForm

async def channelCreated(args: str, Context):
    if len(args) < 1:
        raise SyntaxError("No parameter provided for '$channelCreated'")
    est, utc, pst = timezones
    try:
        ID, TIME, FORM = tuple(args.split(" "))
        TIME = locals()[TIME.strip()]
        FORM = FORM.lower()
    except ValueError:
        FORM="full"
        try:
            ID, TIME = tuple(args.split(" "))
            TIME = locals()[TIME.strip()]
        except:
            ID   = args
            TIME = utc

    
    from LuPYdisc.Class.LuPYClient import _client
    try:
        int(ID)
        channel = await _client.fetch_channel(ID)

        desiredDateForm = format_datetime(channel.created_at, FORM, TIME)
        if desiredDateForm != "ERROR":
            return desiredDateForm
        else:
            raise SyntaxError("Invalid Format option in $channelCreated!")

    except ValueError:
        print("ERRORS")
