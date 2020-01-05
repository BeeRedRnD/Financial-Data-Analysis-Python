import matplotlib
matplotlib.use
import matplotlib.pyplot as mpl


import pandas as pd

# Just making the plots look better
mpl.style.use('ggplot')
mpl.rcParams['figure.figsize'] = (8,6)
mpl.rcParams['font.size'] = 12



def header(msg):
    print('*' * 150)
    print('[ ' + msg + ' ]')

# Read the Fair Users CSV file into a dataframe
fair_users_filename = 'fair_users.csv'
fair_users_df = pd.read_csv(fair_users_filename)

# Read the Fraudster Users CSV file into a dataframe
fraud_users_filename = 'fraud_users.csv'
fraud_users_df = pd.read_csv(fraud_users_filename)

# Read the Transactions by Fair Users CSV file into a dataframe
transactions_fair_users_filename = 'transactions_by_fair_users.csv'
transactions_fair_users_df = pd.read_csv(transactions_fair_users_filename)

# Read the Transactions by Fraudster Users CSV file into a dataframe
transactions_fraud_users_filename = 'transactions_by_fraudsters.csv'
transactions_fraud_users_df = pd.read_csv(transactions_fraud_users_filename)


# Print the first and last 5 rows from the Fair Users data frame
header("Top 5 rows of Fair Users")
print(fair_users_df.head())
print('*' * 150)

header("Last 5 rows of Fair Users")
print(fair_users_df.tail())
print('*' * 150)

# Print the first and last 5 rows from the Fraudsters Users data frame
header("Top 5 rows of Fraudster Users")
print(fraud_users_df.head())
print('*' * 150)

header("Last 5 rows of Fraudsters Users")
print(fraud_users_df.tail())
print('*' * 150)


#Print statistical summary of columns of Fair Users
header("Statistical Summary of Fair Users")
print(fair_users_df.describe())
print('*' * 150)

#Print statistical summary of columns of Fraudster Users
header("Statistical Summary of Fraudster Users")
print(fraud_users_df.describe())
print('*' * 150)

# 1. Comparison between Countries of Fair and Fraudster Users Bar Charts below
fair_users_df['country'].value_counts().plot.bar();
mpl.show()

fraud_users_df['country'].value_counts().plot.bar();
mpl.show()

# 2. Comparison between KYC (Know your customer) of Fair and Fraudster Users Bar Charts below
fair_users_df['kyc'].value_counts().plot.bar();
mpl.show()

fraud_users_df['kyc'].value_counts().plot.bar();
mpl.show()

# 3. Comparison between Birth Year of Fair and Fraudster Users Bar Charts below
fair_users_df['birth_year'].value_counts().plot.bar();
mpl.show()

fraud_users_df['birth_year'].value_counts().plot.bar();
mpl.show()


# 4. Comparison between State of Transactions made by Fair and Fraudster Users
transactions_fair_users_df['state'].value_counts().plot.bar();
mpl.show()

transactions_fraud_users_df['state'].value_counts().plot.bar();
mpl.show()


# 5. Comparison between Amount Spent by Fair and Fraudster Users
transactions_fair_users_df['amount'].plot.line();
mpl.show()

transactions_fraud_users_df['amount'].plot.line();
mpl.show()

# 6. Comparison between Merchant Category of Fair and Fraudster Users
transactions_fair_users_df['merchant_category'].value_counts().plot.bar();
mpl.show()

transactions_fraud_users_df['merchant_category'].value_counts().plot.bar();
mpl.show()


print(fair_users_df['failed_sign_in_attempts'].corr(transactions_fraud_users_df['amount']))






# print(df[df['STATE'] == 'LOCKED'].tail(5))
#
# print(df['STATE'].corr(df['PHONE_COUNTRY']))

# print(df['KYC'].value_counts())
#
# df['KYC'].value_counts().plot.bar();
# mpl.show()
#
# df['BIRTH_YEAR'].value_counts().plot.bar();
# mpl.show()
#
# df['COUNTRY'].value_counts().plot.bar();
# mpl.show()

# Correlation between Merchant Country and State of Transaction for Fair and Fraudster Users
# transactions_fair_users_df.plot.scatter(x='merchant_country', y='state');
# mpl.show()


#print(transactions_fraud_users_df.corr())
