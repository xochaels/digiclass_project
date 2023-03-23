from turtle import left, right
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import streamlit as st

st.set_page_config(page_title='Profit and Sales Dashboard',
                  layout='wide',
                   page_icon=':bar_chart:')

df = pd.read_csv(r'D:\data_science\project\sales_and_profit\dataset\Orders.csv')

def cleaning_data(data):
    data.columns = data.columns.str.replace(' ','_')
    data.columns = data.columns.str.lower()
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = [data['order_date'][x].month for x in range(len(data['order_date']))]
    
    return data

def profit_month_per_year(year):
    data = cleaning_data(df)
    
    month_profit_sales_year = {'date' :['Januari','Februari','Maret','April', 'Mei', 'Juni', 'Juli', 
                       'Agustus', 'September', 'Oktober', 'November','Desember'],
                          'profit':[],
                          'sales':[]}
    
    tahun = data[(data['order_date'] >= f'1/1/{year}') & (data['order_date'] <= f'12/31/{year}')]
    sort_month = tahun.groupby(['month'])

    count=0
    for x in range(12):
        count+=1
        profit_month = sort_month.get_group(count)['profit'].sum()
        sales_month = sort_month.get_group(count)['sales'].sum()

        month_profit_sales_year['profit'].append(profit_month)
        month_profit_sales_year['sales'].append(sales_month)

    return pd.DataFrame(month_profit_sales_year)

def profit_all_month():
    
    data = cleaning_data(df)
    
    month_profit_sales = {'date' :pd.date_range('1-2014',periods=48,freq='m'),
                          'profit':[],
                          'sales':[]}
    
    for year in [14,15,16,17]:
        tahun = data[(data['order_date'] >= f'1/1/20{year}') & (data['order_date'] <= f'12/31/20{year}')]
        sort_month = tahun.groupby(['month'])
    
        count=0
        for x in range(12):
            count+=1
            profit_month = sort_month.get_group(count)['profit'].sum()
            sales_month = sort_month.get_group(count)['sales'].sum()
            
            month_profit_sales['profit'].append(profit_month)
            month_profit_sales['sales'].append(sales_month)

    return pd.DataFrame(month_profit_sales)

def visualization(data_filter,judul):
    fig, ax = plt.subplots(figsize = (10,5))

    plt.title(judul)
    plt.xticks(rotation=45)

    ax2 = ax.twinx()

    ax.plot(data_filter['date'],data_filter['profit'], color='g', marker='o')
    ax2.plot(data_filter['date'],data_filter['sales'], color='b', marker='o')

    ax.set_xlabel('Rentang Waktu', color = 'r')
    ax.set_ylabel('Profit', color = 'g')

    ax2.set_ylabel('Sales', color = 'b')

    plt.tight_layout()

    plt.show()

#Main Page
st.title(':bar_chart: Sales dan Profit')

#sidebar

month_per_year = st.sidebar.radio(
    'Pilih Tahun',
    ('2014','2015','2016','2017','All Years')
)

if month_per_year == '2014':
    tahun_2014 = profit_month_per_year(2014)
    
    total_sales_2014= int(tahun_2014['sales'].sum())
    total_profit_2014= int(tahun_2014['profit'].sum())
    
    left_column, right_coulumn = st.columns(2)
    with left_column:
        st.subheader('Total Sales :')
        st.subheader(f'US $ {total_sales_2014:,}')
    with right_coulumn:
        st.subheader('Total Profit :')
        st.subheader(f'US $ {total_profit_2014:,}')
    
    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(
        go.Line(y=tahun_2014['profit']),
        row=1, col=1
    )

    fig.add_trace(
        go.Line(y=tahun_2014['sales']),
        row=1, col=2
    )

    fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")    
    st.plotly_chart(fig, use_container_width=True)
        
    st.dataframe(tahun_2014)
elif month_per_year == '2015':
    tahun_2015 = profit_month_per_year(2015)
    
    total_sales_2015= int(tahun_2015['sales'].sum())
    total_profit_2015= int(tahun_2015['profit'].sum())
    
    left_column, right_coulumn = st.columns(2)
    with left_column:
        st.subheader('Total Sales :')
        st.subheader(f'US $ {total_sales_2015:,}')
    with right_coulumn:
        st.subheader('Total Profit :')
        st.subheader(f'US $ {total_profit_2015:,}')
    
    st.dataframe(tahun_2015)
elif month_per_year == '2016':
    tahun_2016 = profit_month_per_year(2016)
    
    total_sales_2016= int(tahun_2016['sales'].sum())
    total_profit_2016= int(tahun_2016['profit'].sum())
    
    left_column, right_coulumn = st.columns(2)
    with left_column:
        st.subheader('Total Sales :')
        st.subheader(f'US $ {total_sales_2016:,}')
    with right_coulumn:
        st.subheader('Total Profit :')
        st.subheader(f'US $ {total_profit_2016:,}')
    
    st.dataframe(tahun_2016)
elif month_per_year == '2017':
    tahun_2017 = profit_month_per_year(2017)
    
    total_sales_2017= int(tahun_2017['sales'].sum())
    total_profit_2017= int(tahun_2017['profit'].sum())
    
    left_column, right_coulumn = st.columns(2)
    with left_column:
        st.subheader('Total Sales :')
        st.subheader(f'US $ {total_sales_2017:,}')
    with right_coulumn:
        st.subheader('Total Profit :')
        st.subheader(f'US $ {total_profit_2017:,}')
    
    st.dataframe(tahun_2017)
else:
    all_month = profit_all_month()
    
    total_sales_all_month= int(all_month['sales'].sum())
    total_profit_all_month= int(all_month['profit'].sum())
    
    left_column, right_coulumn = st.columns(2)
    with left_column:
        st.subheader('Total Sales :')
        st.subheader(f'US $ {total_sales_all_month:,}')
    with right_coulumn:
        st.subheader('Total Profit :')
        st.subheader(f'US $ {total_profit_all_month:,}')
    
    st.dataframe(all_month)



