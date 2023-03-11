import datetime as dt                                                                                                   # import date and time librery

def time_formater (txt):                                                                                                # function string converter to time
    return dt.datetime.strptime(txt, "%H:%M")                                                                               # converts string to time

def text_formater (txt):                                                                                                # function for string format
    text = txt.strip().lower()                                                                                              # remove extra spaces and meka lower
    preFormetedText = text.translate({ord(i): None for i in '.,/-_!#@ -+=$"()'})                                            # remove unwonted symbols
    formatedText = list("".join(text))                                                                                      # spit strings by character    
    timeDetectHelper = formatedText.index(":")                                                                              # get ":" index
    result = "".join(formatedText[:(timeDetectHelper+3)])                                                                   # extract time as string
    if type(time_formater(result)) in (dt.datetime, dt.time) and len(preFormetedText) <= 5:                                 # check if string is real time value and do not includes am/pm
        return time_formater(result)                                                                                        # return string converted to time
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
