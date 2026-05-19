import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="WorldSwap Hub", page_icon="🌍")

# 2. Main Title and Navigation
st.title("🌍 WorldSwap Hub")
page = st.sidebar.radio("Navigate Pages:", ["Home Dashboard", "Cultural Explorer", "Share Your Story"])

st.markdown("---")

# 3. PAGE 1: HOME DASHBOARD
if page == "Home Dashboard":
    st.header("Welcome to WorldSwap")
    st.write("WorldSwap is an open-access digital culture hub designed to explore distinct traditions, global philosophies, and promote intercultural connection.")
    st.write("Use the sidebar menu to navigate through our global databases or to contribute to the live platform.")
    
    st.subheader("Current Hub Status")
    st.text("📊 Active Databases: 3 Global Regions")
    st.text("🔒 Platform Cost: $0.00 (Fully Accessible)")

# 4. PAGE 2: CULTURAL EXPLORER
if page == "Cultural Explorer":
    st.header("🗺️ Global Philosophy Explorer")
    st.write("Select a nation from the menu below to unlock a core cultural dynamic.")
    
    country = st.selectbox("Choose a culture to study:", ["Select a country...", "Kenya", "Japan", "Brazil"])
    
    if country == "Kenya":
        st.subheader("🇰🇪 Kenya: The Spirit of 'Harambee'")
        st.write("**Concept:** Translating to 'let us pull together' in Swahili, Harambee is a core national motto representing community togetherness, mutual assistance, and joint effort.")
        st.write("**Practice:** Traditionally used to rally neighborhoods together for collective projects, proving that individual burdens are lighter when shared.")
        
    if country == "Japan":
        st.subheader("🇯🇵 Japan: The Art of 'Omotenashi'")
        st.write("**Concept:** This represents a deep, selfless approach to hospitality. It is the practice of anticipating a guest's needs completely from the heart without expecting anything in return.")
        st.write("**Practice:** Requires acute mindfulness and attention to detail—ensuring an environment is perfectly prepared and welcoming before a visitor arrives.")
        
    if country == "Brazil":
        st.subheader("🇧🇷 Brazil: The Warmth of 'Simpatia'")
        st.write("**Concept:** Simpatia describes a naturally warm, approachable, and vibrant disposition. It reflects a social framework that values open expression and friendliness.")
        st.write("**Practice:** Evident in welcoming gestures, genuine curiosity about others, and an environment where social bonding is heavily prioritized.")

# 5. PAGE 3: SHARE YOUR STORY
if page == "Share Your Story":
    st.header("✍️ Community Sharing Wall")
    st.write("Every tradition belongs here. Contribute a core value or greeting from your own background below.")
    
    user_culture = st.text_input("Country / Culture Name:")
    user_concept = st.text_input("Core Concept / Word:")
    user_value = st.text_area("What does it mean and how is it practiced?")
    
    if st.button("Publish Entry"):
        if user_culture and user_concept and user_value:
            st.success("✨ Contribution successfully loaded into your active session view!")
            st.write(f"### 🌟 Custom Entry: {user_culture}")
            st.write(f"**Concept:** {user_concept}")
            st.write(user_value)
        else:
            st.warning("⚠️ Please fill out all fields before submitting.")
