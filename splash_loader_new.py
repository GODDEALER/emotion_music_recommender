import streamlit as st
import time

def create_splash_loader():
    # Initialize session state
    if 'splash_complete' not in st.session_state:
        st.session_state.splash_complete = False
        st.session_state.progress = 0
    
    # Return early if splash is already complete
    if st.session_state.splash_complete:
        return

    # Hide streamlit components during splash
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # Create containers for splash components
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Title with gradient animation
        st.markdown("""
        <style>
        .splash-title {
            font-size: 2.5em;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 3s ease-in-out infinite;
            margin-bottom: 2rem;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .status-text {
            color: #4ecdc4;
            font-size: 1.2rem;
            text-align: center;
            margin: 1rem 0;
        }
        
        .progress-text {
            color: #ffffff80;
            text-align: center;
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        </style>
        
        <div class="splash-title">Music Emotion Detection</div>
        """, unsafe_allow_html=True)
        
        # Progress bar and status
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Loading messages
        loading_messages = [
            "Initializing AI models...",
            "Setting up emotion detection...",
            "Configuring music recommendations...",
            "Loading user interface...",
            "Preparing for launch...",
            "Almost ready...",
            "Final preparations..."
        ]
        
        # Simulate loading progress
        duration = 100  # 100 seconds
        steps = 100
        
        for i in range(steps + 1):
            current_progress = i
            message_idx = min(int(len(loading_messages) * (current_progress / 100)), len(loading_messages) - 1)
            
            # Update progress and status
            progress_bar.progress(current_progress)
            status_text.markdown(f"""
                <div class="status-text">{loading_messages[message_idx]}</div>
                <div class="progress-text">Progress: {current_progress}%</div>
            """, unsafe_allow_html=True)
            
            if i < steps:  # Don't sleep on the last iteration
                time.sleep(duration / steps)
        
        # Clean up
        progress_bar.empty()
        status_text.empty()
        
        # Mark splash as complete
        st.session_state.splash_complete = True
        
        # Force a rerun to show the main app
        st.rerun()