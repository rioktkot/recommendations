import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #ece9f7;
        }
        .stApp {
           background-color: #fff7e6;
            border-radius: 12px;
            padding: 2em;
        }
        h1, h2, h3 {
            color: #7d3c98;
        }
    </style>
""", unsafe_allow_html=True)


st.title("Corse recommendator")
st.write("""Recommends a Khan Academy course based on grade and subject preferences.""")


# Course options to choose from for our recommendation.
fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"
chess = "Chess school"
art = "artists courses"
football = "football academy"
programming = "programming"


# Collect user attributes to inform our recommendation.
grade = int(st.selectbox("What grade are you in? ",[1,2,3,4,5,6,7,8,9,10,11]))
favorite_subject = (st.selectbox("What is your favorite subject? ",["art","computer science","math","chess"]))
hobby = (st.selectbox("what is your favourite hobby? ",["sport","games","art"]))

# Make a course recommendation based on the user's attributes.
rec = ""
if hobby == "sport":
    rec = football
if grade < 4:
    rec = rec + ", " + grammar
else:
    if favorite_subject == "art":
        rec = rec + ", " + art + ", " + pixar
    else:
        if favorite_subject == "computer science" or favorite_subject == "math":
            rec = rec + ", " + pixar + ", " + programming
        else:
            if favorite_subject == "chess":
                rec = rec + ", " + chess
            else:
               rec = rec + ", " + fin_lit
                    
if st.button("Get My Recommendation!"):
    st.markdown(f"### We recommend the Khan Academy course:\n**{rec}**")
