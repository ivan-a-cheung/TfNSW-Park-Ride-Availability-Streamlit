import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="NSW Park & Ride Carpark Availability Tracker",
    layout="wide",

)

show_pages(
    [
        Page("streamlit_app.py", "Home"),
        Page("pages/carpark_app.py", "Test"),
        Page("pages/carpark_app.py", "About"),
    ]
)

with st.sidebar:
    st.markdown("Created by Ivan Cheung")
    st.caption("Copyright 2024")

with st.container():
    st.title('NSW Park&Ride Carpark Availability Tracker')

    st.markdown('This app displays real-time data on the number of free parking spaces for NSW Park & Ride Carparks. Select from the carparks below to see the real-time availability data:')
    st.markdown('# ')

col1, col2, col3 = st.columns(3)


with st.container():
    with col1:
        st.subheader("North Western Sydney")
        st.button("Bella Vista Car Park", key=31)
        st.button("Cherrybrook Car Park", key=33)
        st.button("Hills Showground Car Park", key=32)
        st.button("Kellyville (North & South Car Park)", key=29)
        st.button("Tallawong (P1, P2 & P3 Car Park)", key=26)

    with col2:
        st.subheader("Northern Sydney & North Shore")
        st.button("Hornsby Jersey St Car Park", key=25)
        st.button("Gordon Henry St North Car Park", key=6)
        st.button("West Ryde Car Park", key=14)

    with col3:
        st.subheader("Northern Beaches")
        st.button("Brookvale Car Park", key=490)
        st.button("Dee Why Car Park", key=13)
        st.button("Manly Vale Car Park", key=489)
        st.button("Mona Vale Car Park", key=12)
        st.button("Narrabeen Car Park", key=11)
        st.button("Warriewood Car Park", key=10)

with st.container():
    st.markdown('# ')

col4, col5, col6 = st.columns(3)

with st.container():
    with col4:
        st.subheader("Western Sydney & Richmond")
        st.button("Penrith Combewood Car Park", key=21)
        st.button("Schofields Car Park", key=24)
        st.button("Seven Hills Car Park", key=488)
        st.button("St Marys Car Park", key=18)


    with col5:
        st.subheader("South Western Sydney")
        st.button("Campbelltown  (Farrow Rd & Hurley Street Car Park)", key=19)
        st.button("Edmondson Park South Car Park", key=17)
        st.button("Leppington Car Park", key=16)
        st.button("Revesby Car Park", key=9)
        st.button("Warwick Farm Car Park", key=23)


    with col6:
        st.subheader("Southern Sydney")
        st.button("Kogarah Car Park", key=487)
        st.button("Sutherland East Parade Car Park", key=15)

with st.container():
    st.markdown('# ')

col7, col8, col9 = st.columns(3)

with st.container():
    with col7:
        st.subheader("Inner West")
        st.button("Ashfield Car Park", key=486)


    with col8:
        st.subheader("Central Coast")
        st.button("Gosford Car Park", key=8)

    with col9:
        st.subheader("Illawarra Region")
        st.button("Kiama Car Park", key=7)