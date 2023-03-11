import datetime as dt

def time_formater (txt):
    return dt.datetime.strptime(txt, "%H:%M")

def text_formater (txt):
    text = txt.strip().lower()
    preFormetedText = text.translate({ord(i): None for i in '.,/-_!#@ -+=$"()'})
    formatedText = list("".join(text))
    timeDetectHelper = formatedText.index(":")
    result = "".join(formatedText[:(timeDetectHelper+3)])
    if type(time_formater(result)) in (dt.datetime, dt.time) and len(preFormetedText) <= 5:
        return time_formater(result)
    elif type(time_formater(result)) in (dt.datetime, dt.time) and len(preFormetedText) > 5 \
            and "pm" in preFormetedText and result[0:2] == "12":
        return time_formater(result)
    elif type(time_formater(result)) in (dt.datetime, dt.time) and len(preFormetedText) > 5 \
            and "pm" in preFormetedText:
        return time_formater(str(int(result[:timeDetectHelper]) + 12) + result[timeDetectHelper:(timeDetectHelper + 3)])
    elif type(time_formater(result)) in (dt.datetime, dt.time) and len(preFormetedText) > 5:
        return time_formater(result)


def main():
    res = text_formater(input("What time is it now? "))

    if res >= time_formater("08:00") and res <=  time_formater("11:00"):
        print("Breakfast time")
    elif res >= time_formater("12:00") and res <=  time_formater("13:00"):
        print("Lanch Time")
    elif res >= time_formater("14:00") and res <=  time_formater("16:00"):
        print("Dinner Time")
    elif res >= time_formater("19:00") and res <= time_formater("21:00"):
        print("Supper Time")
    else:
        print("Stop eating")

main()

