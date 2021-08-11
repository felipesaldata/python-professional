def year_of_daily_effort(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        habit_and_time = args
        total_yearly = int(habit_and_time[1])*365
        print('At the end of the year you will practice ' + str(habit_and_time[0])+' a total of '+str(total_yearly)+' minutes!')
    return wrapper

@year_of_daily_effort
def daily_habit(habit: str, minutes: int) -> str: 
    print(f"your habit is {habit} for {minutes} minutes daily")
    
daily_habit("yoga",25)