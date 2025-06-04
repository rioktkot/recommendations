import streamlit as st

st.title("🌍 Рекомендация по выбору страны для путешествия")

# Первый вопрос
question1 = st.radio("Вы любите, когда жарко?", ["Да", "Нет"])

if question1 == "Да":
    question2 = st.radio("Вы любите моря?", ["Да", "Нет"])

    if question2 == "Да":
        question3 = st.radio("Вы любите острова?", ["Да", "Нет"])
        if question3 == "Да":
            st.success("Поезжайте в Грецию или на Шри-Ланку 🇬🇷 🇱🇰")
        else:
            st.success("Поезжайте в Турцию 🇹🇷")

    else:  # Не любит моря
        question3 = st.radio("Вы любите музеи?", ["Да", "Нет"])
        if question3 == "Да":
            st.success("Поезжайте в Италию 🇮🇹")
        else:
            st.success("Поезжайте в Канаду 🇨🇦")

else:  # Не любит жару
    question2 = st.radio("Вы любите снег?", ["Да", "Нет"])

    if question2 == "Да":
        question3 = st.radio("Вы любите горные лыжи?", ["Да", "Нет"])
        if question3 == "Да":
            st.success("Поезжайте в Швейцарию 🇨🇭")
        else:
            st.success("Поезжайте в Антарктиду ❄️")

    else:
        question3 = st.radio("Вы любите леса?", ["Да", "Нет"])
        if question3 == "Да":
            st.success("Поезжайте в Финляндию 🇫🇮")
        else:
            st.success("Поезжайте в Исландию 🇮🇸")
