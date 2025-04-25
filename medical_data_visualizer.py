import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# 2
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)

df['overweight'] = (df['BMI'] > 25).astype(int)

#print(df)


# 3
# Normalize cholesterol
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

# Normalize gluc
df['gluc'] = (df['gluc'] > 1).astype(int)

#print(df)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars= 'cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight',])
    print(df_cat)
    


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    print(df_cat)

    

    # 7
    #print(df_long)

    fig = sns.catplot(
        data=df_cat, 
        kind="bar", 
        x="variable", 
        y="total", 
        hue="value", 
        col="cardio"
    )

    print(df_cat)
    plt.show



    # 8
    #fig = 


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    print(df)
    # 11
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] < df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] < df['weight'].quantile(0.975)) ]
    print('new')
    print(df_heat)
    #print("filter__________check")
    #print(df_heat[(df_heat['ap_lo'] > df_heat['ap_hi']) & (df_heat['height'] < df_heat['height'].quantile(0.025)) & (df['height'] > df['height'].quantile(0.975)) ])
    #print('original__________')
    #print(df[(df['ap_lo'] > df['ap_hi']) & (df['height'] < df['height'].quantile(0.025)) & (df['height'] < df['height'].quantile(0.975)) & (df['weight'] < df['weight'].quantile(0.025)) & (df['weight'] > df['weight'].quantile(0.975)) ])



    # 12
    corr = df_heat.corr()



    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0)
    plt.title("Correlation Matrix")
    plt.show()





    # 16
    fig.savefig('heatmap.png')
    return fig

#draw_cat_plot()
draw_heat_map()
