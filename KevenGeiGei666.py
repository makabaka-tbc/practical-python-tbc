def countdayofyear(year, month, day, sumofday=0):

    if __name__ == "__main__":
        year = int(input("year"))
        month = int(input("month"))
        day = int(input("day"))

    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    try:
        if 0 < month <= 12 and 0 < day <= 31 and year > 0:
            sumofday += months[month - 1]
            sumofday += day
            if month > 2 and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                sumofday += 1
        else:
            return "date error"
        return sumofday
    except TypeError:
        print("format error")


print(countdayofyear(input(), input(), input()))
