
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[2]:


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
        try:
            city = input('Please enter the city you are interested in (Chicago, New York City or Washington): ').lower()
            if city =='chicago'or city=='new york city' or city=='washington':
                break
        except ValueError:
            print('This\'s not a valid input!')
        else: 
            print('Incorrect input. Try again!\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter the month you would like to filter (all, January, February, March, April, May, June): ').lower()
            if month =='january'or month=='february'or month=='march'or month=='april'or month=='may'or month=='june'or month =='all':
                break
        except ValueError:
            print('This\'s not a valid input!')
        else: 
            print('Incorrect input. Try again!\n')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('please enter the day you would like to filter (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ').lower()
            if day=='monday'or day=='tuesday'or day=='wednesday'or day=='thursday'or day=='friday'or day=='saturday'or day=='sunday'or day=='all':    
                break
        except ValueError:
            print('This\'s not a valid input!')
        else: 
            print('Incorrect input. Try again!\n')
    

    print('-'*40)
    return city, month, day


# In[3]:


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

    print('\nCalculating The Most Frequent Times of Travel...\n')
        
     # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week: ', common_day)
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()

    # TO DO: display the most common start hour on the filtered day
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', common_sstation)
    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('Most commonly used end station: ', common_estation)
    # TO DO: display most frequent combination of start station and end station trip
    rows = df.shape[0]
    station_count = np.repeat(1,rows)
    df['Count'] = station_count
    grouped = df.groupby(['Start Station','End Station']).count()
    idx = grouped['Count'].idxmax()

    print('Most frequent route is from {} to {} '.format(idx[0],idx[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_time)
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    except KeyError:
        print('Missing data in the original files. Check other cities for statistics of users\' genders.')
        print('-'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth: ',earliest_year)
        print('Most recent year of birth: ',recent_year)
        print('Most common year of birth: ',common_year)
    except KeyError:
        print('Missing data in the original files. Check other cities for statistics of users\' birth years.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

