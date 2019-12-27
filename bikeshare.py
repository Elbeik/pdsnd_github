import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for chicago, new york city, or washington?\n')
        city = city.lower()
        if city not in ('chicago','new york city','washington'):
            print('sorry your typing wrong city, please try again.')
            continue
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Wich month would you like to filter ? January, February, March, April, May, or June? or all iif you do not have any preference.')
        month = month.lower()
        if month not in ('january','february','march','april','may','june','july','august','october','november','desember','all'):        
            print('Sorry your typing wrong month, please try again.\n')
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to see filter? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or typing all if do have any preference. \n')
        day = day.lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('Sorry you wrote wrong day.')
            continue
        else:
            break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print('\nthe most common month is : ', most_month)


    # TO DO: display the most common day of week
    most_day_of_week = df['day_of_week'].mode()[0]
    print('\nthe most common day is : ', most_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['Start Time'].mode()[0]
    print('\nthe most hour is : ', most_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print('\nthe most start station is: ', most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print('\nthe most end station is: ', most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination = df.groupby(['Start Station','End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', most_start_station, " & ", most_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nmean travel time: ', mean_travel_time/60,"Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('\nthe user types: ',counts_user_types)


    # TO DO: Display counts of gender
    try:
         counts_gender = df['Gender'].value_counts()
         print('\nthe gender counts is: ',counts_gender)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nthe earliest year  is: ',earliest_year)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    try:
        most_year = df['Birth Year'].max()
        print('\nthe most recent year is: ',most_year)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nthe most common year is: ',most_common_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        S = 0
        E = 5

        while True:
            permision = input('\nWould you like to see some individual trip data ? type yes or no\n')
            raw_data = df[S:E]
            print(raw_data)
            S += 5
            E += 5
            if permision.lower() == 'no':
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
