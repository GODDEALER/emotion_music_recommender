import streamlit as st
from music_functionality import *
from music_ui_styles import *
from splash_animation import create_splash_loader

# Configure page - removed wide layout
st.set_page_config(
    page_title="viberecommender",
    page_icon="🎵",
    initial_sidebar_state="expanded"
)

# Show splash screen first
create_splash_loader()

# Initialize and run the app
load_custom_css()
create_animated_background()
init_session_states()

# Create sidebar - This was missing!
create_sidebar()

# Create main content
create_header()

# Get user preferences
lang, singer = create_input_fields()

# Camera section
create_camera_section_header(lang, singer)
start_clicked, stop_clicked = create_camera_controls()
    
if start_clicked:
    start_camera()
if stop_clicked:
    stop_camera()

# Handle camera stream
has_processor, current_emotion = handle_camera_stream()

# Show current emotion display
if st.session_state.camera_active:
    create_emotion_display(st.session_state.detected_emotion)

show_camera_status(st.session_state.camera_active, has_processor, current_emotion)

# Recommendation button
if st.button("🎵 Recommend me songs", type="primary"):
    if can_recommend_songs():
        youtube_url, spotify_url, search_query = generate_music_urls(
            st.session_state.detected_emotion, lang, singer
        )
        
        show_success_message(f"Opening music platforms based on your **{st.session_state.detected_emotion.upper()}** emotion!")
        
        # Use the enhanced recommendation section
        create_recommendation_section(youtube_url, spotify_url, search_query, st.session_state.detected_emotion, lang, singer)
        
    else:
        show_warning_message("Please start the camera and let me detect your emotion first! Currently detected: neutral")