import pandas as pd
import matplotlib.pyplot as plt
from base import engine 
import matplotlib as mpl
from  io import BytesIO

df = pd.read_sql_table('house', engine)

def count_top10():
    df_plot = pd.DataFrame(data=df['plot'].value_counts()).head(10).reset_index()
    df_plot.columns = ['plot', 'counts']
    #df_position.plot(df_position.city, kind='bar')
    #plt.show()
    return df_plot.to_dict('records')

def type():
    df_type = pd.DataFrame(data=df['type'].value_counts()).reset_index()
    df_type.columns = ['type', 'counts']
    df_type['percent'] = df_type['counts'] / df_type['counts'].sum()
    return df_type.to_dict('records')

def area():
    #df_area = pd.DataFrame(data=df['area'].value_counts()).reset_index()
    #df_area.columns = ['areas', 'counts']
    #df_area['areas'] = df_area['areas'].astype(str)
    return df.to_dict('records')

def rent():
    df_rent = df[['plot', 'type', 'rent']].sort_values(by='rent'
            ).groupby(['type', 'plot']).mean().reset_index()
    return df_rent.to_dict('records')

    
