import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")


df=pd.read_csv('india.csv')
list_of_state=list(df['State'].unique())
list_of_state.insert(0,'Overall India')
# st.title("INDIAn CENSUS 2011 VISULIZATION")
st.sidebar.markdown(
    """
    <h2 style='color:#ff4b4b;'>🔍 Filters </h2>
    <hr>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .card {
        background-color:  #ffcc99;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        font-size:30px;
        font-weight: bold;
        color:#000066;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='card'> INDIA CENSUS 2011 VISULIZATION </div>", unsafe_allow_html=True,)



selected_state=st.sidebar.selectbox('select a state',list_of_state)
parameter=sorted(df.columns[5:])
primary=st.sidebar.selectbox("select primary  parameter",parameter)
secondary=st.sidebar.selectbox("select secondary  parameter",parameter)
plot=st.sidebar.button("plot graph")
if plot:
    if selected_state=='Overall India':
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            hover_name="District",


            zoom=3.5,
            size_max=35,
            width=1200,
            height=680,
            mapbox_style="carto-positron"
        )
        st.plotly_chart(fig,use_container_width=True)


    else:
        state_df=df[df['State']==selected_state]
        st.markdown(
            """
            <style>
            .card1 {
                font-size:10px;
                font-weight: bold;
                color:#00ff00
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(f"""<div class='card1'>📍 Map shows {selected_state} data</div>""", unsafe_allow_html=True, )
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            hover_name="District",


            zoom=6,
            size_max=35,
            width=1200,
            height=680,
            mapbox_style="carto-positron"
        )
        st.plotly_chart(fig, use_container_width=True)






































































































































































































































































































































































































































































































































