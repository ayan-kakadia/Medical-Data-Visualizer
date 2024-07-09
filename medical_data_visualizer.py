import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2) > 25
df["overweight"] = df["overweight"].astype(int)

# 3
df["cholesterol"] = df["cholesterol"] > 1
df["cholesterol"] = df["cholesterol"].astype(int)
df["gluc"] = df["gluc"] > 1
df["gluc"] = df["gluc"].astype(int)

# 4
def draw_cat_plot():
    # 5

    df_cat = pd.melt(df, id_vars=["id", "age", "sex", "height", "weight", "ap_hi", "ap_lo",  "cardio" ]).sort_values("variable")


    # 8
    fig = sns.catplot(x="variable",hue="value", data=df_cat, kind="count", col="cardio").set_axis_labels("variable", "total")
    fig=fig.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
            & (df['height'] >= df['height'].quantile(0.025))
            & (df['height'] <= df['height'].quantile(0.975))
            & (df['weight'] >= df['weight'].quantile(0.025))
            & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    
    # 13
    mask = np.triu(corr)


    # 14
    fig, ax = plt.subplots(figsize=(9,7))

    # 15
    sns.heatmap(corr, mask=mask,  fmt=".1f", annot=True)


    # 16
    fig.savefig('heatmap.png')
    return fig