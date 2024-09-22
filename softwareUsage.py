import streamlit as st
import pandas as pd
import plotly.express as px

data_file = 'data.xlsx'
df = pd.read_excel(data_file)

st.title("Software Usage Dashboard")
st.write("A dashboard to monitor software installations, usage, and costs in the IT department.")

# KPIs in the sidebar
st.sidebar.header("Key Performance Indicators")

st.sidebar.metric(label="Total Licenses", value=df['Software_Name'].count())
st.sidebar.metric(label="Active Licenses", value=df[df['License_Status'] == 'Active'].shape[0])
st.sidebar.metric(label="Expired Licenses", value=df[df['License_Status'] == 'Expired'].shape[0])
st.sidebar.metric(label="Licenses Expiring Soon", value=df[(df['License_Validity_Days_Left'] > 0) & (df['License_Validity_Days_Left'] <= 30)].shape[0])
st.sidebar.metric(label="Total License Cost", value=f"${df['License_Cost'].sum():,.2f}")
st.sidebar.metric(label="Average License Cost", value=f"${df['License_Cost'].mean():,.2f}")
st.sidebar.metric(label="Total Usage Hours", value=f"{df['Usage_Hours'].sum():,.2f} hours")
st.sidebar.metric(label="Most Expensive Software", value=df.loc[df['License_Cost'].idxmax()]['Software_Name'])

st.header("Visualizations")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Most Used Software (by Usage Hours)")
    usage_by_software = df.groupby('Software_Name')['Usage_Hours'].sum()
    fig1 = px.pie(values=usage_by_software, names=usage_by_software.index, title="Usage by Hours", hole=0.3)
    st.plotly_chart(fig1)

with col4:
    st.subheader("Most Costly Software (by Total Cost)")
    cost_by_software = df.groupby('Software_Name')['License_Cost'].sum()
    fig2 = px.pie(values=cost_by_software, names=cost_by_software.index, title="Costs by Software", hole=0.3)
    st.plotly_chart(fig2)

col5, _ = st.columns([1, 0.1])

with col5:
    st.subheader("Most Used Software (by Number of Users)")
    users_by_software = df.groupby('Software_Name')['User'].nunique()
    fig3 = px.pie(values=users_by_software, names=users_by_software.index, title="Users per Software", hole=0.3)
    st.plotly_chart(fig3)

st.header("Department-wise Analytics")
col6, col7 = st.columns(2)

with col6:
    st.subheader("Installations by Department")
    installations_by_department = df['Department'].value_counts()
    st.bar_chart(installations_by_department)

with col7:
    st.subheader("License Cost by Department")
    cost_by_department = df.groupby('Department')['License_Cost'].sum()
    st.bar_chart(cost_by_department)

st.subheader("Total Usage Hours by Department")
usage_by_department = df.groupby('Department')['Usage_Hours'].sum()
st.bar_chart(usage_by_department)

st.subheader("Licenses Expiring Soon (within next 30 days)")
expiring_licenses_df = df[(df['License_Validity_Days_Left'] > 0) & (df['License_Validity_Days_Left'] <= 30)]
st.dataframe(expiring_licenses_df[['Software_Name', 'User', 'Department', 'License_Validity_Days_Left']])
