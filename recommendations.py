import streamlit as st

st.set_page_config(page_title="Куда поехать?", page_icon="🌍")

st.title(" Путеводитель по странам")

# Инициализируем состояние
if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

def reset():
    st.session_state.step = 1
    for key in list(st.session_state.keys()):
        if key != "step":
            del st.session_state[key]

# Страница 1
if st.session_state.step == 1:
    st.subheader("Вопрос 1 из 3")
    st.session_state.q1 = st.radio("Вы любите, когда жарко?", ["Да", "Нет"])
    st.button("Далее", on_click=next_step)

# Страница 2
elif st.session_state.step == 2:
    st.subheader("Вопрос 2 из 3")

    if st.session_state.q1 == "Да":
        st.session_state.q2 = st.radio("Вы любите моря?", ["Да", "Нет"])
    else:
        st.session_state.q2 = st.radio("Вы любите снег?", ["Да", "Нет"])

    st.button("Далее", on_click=next_step)

# Страница 3
elif st.session_state.step == 3:
    st.subheader("Вопрос 3 из 3")

    if st.session_state.q1 == "Да":
        if st.session_state.q2 == "Да":
            q3 = st.radio("Вы любите острова?", ["Да", "Нет"])
            if q3 == "Да":
                result = "Поезжайте в Грецию или на Шри-Ланку 🇬🇷 🇱🇰"
            else:
                result = "Поезжайте в Турцию 🇹🇷"
        else:
            q3 = st.radio("Вы любите музеи?", ["Да", "Нет"])
            if q3 == "Да":
                result = "Поезжайте в Италию 🇮🇹"
            else:
                result = "Поезжайте в Канаду 🇨🇦"
    else:
        if st.session_state.q2 == "Да":
            q3 = st.radio("Вы любите горные лыжи?", ["Да", "Нет"])
            if q3 == "Да":
                result = "Поезжайте в Швейцарию 🇨🇭"
            else:
                result = "Поезжайте в Антарктиду ❄️"
        else:
            q3 = st.radio("Вы любите леса?", ["Да", "Нет"])
            if q3 == "Да":
                result = "Поезжайте в Финляндию 🇫🇮"
            else:
                result = "Поезжайте в Исландию 🇮🇸"

    st.session_state.result = result
    st.button("Узнать результат", on_click=next_step)

# Страница результата
elif st.session_state.step == 4:
    st.subheader(" Ваш выбор:")
    st.success(st.session_state.result)
    st.button("Начать заново", on_click=reset)
