import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simply DATA ")
upload=st.file_uploader("Chose csv file ",type="csv")

if upload is not None:
    df=pd.read_csv(upload)
    st.subheader("Data Preview")
    st.write(df.head(6))
    
    st.subheader('DataSummary')
    st.write(df.describe())
    
    st.subheader('Filter Data')
    col=df.columns.tolist()
    selc_col=st.selectbox("select columns filter by ",col)
    uniq=df[selc_col].unique()
    selected_val=st.selectbox("Select value",uniq)
    
    filter_df=df[df[selc_col]==selected_val]
    st.write(filter_df)
    
    st.subheader("plot data")
    x=st.selectbox("Select x-axis columns ",col)
    y=st.selectbox("Select y-axis columns ",col)
    
    if st.button("Plot"):
        st.line_chart(filter_df.set_index(x)[y])

else:
    st.write("waiting for file upload . . . ")
