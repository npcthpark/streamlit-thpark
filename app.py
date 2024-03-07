import streamlit as st
view = [100, 150, 30]
st.write('# Streamlit view')
st.title(':flag-kr:')
view
st.write('## bar chart') 
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview = st.write('## Series')
sview