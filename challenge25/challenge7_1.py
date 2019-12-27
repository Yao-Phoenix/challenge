import pandas as pd

def co2():
    data = pd.read_excel('ClimateChange.xlsx')
    data = data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data = data.drop(data.columns[:5], axis=1)
    data = data.replace({'..': pd.np.nan})
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data['Sum emissions'] = data.sum(axis=1)
    country = pd.read_excel('ClimateChange.xlsx', sheetname='Country') \
            .set_index('Country code')
    df = pd.concat([data['Sum emissions'], country['Income group']], axis=1)
    sum_emissions = df.groupby('Income group').sum()
    df.insert(loc=0, column='Country name', value=country['Country name'])
    highest_emissions = df.sort_values(by='Sum emissions', ascending=False) \
            .groupby('Income group').head(1).set_index('Income group')
    highest_emissions.columns = ['Highest emission country', 'Highest emissions']
    lowest_emissions = df[df['Sum emissions'] > 0].sort_values(by='Sum emissions'
            ).groupby('Income group').head(1).set_index('Income group')
    lowest_emissions.columns = ['Lowest emission country', 'Lowest emissions']
    return pd.concat([sum_emissions, highest_emissions, lowest_emissions], 1)

if __name__ == '__main__':
    print(co2())
