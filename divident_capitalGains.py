import pandas as pd
import numpy as np

# read Equity Dividends sheet of taxpnl export file after
# skipping starting 14 rows

reqCols = ['Symbol', 'Date', 'Quantity', 'Net Dividend Amount']
df = pd.read_excel('taxpnl-BR1239.xlsx',
                   sheet_name='Equity Dividends', skiprows=14, usecols=reqCols)

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')


# maps the dividend to corresponding Quarter based on date
def findQuarter(date_):
    Q1_StartDate = pd.to_datetime('2021-04-01')
    Q1_EndDate = pd.to_datetime('2021-06-30')

    Q2_StartDate = pd.to_datetime('2021-07-01')
    Q2_EndDate = pd.to_datetime('2021-09-30')

    Q3_StartDate = pd.to_datetime('2021-10-01')
    Q3_EndDate = pd.to_datetime('2021-12-31')

    Q4_StartDate = pd.to_datetime('2022-01-01')
    Q4_EndDate = pd.to_datetime('2022-03-31')

    if (date_ >= Q1_StartDate) & (date_ <= Q1_EndDate):
        return 'Q1'
    if (date_ >= Q2_StartDate) & (date_ <= Q2_EndDate):
        return 'Q2'
    if (date_ >= Q3_StartDate) & (date_ <= Q3_EndDate):
        return 'Q3'
    elif (date_ >= Q4_StartDate) & (date_ <= Q4_EndDate):
        return 'Q4'
    return ''


df['Quarter'] = df['Date'].apply(findQuarter)

#find total dividend earned in each quarter
Q1_dividend = df.loc[df['Quarter'] == 'Q1', 'Net Dividend Amount'].sum()
Q2_dividend = df.loc[df['Quarter'] == 'Q2', 'Net Dividend Amount'].sum()
Q3_dividend = df.loc[df['Quarter'] == 'Q3', 'Net Dividend Amount'].sum()
Q4_dividend = df.loc[df['Quarter'] == 'Q4', 'Net Dividend Amount'].sum()

print('Q1_dividend = ', Q1_dividend, '\nQ2_dividend = ', Q2_dividend, '\nQ3_dividend = ', Q3_dividend,
      '\nQ4_dividend = ', Q4_dividend)
