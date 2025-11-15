import streamlit as st

# CSS Styles for the advanced animated application
def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-container {
        position: relative;
        min-height: 100vh;
        overflow: hidden;
    }
    
    /* Animated background particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.3) 0%, transparent 50%);
        animation: particleFloat 20s ease-in-out infinite;
    }
    
    @keyframes particleFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 1; }
        33% { transform: translateY(-20px) rotate(120deg); opacity: 0.8; }
        66% { transform: translateY(-10px) rotate(240deg); opacity: 0.9; }
    }
    
    /* Hide Streamlit branding */
    .stDeployButton, header[data-testid="stHeader"], .stDecoration {
        display: none !important;
    }
    
    /* Main title styling */
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 3s ease-in-out infinite, titleFloat 6s ease-in-out infinite;
        margin: 2rem 0;
        text-shadow: 0 0 30px rgba(78, 205, 196, 0.5);
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes titleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Glassmorphism containers */
    .glass-container {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
        animation: containerFloat 8s ease-in-out infinite;
    }
    
    @keyframes containerFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .glass-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.7s ease;
    }
    
    .glass-container:hover::before {
        left: 100%;
    }
    
    /* Sidebar styling */
    .stSidebar {
        background: rgba(0, 0, 0, 0.8) !important;
        backdrop-filter: blur(20px);
    }
    
    .stSidebar > div {
        background: transparent !important;
    }
    
    .sidebar-header {
        color: #4ecdc4;
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 0 20px rgba(78, 205, 196, 0.5);
    }
    
    /* Animated expandable sections */
    .stExpander {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(78, 205, 196, 0.3) !important;
        margin: 0.5rem 0 !important;
        transition: all 0.3s ease;
    }
    
    .stExpander:hover {
        transform: translateX(10px);
        border-color: rgba(78, 205, 196, 0.6) !important;
        box-shadow: 0 0 20px rgba(78, 205, 196, 0.2);
    }
    
    .stExpander > div:first-child {
        animation: pulse 3s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; transform: scale(1.02); }
    }
    
    /* Input field styling */
    .stSelectbox, .stTextInput {
        margin: 1rem 0;
    }
    
    .stSelectbox > div > div,
    .stTextInput > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(78, 205, 196, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        transition: all 0.3s ease !important;
        position: relative;
        overflow: hidden;
    }
    
    .stSelectbox > div > div:focus-within,
    .stTextInput > div > div:focus-within {
        border-color: rgba(78, 205, 196, 0.8) !important;
        box-shadow: 0 0 20px rgba(78, 205, 196, 0.3) !important;
        transform: scale(1.02);
    }
    
    /* Button animations */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        border-radius: 50px !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stButton > button::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent) !important;
        transition: left 0.5s ease !important;
    }
    
    .stButton > button:hover::before {
        left: 100% !important;
    }
    
    /* Emotion display */
    .emotion-display {
        background: linear-gradient(135deg, rgba(78, 205, 196, 0.1) 0%, rgba(255, 107, 107, 0.1) 100%);
        border: 2px solid rgba(78, 205, 196, 0.5);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        animation: emotionPulse 4s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes emotionPulse {
        0%, 100% { border-color: rgba(78, 205, 196, 0.5); }
        50% { border-color: rgba(255, 107, 107, 0.8); }
    }
    
    .emotion-text {
        font-size: 3rem !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        animation: emotionTextFloat 3s ease-in-out infinite !important;
        text-shadow: 0 0 30px rgba(78, 205, 196, 0.5) !important;
    }
    
    @keyframes emotionTextFloat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Platform buttons */
    .platform-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        border: 2px solid transparent;
    }
    
    .platform-button:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        border-color: rgba(78, 205, 196, 0.6);
    }
    
    .platform-button::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s ease;
        opacity: 0;
    }
    
    .platform-button:hover::before {
        opacity: 1;
        animation: shimmer 1.2s ease-in-out;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    /* YouTube specific styling */
    .youtube-button {
        background: linear-gradient(135deg, #ff0000, #cc0000) !important;
        border-left: 4px solid #ff4444;
    }
    
    /* Spotify specific styling */
    .spotify-button {
        background: linear-gradient(135deg, #1db954, #1aa34a) !important;
        border-left: 4px solid #1ed760;
    }
    
    /* Status messages */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 15px !important;
        border: none !important;
        backdrop-filter: blur(10px) !important;
        animation: statusFloat 4s ease-in-out infinite !important;
    }
    
    @keyframes statusFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-3px); }
    }
    
    /* Floating elements */
    .floating-particles::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(78, 205, 196, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 75% 75%, rgba(255, 107, 107, 0.1) 0%, transparent 50%);
        animation: floatingParticles 15s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes floatingParticles {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-20px) rotate(120deg); }
        66% { transform: translateY(-10px) rotate(240deg); }
    }
    
    /* Link styling */
    .stMarkdown a {
        color: #4ecdc4 !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        position: relative !important;
    }
    
    .stMarkdown a:hover {
        color: #45b7d1 !important;
        transform: translateX(5px) !important;
    }
    
    .stMarkdown a::after {
        content: '' !important;
        position: absolute !important;
        bottom: -2px !important;
        left: 0 !important;
        width: 0 !important;
        height: 2px !important;
        background: linear-gradient(45deg, #4ecdc4, #45b7d1) !important;
        transition: width 0.3s ease !important;
    }
    
    .stMarkdown a:hover::after {
        width: 100% !important;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(78, 205, 196, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
    }
    
    .stTextArea textarea:focus {
        border-color: rgba(78, 205, 196, 0.8) !important;
        box-shadow: 0 0 20px rgba(78, 205, 196, 0.3) !important;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem !important;
        }
        
        .glass-container {
            padding: 1rem !important;
            margin: 1rem 0 !important;
        }
        
        .emotion-text {
            font-size: 2rem !important;
        }
    }
    
    /* Scroll animations */
    @keyframes slideInFromBottom {
        0% {
            transform: translateY(100px);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    .slide-in {
        animation: slideInFromBottom 0.8s ease-out;
    }
    
    /* Loading animation */
    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 4px solid rgba(78, 205, 196, 0.3);
        border-top: 4px solid #4ecdc4;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    
    <script>
    // Add particles effect
    document.addEventListener('DOMContentLoaded', function() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        document.body.appendChild(particlesContainer);
        
        // Add mouse trail effect
        document.addEventListener('mousemove', function(e) {
            const trail = document.createElement('div');
            trail.style.position = 'fixed';
            trail.style.left = e.clientX - 2 + 'px';
            trail.style.top = e.clientY - 2 + 'px';
            trail.style.width = '4px';
            trail.style.height = '4px';
            trail.style.background = 'rgba(78, 205, 196, 0.6)';
            trail.style.borderRadius = '50%';
            trail.style.pointerEvents = 'none';
            trail.style.zIndex = '1000';
            trail.style.transition = 'all 0.5s ease';
            document.body.appendChild(trail);
            
            setTimeout(() => {
                trail.style.opacity = '0';
                trail.style.transform = 'scale(0)';
                setTimeout(() => {
                    if (trail.parentNode) {
                        trail.parentNode.removeChild(trail);
                    }
                }, 500);
            }, 100);
        });
    });
    </script>
    """, unsafe_allow_html=True)
#enhanced sidebar
def create_sidebar():
    # Inject custom glassmorphism CSS + sidebar animation
    st.markdown("""
    <style>
    /* Sidebar glassmorphism base */
    [data-testid="stSidebar"] {
        background: rgba(15, 15, 25, 0.85) !important;
        backdrop-filter: blur(18px) saturate(180%) !important;
        border-right: 2px solid rgba(78, 205, 196, 0.3) !important;
        box-shadow: 2px 0 18px rgba(0, 255, 200, 0.15) !important;
        transition: all 0.3s ease-in-out !important;
        z-index: 999999 !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
    }
    
    @media (max-width: 768px) {
        [data-testid="stSidebar"].st-emotion-cache-1cypcdb {
            transform: none !important;
            transition: width 0.3s !important;
        }
    }

    [data-testid="stSidebarNav"] {
        background: transparent !important;
        z-index: 999999 !important;
        position: relative !important;
    }

    /* Ensure sidebar content stays on top */
    .sidebar-content {
        position: relative !important;
        z-index: 999999 !important;
    }

    /* Sidebar title */
    .sidebar-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #4ECDC4;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 25px;
        text-shadow: 0 0 15px rgba(78, 205, 196, 0.9);
        letter-spacing: 1.2px;
    }

    /* Sidebar buttons */
    .sidebar-button {
        background: linear-gradient(90deg, rgba(78,205,196,0.15), rgba(255,255,255,0.05));
        border: 1px solid rgba(78,205,196,0.25);
        border-radius: 12px;
        padding: 10px 15px;
        color: #E8FDFD;
        font-weight: 500;
        text-decoration: none;
        display: block;
        margin: 8px 0;
        text-align: left;
        transition: all 0.3s ease;
    }
    .sidebar-button:hover {
        background: linear-gradient(90deg, rgba(78,205,196,0.4), rgba(255,255,255,0.1));
        border-color: rgba(78,205,196,0.6);
        transform: translateX(6px);
        box-shadow: 0 0 12px rgba(78,205,196,0.5);
    }

    /* Divider line */
    .sidebar-divider {
        border-top: 1px solid rgba(78,205,196,0.25);
        margin: 20px 0;
    }

    /* Expander text */
    .slide-in {
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar content
    with st.sidebar:
        st.markdown('<div class="sidebar-title">🌐 Futuristic Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        st.markdown('<h2 class="sidebar-header">📖 How It Works</h2>', unsafe_allow_html=True)

        with st.expander("🎬 Step-by-Step Guide", expanded=False):
            st.markdown("""
            <div class="slide-in">
            ### 🚀 Getting Started  
            **Step 1:** Set your preferences  
            **Step 2:** Start the camera  
            **Step 3:** Detect emotions in real time  
            **Step 4:** Get AI-based music recommendations  
            </div>
            """, unsafe_allow_html=True)

        with st.expander("😊 Supported Emotions", expanded=False):
            st.markdown("""
            <div class="slide-in">
            - 😊 Happy → Energetic songs  
            - 😢 Sad → Emotional ballads  
            - 😠 Angry → Rock or metal  
            - 😐 Neutral → Mainstream hits  
            - 😮 Surprise → Experimental  
            - 😨 Fear → Calming music  
            - 🤢 Disgust → Indie tracks  
            </div>
            """, unsafe_allow_html=True)

        with st.expander("💡 Tips for Better Detection", expanded=False):
            st.markdown("""
            <div class="slide-in">
            ✅ Good lighting  
            ✅ Clear face visibility  
            ✅ Hold emotion for 2–3 seconds  
            ✅ Be expressive  
            ✅ Stable camera  
            </div>
            """, unsafe_allow_html=True)

        with st.expander("🎵 Music Genres", expanded=False):
            st.markdown("""
            <div class="slide-in">
            **English:** Pop, Rock, Jazz  
            **Hindi:** Bollywood, Classical  
            **Regional:** Folk, Traditional  
            **International:** K-Pop, EDM, Latin  
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        st.markdown('<a class="sidebar-button" href="#"><span class="icon">💬</span> Chat</a>', unsafe_allow_html=True)
        st.markdown('<a class="sidebar-button" href="#"><span class="icon">🚀</span> About</a>', unsafe_allow_html=True)


# Enhanced YouTube button with advanced animations
def create_youtube_button(youtube_url):
    return f"""
    <a href="{youtube_url}" target="_blank" style="text-decoration: none;">
        <div class="platform-button youtube-button" style="
            background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
            color: white; 
            padding: 20px 30px; 
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(255, 0, 0, 0.3);
        " onmouseover="this.style.transform='translateY(-8px) scale(1.03)'; this.style.boxShadow='0 15px 35px rgba(255, 0, 0, 0.5)'; this.style.borderColor='rgba(255, 68, 68, 0.8)';" 
           onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 8px 25px rgba(255, 0, 0, 0.3)'; this.style.borderColor='transparent';">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
            Open YouTube
        </div>
    </a>
    """

# Enhanced Spotify button with advanced animations
def create_spotify_button(spotify_url):
    return f"""
    <a href="{spotify_url}" target="_blank" style="text-decoration: none;">
        <div class="platform-button spotify-button" style="
            background: linear-gradient(135deg, #1db954 0%, #1aa34a 100%);
            color: white; 
            padding: 20px 30px; 
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(29, 185, 84, 0.3);
        " onmouseover="this.style.transform='translateY(-8px) scale(1.03)'; this.style.boxShadow='0 15px 35px rgba(29, 185, 84, 0.5)'; this.style.borderColor='rgba(29, 231, 96, 0.8)';" 
           onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 8px 25px rgba(29, 185, 84, 0.3)'; this.style.borderColor='transparent';">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
                <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.42 1.56-.299.421-1.02.599-1.559.3z"/>
            </svg>
            Open Spotify
        </div>
    </a>
    """

# Enhanced camera controls with animations
def create_camera_controls():
    col1, col2 = st.columns(2)
    
    with col1:
        start_clicked = st.button("🎥 Start Camera", type="primary", key="start_cam")
    
    with col2:
        stop_clicked = st.button("⏹️ Stop Camera", type="secondary", key="stop_cam")
    
    return start_clicked, stop_clicked

# Enhanced status messages
def show_camera_status(camera_active, has_video_processor, current_emotion):
    if camera_active:
        if has_video_processor:
            st.success(f"🟢 Camera is active - Current emotion: **{current_emotion.upper()}**")
        else:
            st.info("📷 Click 'Allow' when browser asks for camera permission")
    else:
        st.info("▶️ Click 'Start Camera' to begin emotion detection")

# Enhanced platform buttons display
def show_platform_buttons(youtube_url, spotify_url):
    col1, col2 = st.columns(2)
    
    with col1:
        youtube_button = create_youtube_button(youtube_url)
        st.components.v1.html(youtube_button, height=100)
    
    with col2:
        spotify_button = create_spotify_button(spotify_url)
        st.components.v1.html(spotify_button, height=100)

# Enhanced direct links
def show_direct_links(youtube_url, spotify_url):
    st.markdown("### 📱 Direct Links (Click to Open):")
    
    link_col1, link_col2 = st.columns(2)
    
    with link_col1:
        st.markdown(f"[🔴 Open YouTube]({youtube_url})")
        
    with link_col2:
        st.markdown(f"[🟢 Open Spotify]({spotify_url})")
    
    with st.expander("📋 Copy URLs if links don't work"):
        st.text_area("YouTube URL:", youtube_url, height=60)
        st.text_area("Spotify URL:", spotify_url, height=60)

# Enhanced recommendation criteria display
def show_recommendation_criteria(emotion, language="", singer=""):
    criteria = f"🎯 **Based on:** Emotion = {emotion}"
    if language:
        criteria += f", Language = {language}"
    if singer:
        criteria += f", Singer = {singer}"
    
    st.markdown(f'<div class="glass-container">{criteria}</div>', unsafe_allow_html=True)

# Enhanced input fields - removed glass container
def create_input_fields():
    languages = ["", "English", "Hindi", "Spanish", "French", "German", "Italian", "Japanese", "Korean", "Chinese", "Portuguese", "Russian", "Arabic", "Telugu", "Tamil", "Bengali", "Marathi", "Gujarati", "Punjabi", "Kannada", "Malayalam"]
    singers = ["", "Taylor Swift", "Ed Sheeran", "Arijit Singh", "Shreya Ghoshal", "A.R. Rahman", "Lata Mangeshkar", "Kishore Kumar", "Adele", "Bruno Mars", "Beyonce", "The Weekend", "Drake", "Billie Eilish", "Post Malone", "Ariana Grande", "Justin Bieber", "Dua Lipa", "BTS", "Blackpink"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_type = st.radio("🌍 Language Input Method", ["Select from List", "Type Custom"], horizontal=True)
        if input_type == "Select from List":
            lang = st.selectbox("Select Language (Optional)", languages, key="lang_select")
        else:
            lang = st.text_input("Type Language", key="lang_input", placeholder="Enter any language...")
    
    with col2:
        singer_input_type = st.radio("🎤 Singer Input Method", ["Select from List", "Type Custom"], horizontal=True)
        if singer_input_type == "Select from List":
            singer = st.selectbox("Select Singer (Optional)", singers, key="singer_select")
        else:
            singer = st.text_input("Type Singer", key="singer_input", placeholder="Enter any singer name...")
    
    return lang, singer

# Enhanced main title and header - removed glass container
def create_header():
    st.markdown("""
    <h1 class="hero-title">🎵 Music Detection System</h1>
    """, unsafe_allow_html=True)

# Enhanced camera section header - removed glass container
def create_camera_section_header(lang, singer):
    st.markdown("## 📹 Emotion Detection Camera")
    
    if lang or singer:
        preferences = []
        if lang:
            preferences.append(f"🌍 Language: **{lang}**")
        if singer:
            preferences.append(f"🎤 Singer: **{singer}**")
        
        st.markdown(" | ".join(preferences))

# Enhanced emotion display
def create_emotion_display(current_emotion):
    emotion_emojis = {
        'happy': '😊',
        'sad': '😢', 
        'angry': '😠',
        'surprise': '😮',
        'fear': '😨',
        'disgust': '🤢',
        'neutral': '😐'
    }
    
    emoji = emotion_emojis.get(current_emotion.lower(), '😐')
    
    st.markdown(f"""
    <div class="emotion-display">
        <h3>🎭 Current Emotion</h3>
        <div class="emotion-text">{emoji} {current_emotion.upper()}</div>
        <p>Keep your face centered for optimal detection</p>
        <div class="loading-spinner" id="emotion-loader" style="display: none;"></div>
    </div>
    """, unsafe_allow_html=True)

# Enhanced loading animation
def show_loading_animation(message="Processing..."):
    st.markdown(f"""
    <div class="glass-container" style="text-align: center;">
        <div class="loading-spinner"></div>
        <p style="margin-top: 1rem; color: #4ecdc4;">{message}</p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced recommendation section
def create_recommendation_section(youtube_url, spotify_url, search_query, emotion, language="", singer=""):
    
    st.markdown("### 🎶 Your Personalized Music Search")
    st.info(f"🔍 **Search Query:** {search_query}")
    
    
    # Show platform buttons
    show_platform_buttons(youtube_url, spotify_url)
    
    # Show direct links
    show_direct_links(youtube_url, spotify_url)
    
    # Show criteria
    show_recommendation_criteria(emotion, language, singer)
    
    st.markdown("""
    <div class="glass-container">
        <p style="text-align: center; color: #4ecdc4;">
            🎵 Click the buttons above to open your personalized music recommendations!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced success/error messages
def show_success_message(message):
    st.markdown(f"""
    <div class="glass-container" style="
        border: 2px solid #4ecdc4;
        background: linear-gradient(135deg, rgba(78, 205, 196, 0.1), rgba(69, 183, 209, 0.1));
    ">
        <p style="color: #4ecdc4; text-align: center; font-weight: 600;">
            ✨ {message}
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_warning_message(message):
    st.markdown(f"""
    <div class="glass-container" style="
        border: 2px solid #ff6b6b;
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.1), rgba(255, 154, 0, 0.1));
    ">
        <p style="color: #ff6b6b; text-align: center; font-weight: 600;">
            ⚠️ {message}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced page background with particles
def create_animated_background():
    st.markdown("""
    <script>
    // Enhanced particle system
    function createParticleSystem() {
        const canvas = document.createElement('canvas');
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.zIndex = '-2';
        canvas.style.pointerEvents = 'none';
        document.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const particles = [];
        const particleCount = 100;
        
        for (let i = 0; i < particleCount; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                size: Math.random() * 2 + 1,
                opacity: Math.random() * 0.5 + 0.2
            });
        }
        
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            particles.forEach(particle => {
                particle.x += particle.vx;
                particle.y += particle.vy;
                
                if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
                if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;
                
                ctx.beginPath();
                ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(78, 205, 196, ${particle.opacity})`;
                ctx.fill();
            });
            
            requestAnimationFrame(animate);
        }
        
        animate();
        
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    }
    
    // Initialize particle system when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createParticleSystem);
    } else {
        createParticleSystem();
    }
    </script>
    """, unsafe_allow_html=True)