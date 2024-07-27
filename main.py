import streamlit as st

st.title("AI tutor Title")
st.subheader("sub header")
st.write("hello word")

"""
# This is markdown
## This is sub title
### This is su sub title
"""

text = st.text_input("text input")
st.write(text)

gender = st.selectbox("gender input", ("male", "female"))

selected = st.checkbox("are you agree ?")

if selected:
    st.success("동의했습니다.")
else:
    st.error("동의하지 않았습니다.")

options = st.multiselect("취미",['음악 감상', '독서', '게임'])
st.write(', '.join(options))

with st.sidebar:
    add_radio = st.radio("언어 선택", ("한국어","영어"))

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("A owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)

with tab3:
    st.header("A owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=300)