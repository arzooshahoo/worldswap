import streamlit as st

# Page setup
st.set_page_config(page_title="WorldSwap Hub", page_icon="🌍")
st.title("🌍 WorldSwap Hub")
st.write("Welcome! This platform is designed as a digital culture hub to explore traditions and promote global intercultural connection.")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Cultural Explorer", "Share Your Culture"])

# --- PAGE 1: HOME ---
if page == "Home":
    st.header("About This Project")
    st.write("As a beginner coder, I built this website to showcase my journey learning Python and to create a digital space where people can connect across cultures.")
    st.image("https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=500", caption="Connecting Worlds")

# --- PAGE 2: EXPLORER ---
elif page == "Cultural Explorer":
    st.header("🗺️ Explore Cultural Values")
    st.write("Select a country below to learn about a unique cultural concept or value.")
    
    country = st.selectbox("Choose a culture:", ["Select a country...", "Kenya", "Japan", "Brazil"])
    
    if country == "Kenya":
        st.subheader("🇰🇪 Kenya: Harambee")
        st.write("**Harambee** is a Swahili term that translates to 'let us pull together.' It represents community togetherness, mutual assistance, and joint effort.")
    elif country == "Japan":
        st.subheader("🇯🇵 Japan: Omotenashi")
        st.write("**Omotenashi** goes beyond standard hospitality. It is the art of selflessly looking after guests from the heart, anticipating their needs before they even ask.")
    elif country == "Brazil":
        st.subheader("🇧🇷 Brazil: Simpatia")
        st.write("**Simpatia** describes a warm, welcoming, and approachable disposition. It reflects the deeply social and expressive nature of Brazilian cultural interactions.")

# --- PAGE 3: SHARE ---
elif page == "Share Your Culture":
    st.header("✍️ Share Your Story")
    st.write("What is a value, food, or greeting from your culture?")
    
    user_culture = st.text_input("Your Culture/Country:")
    user_value = st.text_area("Share a cultural value or fact:")
    
    if st.button("Submit to Page"):
        if user_culture and user_value:
            st.success("Thank you for sharing!")
            st.info(f"**{user_culture}**: {user_value}")
        else:
            st.warning("Please fill out both boxes before submitting.")
