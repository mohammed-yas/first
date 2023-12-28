import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')