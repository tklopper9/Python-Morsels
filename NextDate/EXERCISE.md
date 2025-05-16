It's sometimes hard to know when you should make a class and when you should just make a couple of functions. We're going to make a class and some functions (in bonus 3) which serve the same purpose.

I'd like you to make a class called NextDate which will help figure out the date and number of days (from today) until the next given weekday.

I'd actually like you to make two classes: NextDate and Weekday. The Weekday class just exists to store some data: it will have attributes that represent each weekday.

So if it's Friday December 31, 1999 and we want to figure out when next Thursday is, we could do this:

```
from datetime import date

from nextdate import NextDate, Weekday

date.today()
datetime.date(1999, 12, 31)

next_thursday = NextDate(Weekday.THURSDAY)

next_thursday.days_until()
6

next_thursday.date()
datetime.date(2000, 1, 6)
```

When the current date changes, these methods should update their values as well. For example on Saturday January 1, 2000, it should only be 5 days until next Thursday:

```
date.today()
datetime.date(2000, 1, 1)

next_thursday.days_until()
5
```

If the current date matches the given weekday, the date returned should be today and days_until should return 0.