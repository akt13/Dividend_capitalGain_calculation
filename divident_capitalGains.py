import pandas as pd
import numpy as np
import json

with open('split_quarter.json', 'r') as f:
    data_ = json.load(f)


# maps the dividend to corresponding Quarter based on date
def findQuarter(divident_date):
    Q1_StartDate = pd.to_datetime(data_["Q1"][0])
    Q1_EndDate = pd.to_datetime(data_["Q1"][1])

    Q2_StartDate = pd.to_datetime(data_["Q2"][0])
    Q2_EndDate = pd.to_datetime(data_["Q2"][1])

    Q3_StartDate = pd.to_datetime(data_["Q3"][0])
    Q3_EndDate = pd.to_datetime(data_["Q3"][1])

    Q4_StartDate = pd.to_datetime(data_["Q4"][0])
    Q4_EndDate = pd.to_datetime(data_["Q4"][1])

    if (divident_date >= Q1_StartDate) & (divident_date <= Q1_EndDate):
        return 'Q1'
    if (divident_date >= Q2_StartDate) & (divident_date <= Q2_EndDate):
        return 'Q2'
    if (divident_date >= Q3_StartDate) & (divident_date <= Q3_EndDate):
        return 'Q3'
    elif (divident_date >= Q4_StartDate) & (divident_date <= Q4_EndDate):
        return 'Q4'
    return ''

# find total dividend earned in each quarter


def dividendSum(df):
    Q1_dividend = df.loc[df['Quarter'] == 'Q1', 'Net Dividend Amount'].sum()
    Q2_dividend = df.loc[df['Quarter'] == 'Q2', 'Net Dividend Amount'].sum()
    Q3_dividend = df.loc[df['Quarter'] == 'Q3', 'Net Dividend Amount'].sum()
    Q4_dividend = df.loc[df['Quarter'] == 'Q4', 'Net Dividend Amount'].sum()

    print('Q1_dividend = ', Q1_dividend, '\nQ2_dividend = ', Q2_dividend, '\nQ3_dividend = ', Q3_dividend,
          '\nQ4_dividend = ', Q4_dividend)


def main():
    reqCols = ['Symbol', 'Date', 'Quantity', 'Net Dividend Amount']

    # read Equity Dividends sheet of taxpnl export file after
    # skipping starting 14 rows
    df = pd.read_excel(data_["P&L_ExportName"],
                       sheet_name='Equity Dividends', skiprows=14, usecols=reqCols)

    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    df['Quarter'] = df['Date'].apply(findQuarter)

    dividendSum(df)


if __name__ == '__main__':
    main()
