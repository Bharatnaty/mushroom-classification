import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import pickle
import cv2
st.title("Mushroom Classification")

st.sidebar.markdown("CHOOSE WHAT YOU WANT")
menu = ["PREDICTION", "About Us"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "About Us":
    st.subheader("ABOUT US")
    HTML = """
                <div><h2>MUSHROOM CLASSIFICATION</h2>
                <h3>DATA:</h3>KAGGLE<br>
                <h3>DATA CLEANING:</h3>True<br>
                <h3>DATA VISUALIZATION:</h3>True
                <h3>Model Hyperparametr:</h3>True
                <h3>Model:</h3>RandomForestClassifier
                <h3>Designed by:</h3>Bharat Natrayn
                </div>

         """
    st.markdown(HTML, unsafe_allow_html=True)
else:
    st.subheader("PREDICTION")
    # input 1 cap-shape
    cap_shape = ['x', 'b', 's', 'f', 'k', 'c']
    cap_shape_txt = st.selectbox("cap-shape", cap_shape)
    if cap_shape_txt == 'x':
        cap_shape_no = 5
    elif cap_shape_txt == 'b':
        cap_shape_no = 0
    elif cap_shape_txt == 's':
        cap_shape_no = 4
    elif cap_shape_txt == 'f':
        cap_shape_no = 2
    elif cap_shape_txt == 'k':
        cap_shape_no = 3
    elif cap_shape_txt == 'c':
        cap_shape_no = 1

    # input 2 cap-surface
    cap_surface = ['s', 'y', 'f', 'g']
    cap_surface_txt = st.selectbox("cap-surface", cap_surface)
    if cap_surface_txt == 's':
        cap_surface_no = 2
    elif cap_surface_txt == 'y':
        cap_surface_no = 3
    elif cap_surface_txt == 'f':
        cap_surface_no = 0
    elif cap_surface_txt == 'g':
        cap_surface_no = 1

    # input 3 bruises
    bruises = ['t', 'f']
    bruises_txt = st.selectbox("bruises", bruises)
    if bruises_txt == 't':
        bruises_no = 1
    elif bruises_txt == 'f':
        bruises_no = 0

    # input 4 odor
    odor = ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm']
    odor_txt = st.selectbox("odor", odor)
    if odor_txt == 'p':
        odor_no = 6
    elif odor_txt == 'a':
        odor_no = 0
    elif odor_txt == 'l':
        odor_no = 3
    elif odor_txt == 'n':
        odor_no = 5
    elif odor_txt == 'f':
        odor_no = 2
    elif odor_txt == 'c':
        odor_no = 1
    elif odor_txt == 'y':
        odor_no = 8
    elif odor_txt == 's':
        odor_no = 7
    elif odor_txt == 'm':
        odor_no = 4
    # input 5 gill-spacing
    gill_spacing = ['c', 'w']
    gill_spacing_txt = st.selectbox("gill-spacing", gill_spacing)
    if gill_spacing_txt == 'c':
        gill_spacing_no = 0
    elif gill_spacing_txt == 'w':
        gill_spacing_no = 1

    # input 6 gill-size
    gill_size = ['n', 'b']
    gill_size_txt = st.selectbox("gill-size", gill_size)
    if gill_size_txt == 'n':
        gill_size_no = 1
    elif gill_size_txt == 'b':
        gill_size_no = 0

    # input 7 odor gill-color
    gill_color = ['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o']
    gill_color_txt = st.selectbox("gill-color", gill_color)
    if gill_color_txt == 'k':
        gill_color_no = 4
    elif gill_color_txt == 'n':
        gill_color_no = 5
    elif gill_color_txt == 'g':
        gill_color_no = 2
    elif gill_color_txt == 'p':
        gill_color_no = 7
    elif gill_color_txt == 'w':
        gill_color_no = 10
    elif gill_color_txt == 'h':
        gill_color_no = 3
    elif gill_color_txt == 'u':
        gill_color_no = 9
    elif gill_color_txt == 'e':
        gill_color_no = 1
    elif gill_color_txt == 'b':
        gill_color_no = 0
    elif gill_color_txt == 'r':
        gill_color_no = 8
    elif gill_color_txt == 'y':
        gill_color_no = 11
    elif gill_color_txt == 'o':
        gill_color_no = 6
    # input 8 stalk-shape
    stalk_shape = ['e', 't']
    stalk_shape_txt = st.selectbox("stalk-shape", stalk_shape)
    if stalk_shape_txt == 'e':
        stalk_shape_no = 0
    elif stalk_shape_txt == 't':
        stalk_shape_txt = 1

    # input 9 stalk-root
    stalk_root = ['e', 'c', 'b', 'r']
    stalk_root_txt = st.selectbox("stalk-root", stalk_root)
    if stalk_root_txt == 'e':
        stalk_root_no = 2
    elif stalk_root_txt == 'c':
        stalk_root_no = 1
    elif stalk_root_txt == 'b':
        stalk_root_no = 0
    elif stalk_root_txt == 'r':
        stalk_root_no = 3

    # input 10 stalk-surface-above-ring
    stalk_surface_above_ring = ['s', 'f', 'k', 'y']
    stalk_surface_above_ring_txt = st.selectbox("stalk-surface-above-ring", stalk_surface_above_ring)
    if stalk_surface_above_ring_txt == 's':
        stalk_surface_above_ring_no = 2
    elif stalk_surface_above_ring_txt == 'f':
        stalk_surface_above_ring_no = 0
    elif stalk_surface_above_ring_txt == 'k':
        stalk_surface_above_ring_no = 1
    elif stalk_surface_above_ring_txt == 'y':
        stalk_surface_above_ring_no = 3

    # input 11 stalk-surface-below-ring
    stalk_surface_below_ring = ['s', 'f', 'k', 'y']
    stalk_surface_below_ring_txt = st.selectbox("stalk-surface-below-ring", stalk_surface_below_ring)
    if stalk_surface_below_ring_txt == 's':
        stalk_surface_below_ring_no = 2
    elif stalk_surface_below_ring_txt == 'f':
        stalk_surface_below_ring_no = 0
    elif stalk_surface_below_ring_txt == 'k':
        stalk_surface_below_ring_no = 3
    elif stalk_surface_below_ring_txt == 'y':
        stalk_surface_below_ring_no = 1

    # input 12 stalk-color-above-ring
    stalk_color_above_ring = ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y']
    stalk_color_above_ring_txt = st.selectbox("stalk-color-above-ring", stalk_color_above_ring)
    if stalk_color_above_ring_txt == 'w':
        stalk_color_above_ring_no = 7
    elif stalk_color_above_ring_txt == 'g':
        stalk_color_above_ring_no = 3
    elif stalk_color_above_ring_txt == 'p':
        stalk_color_above_ring_no = 6
    elif stalk_color_above_ring_txt == 'n':
        stalk_color_above_ring_no = 4
    elif stalk_color_above_ring_txt == 'b':
        stalk_color_above_ring_no = 0
    elif stalk_color_above_ring_txt == 'e':
        stalk_color_above_ring_no = 2
    elif stalk_color_above_ring_txt == 'o':
        stalk_color_above_ring_no = 5
    elif stalk_color_above_ring_txt == 'c':
        stalk_color_above_ring_no = 1
    elif stalk_color_above_ring_txt == 'y':
        stalk_color_above_ring_no = 8

    # input 13 stalk-color-below-ring
    stalk_color_below_ring = ['w', 'p', 'g', 'b', 'n', 'e', 'y', 'o', 'c']
    stalk_color_below_ring_txt = st.selectbox("stalk-color-below-ring", stalk_color_below_ring)
    if stalk_color_below_ring_txt == 'w':
        stalk_color_below_ring_no = 7
    elif stalk_color_below_ring_txt == 'p':
        stalk_color_below_ring_no = 6
    elif stalk_color_below_ring_txt == 'g':
        stalk_color_below_ring_no = 3
    elif stalk_color_below_ring_txt == 'b':
        stalk_color_below_ring_no = 0
    elif stalk_color_below_ring_txt == 'n':
        stalk_color_below_ring_no = 4
    elif stalk_color_below_ring_txt == 'e':
        stalk_color_below_ring_no = 2
    elif stalk_color_below_ring_txt == 'y':
        stalk_color_below_ring_no = 8
    elif stalk_color_below_ring_txt == 'o':
        stalk_color_below_ring_no = 5
    elif stalk_color_below_ring_txt == 'c':
        stalk_color_below_ring_no = 1

    # input 14 ring-number
    ring_number = ['o', 't', 'n']
    ring_number_txt = st.selectbox("ring-number", ring_number)
    if ring_number_txt == 'o':
        ring_number_no = 1
    elif ring_number_txt == 't':
        ring_number_no = 2
    elif ring_number_txt == 'n':
        ring_number_no = 0

    # input 15 ring-type
    ring_type = ['p', 'e', 'l', 'f', 'n']
    ring_type_txt = st.selectbox("ring-type", ring_type)
    if ring_type_txt == 'p':
        ring_type_no = 4
    elif ring_type_txt == 'e':
        ring_type_no = 0
    elif ring_type_txt == 'l':
        ring_type_no = 2
    elif ring_type_txt == 'f':
        ring_type_no = 1
    elif ring_type_txt == 'n':
        ring_type_no = 3

    # input 16 spore-print-color
    spore_print_color = ['k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b']
    spore_print_color_txt = st.selectbox("spore-print-color", spore_print_color)
    if spore_print_color_txt == 'k':
        spore_print_color_no = 2
    elif spore_print_color_txt == 'n':
        spore_print_color_no = 3
    elif spore_print_color_txt == 'u':
        spore_print_color_no = 6
    elif spore_print_color_txt == 'h':
        spore_print_color_no = 1
    elif spore_print_color_txt == 'w':
        spore_print_color_no = 7
    elif spore_print_color_txt == 'r':
        spore_print_color_no = 5
    elif spore_print_color_txt == 'o':
        spore_print_color_no = 4
    elif spore_print_color_txt == 'y':
        spore_print_color_no = 8
    elif spore_print_color_txt == 'b':
        spore_print_color_no = 0

    # input 17 population
    population = ['s', 'n', 'a', 'v', 'y', 'c']
    population_txt = st.selectbox("population", population)
    if population_txt == 's':
        population_no = 3
    elif population_txt == 'n':
        population_no = 2
    elif population_txt == 'a':
        population_no = 0
    elif population_txt == 'v':
        population_no = 4
    elif population_txt == 'y':
        population_no = 5
    elif population_txt == 'c':
        population_no = 1

    # input 18 habitat
    habitat = ['u', 'g', 'm', 'd', 'p', 'w', 'l']
    habitat_txt = st.selectbox("habitat", habitat)
    if habitat_txt == 'u':
        habitat_no = 5
    elif habitat_txt == 'g':
        habitat_no = 1
    elif habitat_txt == 'm':
        habitat_no = 3
    elif habitat_txt == 'd':
        habitat_no = 0
    elif habitat_txt == 'p':
        habitat_no = 4
    elif habitat_txt == 'w':
        habitat_no = 6
    elif habitat_txt == 'l':
        habitat_no = 2

    input = [cap_shape_no, cap_surface_no, bruises_no, odor_no, gill_spacing_no, gill_size_no, gill_color_no,
             stalk_shape_no, stalk_root_no, stalk_surface_above_ring_no, stalk_surface_below_ring_no
        , stalk_color_above_ring_no, stalk_color_below_ring_no, ring_number_no, ring_type_no, spore_print_color_no,
             population_no, habitat_no]

    with open(r"C:\Users\Admin\PycharmProject\project\mushroom_model.pkl", "rb")as file:
        model = pickle.load(file)
        res = model.predict([input])
    if st.button("Submit"):
        if res[0] == 0:
            result = "Eat"
            image=cv2.resize(cv2.imread(r"C:\Users\Admin\PycharmProject\project\eat.png"),(100,100))
        elif res[0] == 1:
            result = "Poision"
            image=cv2.imread(r"C:\Users\Admin\PycharmProject\project\do-not-eat.jpg")
            image=cv2.resize(image,(100,100))
        st.text(result)
        st.image(image)