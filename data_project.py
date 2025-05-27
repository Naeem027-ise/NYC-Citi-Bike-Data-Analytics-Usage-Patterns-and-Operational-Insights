import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('file.csv')

#print(df.head(5))


df.describe()
df.info()

df['started_at'] = pd.to_datetime(df['started_at']) # Convert date columns to datetime
df['ended_at'] = pd.to_datetime(df['ended_at'])


df['hour'] = df['started_at'].dt.hour
df['day_of_week'] = df['started_at'].dt.day_name()

# date columns 
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# ride duration
df['ride_duration'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

df = df[df['ride_duration'] > 0]

# hour and day of week columns
df['hour'] = df['started_at'].dt.hour
df['day_of_week'] = df['started_at'].dt.day_name()

# T-test to compare the mean ride durations between members and casual users
members = df[df['member_casual'] == 'member']['ride_duration']
casuals = df[df['member_casual'] == 'casual']['ride_duration']
t_stat, p_value = stats.ttest_ind(members, casuals)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Pearson corr. ride duration vs the hour of the day
correlation, p_value_corr = stats.pearsonr(df['ride_duration'], df['hour'])
print(f"Correlation: {correlation}")
print(f"P-value: {p_value_corr}")

# Generate a corr. ride  duration vs hour
correlation_matrix = df[['ride_duration', 'hour']].corr()
print(correlation_matrix)

for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].astype('category').cat.codes
 
correlation_matrix = df.corr()
 
# heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

