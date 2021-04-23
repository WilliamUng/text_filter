import streamlit as st
from multiapp import MultiApp
from apps import keyphrase, data_stats # import your app modules here

app = MultiApp()

st.set_page_config(page_title='Dashboard', layout='wide', initial_sidebar_state = 'auto')
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>', unsafe_allow_html=True)

# Add all your application here
app.add_app("Key phrases", keyphrase.app)
app.add_app("Data Stats", data_stats.app)

st.sidebar.title('Webinars')

# The main app
app.run()