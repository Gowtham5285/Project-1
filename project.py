import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dairy Milk Dashboard", layout="wide")
PLOT_WIDTH = 4
PLOT_HEIGHT = 2.2  # Fixed size for all charts

st.markdown("<h3 style='text-align:center;'>📊 Dairy Milk Visual Analytics Dashboard</h3>", unsafe_allow_html=True)

df = pd.read_csv("dairy_milk_data.csv")


st.sidebar.header("🛠 Filters")

region_filter = st.sidebar.multiselect(
    "Filter by Region",
    options=df["Region"].unique(),
    default=list(df["Region"].unique())
)

year_filter = st.sidebar.multiselect(
    "Filter by Year",
    options=df["Year"].unique(),
    default=list(df["Year"].unique())
)

month_filter = st.sidebar.multiselect(
    "Filter by Month",
    options=df["Month"].unique(),
    default=list(df["Month"].unique())
)

units_min, units_max = int(df["Sales_Units"].min()), int(df["Sales_Units"].max())
units_filter = st.sidebar.slider(
    "Filter by Units Sold",
    min_value=units_min, max_value=units_max,
    value=(units_min, units_max)
)

value_min, value_max = float(df["Sales_Value_USD"].min()), float(df["Sales_Value_USD"].max())
value_filter = st.sidebar.slider(
    "Filter by Sales Value (USD)",
    min_value=value_min, max_value=value_max,
    value=(value_min, value_max)
)

df = df[
    (df["Region"].isin(region_filter)) &
    (df["Year"].isin(year_filter)) &
    (df["Month"].isin(month_filter)) &
    (df["Sales_Units"].between(units_filter[0], units_filter[1])) &
    (df["Sales_Value_USD"].between(value_filter[0], value_filter[1]))
]

df_monthly = df.groupby("Month")["Sales_Value_USD"].sum()
df_region = df.groupby("Region")["Sales_Value_USD"].sum()
df_year = df.groupby("Year")["Sales_Value_USD"].sum()


def fix_size(fig, ax=None):
    fig.set_size_inches(PLOT_WIDTH, PLOT_HEIGHT)
    if ax:
        ax.set_aspect("auto")
    plt.tight_layout(pad=0)
    fig.subplots_adjust(wspace=0, hspace=0)
    return fig

def show(fig):
    fig = fix_size(fig)
    st.pyplot(fig, clear_figure=True)


charts = []

# 1 Line Chart
fig, ax = plt.subplots()
ax.plot(df_year.index, df_year.values)
charts.append(fix_size(fig, ax))

# 2 Bar Vertical
fig, ax = plt.subplots()
ax.bar(df_region.index, df_region.values)
charts.append(fix_size(fig, ax))

# 3 Bar Horizontal
fig, ax = plt.subplots()
ax.barh(df_region.index, df_region.values)
charts.append(fix_size(fig, ax))

# 4 Pie Chart
fig, ax = plt.subplots()
ax.pie(df_region.values, labels=df_region.index)
charts.append(fix_size(fig, ax))

# 5 Scatter
fig, ax = plt.subplots()
ax.scatter(df["Sales_Units"], df["Sales_Value_USD"])
charts.append(fix_size(fig, ax))

# 6 Histogram
fig, ax = plt.subplots()
ax.hist(df["Sales_Value_USD"], bins=10)
charts.append(fix_size(fig, ax))

# 7 Area Chart
fig, ax = plt.subplots()
ax.fill_between(df_year.index, df_year.values)
charts.append(fix_size(fig, ax))

# 8 Boxplot
fig, ax = plt.subplots()
ax.boxplot(df["Sales_Value_USD"])
charts.append(fix_size(fig, ax))

# 9 Violin Plot
fig, ax = plt.subplots()
sns.violinplot(y=df["Sales_Value_USD"], ax=ax)
charts.append(fix_size(fig, ax))

# 10 Heatmap
fig, ax = plt.subplots()
sns.heatmap(np.random.rand(4, 4), ax=ax)
charts.append(fix_size(fig, ax))

# 11 Polar Plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2*np.pi, len(df_monthly))
ax.plot(theta, df_monthly.values)
charts.append(fix_size(fig, ax))

# 12 Stackplot
fig, ax = plt.subplots()
ax.stackplot(df_year.index, [df_year.values * 0.3, df_year.values * 0.7])
charts.append(fix_size(fig, ax))

# 13 Step Plot
fig, ax = plt.subplots()
ax.step(df_year.index, df_year.values)
charts.append(fix_size(fig, ax))

# 14 Stem Plot
fig, ax = plt.subplots()
ax.stem(df_year.index, df_year.values)
charts.append(fix_size(fig, ax))

# 15 Error Bar
fig, ax = plt.subplots()
ax.errorbar(df_year.index, df_year.values, yerr=1000)
charts.append(fix_size(fig, ax))

# 16 Donut Chart
fig, ax = plt.subplots()
ax.pie(df_region.values, labels=df_region.index, wedgeprops=dict(width=0.4))
charts.append(fix_size(fig, ax))

# 17 Radar Chart
labels = df_region.index
values = np.concatenate((df_region.values, [df_region.values[0]]))
angles = np.linspace(0, 2*np.pi, len(values))
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, values)
charts.append(fix_size(fig, ax))

# 18 Grouped Bar
fig, ax = plt.subplots()
ax.bar(df_region.index, df_region.values, label="2024")
ax.bar(df_region.index, df_region.values * 0.9, label="2023")
ax.legend(fontsize=6)
charts.append(fix_size(fig, ax))

# 19 CDF Plot
fig, ax = plt.subplots()
ax.hist(df["Sales_Value_USD"], bins=20, density=True, cumulative=True)
charts.append(fix_size(fig, ax))

# 20 KDE Plot
fig, ax = plt.subplots()
sns.kdeplot(df["Sales_Value_USD"], ax=ax)
charts.append(fix_size(fig, ax))

# 21 Sorted Bar
fig, ax = plt.subplots()
sorted_vals = df_region.sort_values()
ax.bar(sorted_vals.index, sorted_vals.values)
charts.append(fix_size(fig, ax))

# 22 Lollipop Chart
fig, ax = plt.subplots()
ax.stem(sorted_vals.index, sorted_vals.values)
charts.append(fix_size(fig, ax))

# 23 Dual Axis Plot
fig, ax = plt.subplots()
ax.plot(df_year.index, df_year.values, label="Sales")
ax2 = ax.twinx()
ax2.bar(df_year.index, [10, 15, 20], alpha=0.3)
charts.append(fix_size(fig, ax))

# 24 Bubble Chart
fig, ax = plt.subplots()
ax.scatter(df["Sales_Units"], df["Sales_Value_USD"], s=df["Sales_Units"] / 10)
charts.append(fix_size(fig, ax))

for i in range(0, 24, 3):
    col1, col2, col3 = st.columns(3)
    with col1: show(charts[i])
    with col2: show(charts[i+1])
    with col3: show(charts[i+2])

st.markdown("<hr><p style='text-align:center;'>🎯 All charts displayed with equal size using Matplotlib</p>", 
            unsafe_allow_html=True)
