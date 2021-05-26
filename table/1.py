import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

workouts = pd.read_csv('workouts.csv', parse_dates=['start_at'])
users = pd.read_excel('users.xlsx')

# сразу создадим новый датафрейм, в котором соединены уроки и пользователи

workouts_users = pd.merge(workouts, users,
                          how='left',
                          left_on='client_id', right_on='user_id')

trainings_by_day = workouts

print(trainings_by_day)
