import pandas as pd
import matplotlib.pyplot as plt
from base import engine 
import matplotlib as mpl
from  io import BytesIO

df = pd.read_sql_table('job', engine)

def count_top10():
    df_position = pd.DataFrame(data=df['city'].value_counts()).reset_index()
    df_position.columns = ['city', 'counts']
    #df_position.plot(df_position.city, kind='bar')
    #plt.show()
    return df_position.to_dict('records')

def salary_top10():
    df['salary'] = (df['salary_lower'] + df['salary_upper']) / 2
    df_salary = df[['city', 'salary']].groupby('city').mean().sort_values(
            'salary', ascending=False).head(10).reset_index()
    #df_salary.plot(df_salary.city, kind='bar')
    #plt.show()
    return df_salary.to_dict('records')

def hot_tags():
    df_tag = []
    for tag in df['tags']:
        if len(tag) > 0:
            df_tag.extend(tag.split(' '))
    tags = pd.DataFrame(data=df_tag, columns=['tags'])
    df_tags = pd.DataFrame(data=tags['tags'].value_counts()).reset_index().head(10)
    df_tags.columns = ['tags', 'counts']
    return df_tags

def hot_tags_plot():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    query = hot_tags()
    query.plot.bar(query.tags)

    img = BytesIO()
    plt.savefig(img, format='png')
    return img.getvalue()

def experience():
    df['experience'] = df['experience_lower'
            ].astype(str) +'-' + df['experience_upper'].astype(str) + '年'
    df_experience = pd.DataFrame(data=df['experience'].value_counts()).reset_index()
    df_experience.columns = ['experience', 'counts']
    df_experience['percent'] = df_experience['counts'] / df_experience['counts'].sum()
    print('--------------------------------------------------')
    print(df_experience.to_dict('records'))
    print('--------------------------------------------------')
    return df_experience.to_dict('records')

def education():
    df_education = pd.DataFrame(data=df['education'].value_counts()).reset_index()
    df_education.columns = ['education', 'counts']
    df_education['percent'] = df_education['counts'] / df_education['counts'].sum()
    return df_education.to_dict('records')

def same_education_different_cities_salary():
    df['salary'] = (df['salary_lower'] + df['salary_upper']) / 2
    df_salary_ = df[['city', 'salary', 'education']].sort_values(by='education'
            ).groupby(['city', 'education']).mean().reset_index()
    df_salary_['salary'] = round(df_salary_['salary'], 1)
    return df_salary_.to_dict('records')
    
