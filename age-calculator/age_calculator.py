from datetime import date

while (True):
    year = int(input("Enter the year of birth "))
    month = int(input("Enter the month of birth "))
    day = int(input("Enter the date of birth "))

    t_year = date.today().year
    t_month = date.today().month
    t_day = date.today().day

    print("today year: " + str(t_year))
    print("today month: " + str(t_month))
    print("today day: " + str(t_day))

    age = (t_year - year)
    age = (t_month - month)
    age = (t_day - day)

    modified_t_year = t_year
    modified_t_month = t_month
    modified_t_day = t_day

    if t_day < day:
        modified_t_day = t_day + 30
        modified_t_month = t_month - 1

    if modified_t_month < month:
        modified_t_month = t_month + 12
        modified_t_year = t_year - 1

    print("modified today year: " + str(modified_t_year))
    print("modified today month: " + str(modified_t_month))
    print("modified today day: " + str(modified_t_day))

    age_year = modified_t_year - year
    age_month = modified_t_month - month
    age_day = modified_t_day - day

    print("Calculated Age: {} years {} months {} days".format(
        age_year, age_month, age_day))
