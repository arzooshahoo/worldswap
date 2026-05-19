import streamlit as st

# 1. Page Configuration (Sets the tab title, icon, and expands the layout to wide mode)
st.set_page_config(
    page_title="WorldSwap Hub", 
    page_icon="🌍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR BETTER VISUALS ---
st.markdown("""
<style>
    /* Styling the main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    /* Subtitle styling */
    .subtitle {
        font-size: 18px;
        color: #4B5563;
        margin-bottom: 30px;
    }
    /* Custom card styles for cultural facts */
    .culture-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 15px;
    }
    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #1F2937;
        margin-bottom: 8px;
    }
</style>
""", unsafe_style_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    page = st.radio("Go to:", ["🏠 Home Dashboard", "🗺️ Cultural Explorer", "✍️ Share Your Story"])
    st.markdown("---")
    st.markdown("### 💡 About WorldSwap")
    st.caption("A digital platform built to bridge perspectives, highlight unique global traditions, and foster intercultural empathy.")

# --- PAGE 1: HOME DASHBOARD ---
if page == "🏠 Home Dashboard":
    st.markdown('<div class="main-title">🌍 WorldSwap Hub</div>', unsafe_style_html=True)
    st.markdown('<div class="subtitle">Exchanging perspectives, traditions, and values across borders.</div>', unsafe_style_html=True)
    
    # Using columns for a dynamic layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Our Mission")
        st.write(
            "In an increasingly interconnected world, understanding *how* different communities navigate "
            "life, relationships, and hospitality is vital. WorldSwap is an open-access digital hub "
            "where users can explore core cultural philosophies that shape societies around the globe."
        )
        st.write(
            "Use the sidebar navigation to dive into our interactive database or contribute a piece "
            "of your own heritage to our community record."
        )
        
        # Adding some quick platform statistics using standard metric widgets
        st.markdown("### 📈 Current Hub Status")
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Explorable Regions", value="3 Global Hubs", delta="More coming")
        m2.metric(label="Core Philosophies", value="3 Documented", delta="Verified")
        m3.metric(label="Platform Cost", value="$0.00", delta="100% Accessible")

    with col2:
        # High-quality visual anchor
        st.image("https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=500", use_container_width=True)

# --- PAGE 2: CULTURAL EXPLORER ---
elif page == "🗺️ Cultural Explorer":
    st.markdown('<div class="main-title">🗺️ Cultural Explorer</div>', unsafe_style_html=True)
    st.markdown('<div class="subtitle">Select a nation below to unlock a core cultural dynamic or guiding philosophy.</div>', unsafe_style_html=True)
    
    # Styled drop-down selection
    country = st.selectbox("Select a country to explore:", ["Choose options...", "Kenya", "Japan", "Brazil"])
    
    st.markdown("---")
    
    if country == "Kenya":
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="culture-card">
                <div class="card-title">🇰🇪 Kenya: The Spirit of 'Harambee'</div>
                <p><strong>Pronunciation:</strong> ha-rahm-BEE</p>
                <p><strong>Core Concept:</strong> Translating literally to 'let us pull together' in Swahili, Harambee is Kenya's official national motto. It embodies community togetherness, mutual assistance, and collective effort.</p>
                <p><strong>Real-World Practice:</strong> It is traditionally used to rally communities for joint projects, from building local schools to supporting families in financial need, proving that individual burdens are lighter when shared by the collective.</p>
            </div>
            """, unsafe_style_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1489749798305-4fea3ae63d43?w=400", caption="Community & Connection", use_container_width=True)
            
    elif country == "Japan":
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="culture-card">
                <div class="card-title">🇯🇵 Japan: The Art of 'Omotenashi'</div>
                <p><strong>Pronunciation:</strong> oh-moh-teh-nah-shee</p>
                <p><strong>Core Concept:</strong> This represents a deep, selfless approach to hospitality. It goes far beyond standard customer service; it is the practice of anticipating a guest's needs completely from the heart without expecting anything in return.</p>
                <p><strong>Real-World Practice:</strong> It requires acute mindfulness and attention to detail—ensuring an environment is perfectly prepared, comfortable, and welcoming before a guest even arrives.</p>
            </div>
            """, unsafe_style_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=400", caption="Mindfulness & Design", use_container_width=True)
            
    elif country == "Brazil":
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="culture-card">
                <div class="card-title">🇧🇷 Brazil: The Warmth of 'Simpatia'</div>
                <p><strong>Pronunciation:</strong> seem-pah-TEE-ah</p>
                <p><strong>Core Concept:</strong> Simpatia describes a naturally warm, approachable, and vibrant disposition. It reflects a deeply social cultural framework that values open expression, friendliness, and treating strangers like immediate community members.</p>
                <p><strong>Real-World Practice:</strong> It shows up in high-energy greetings, genuine curiosity about others, and a collective social environment where community bonding and joy are prioritized.</p>
            </div>
            """, unsafe_style_html=True)
        with col2:
            st.image("https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=400", caption="Vibrant Social Connections", use_container_width=True)

# --- PAGE 3: SHARE YOUR STORY ---
elif page == "✍️ Share Your Story":
    st.markdown('<div class="main-title">✍️ Community Sharing Wall</div>', unsafe_style_html=True)
    st.markdown('<div class="subtitle">Every tradition belongs here. Contribute a core value, greeting, or concept from your background.</div>', unsafe_style_html=True)
    
    # Split input screen layout
    form_col, info_col = st.columns([3, 2])
    
    with form_col:
        st.subheader("Submit Your Heritage Data")
        user_culture = st.text_input("Country / Culture Name:", placeholder="e.g., Italy, New Zealand, etc.")
        user_concept = st.text_input("Core Concept / Word:", placeholder="e.g., Bella Figura, Whānau, etc.")
        user_value = st.text_area("What does it mean and how is it practiced?", placeholder="Describe the tradition or cultural philosophy...")
        
        if st.button("Publish to Live Session"):
            if user_culture and user_concept and user_value:
                st.success("✨ Contribution successfully loaded into the current active user view!")
                
                # Render the user's custom submission in a stylized block instantly
                st.markdown(f"""
                <div class="culture-card" style="border-left-color: #10B981; background-color: #ECFDF5;">
                    <div class="card-title">🌟 Custom Entry: {user_culture} ({user_concept})</div>
                    <p>{user_value}</p>
                </div>
                """, unsafe_style_html=True)
            else:
                st.warning("⚠️ Please fill in all fields before submitting.")
                
    with info_col:
        st.info(
            "💡 **Why participate?**\n\n"
            "By mapping out unique terms and values, we realize that while our customs might differ, "
            "the core human desire for community, hospitality, respect, and love remains identical "
            "across every coordinate on the globe."
        )
