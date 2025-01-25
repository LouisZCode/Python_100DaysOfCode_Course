from datetime import datetime, timedelta

def day_count_date():

    d_t = datetime.today()
    d_y = d_t - timedelta(days=1)
    d_yy = d_t - timedelta(days=2)

    #how do we adjust so the data doesnt break when changing months,
    # aka, from 1 February, we cannot go -1
    #we use   .strftime('%Y-%m-%d') and timedelta above!

    #now we format them to look as in the data:
    current_day = d_t.strftime('%Y-%m-%d')
    day_before = d_y.strftime('%Y-%m-%d')
    day_beforebefore = d_yy.strftime('%Y-%m-%d')
    #checking:

    return day_before, day_beforebefore


#days = day_count_date()
#print(days)