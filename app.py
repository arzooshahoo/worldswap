import streamlit as st

st.markdown(
    """
    <style>
    /* Make the app background a premium deep slate/navy instead of plain gray */
    .stApp {
        background-color: #0F172A;
    }
    
    /* Make the main title a beautiful, vibrant gradient */
    h1 {
        font-weight: 800 !important;
        background: linear-gradient(135deg, #38BDF8, #34D399) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-size: 3rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Style subheaders to be clean and crisp */
    h2, h3 {
        color: #E2E8F0 !important;
        font-weight: 600 !important;
    }
    
    /* Style normal paragraph text to be soft and readable */
    p {
        color: #94A3B8 !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    st.subheader("Current Hub Status")

# This creates a beautifully boxed, high-end dashboard element
col1, col2 = st.columns([1, 2])
with col1:
    st.metric(label="Global Regions", value="3 Active", delta="✓ Live")

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
