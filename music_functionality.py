import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import urllib.parse

# Load model and labels
@st.cache_resource
def load_emotion_model():
    model = load_model("model.h5")
    label = np.load("labels.npy")
    return model, label

# Initialize MediaPipe
@st.cache_resource
def init_mediapipe():
    holistic = mp.solutions.holistic
    hands = mp.solutions.hands
    holis = holistic.Holistic()
    drawing = mp.solutions.drawing_utils
    return holistic, hands, holis, drawing

# Emotion detection processor class
class Emotion_Processor:
    def __init__(self):
        self.frame_count = 0
        self.current_emotion = "neutral"
        self.process_every_n_frames = 3
        self.last_detected_emotion = None
        
        # Load model and mediapipe
        self.model, self.label = load_emotion_model()
        self.holistic, self.hands, self.holis, self.drawing = init_mediapipe()
    
    def get_current_emotion(self):
        return self.current_emotion
    
    def recv(self, frm):
        # Convert frame to numpy array
        frame = frm.to_ndarray(format="bgr24")
        frame = cv2.flip(frame, 1)
        
        self.frame_count += 1
        
        # Only process emotion detection every N frames
        if self.frame_count % self.process_every_n_frames == 0:
            try:
                res = self.holis.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                lst = []
                
                if res.face_landmarks:
                    # Extract face landmarks
                    for i in res.face_landmarks.landmark:
                        lst.append(i.x - res.face_landmarks.landmark[1].x)
                        lst.append(i.y - res.face_landmarks.landmark[1].y)
                    
                    # Extract left hand landmarks
                    if res.left_hand_landmarks:
                        for i in res.left_hand_landmarks.landmark:
                            lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                            lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
                    else:
                        for i in range(42):
                            lst.append(0.0)
                    
                    # Extract right hand landmarks
                    if res.right_hand_landmarks:
                        for i in res.right_hand_landmarks.landmark:
                            lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                            lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
                    else:
                        for i in range(42):
                            lst.append(0.0)
                    
                    # Make prediction if we have enough features
                    if len(lst) == 1020:
                        lst = np.array(lst).reshape(1, -1)
                        prediction = self.model.predict(lst, verbose=0)
                        pred = self.label[np.argmax(prediction)]
                        self.current_emotion = pred
                        print(f"Detected emotion: {pred}")
                
            except Exception as e:
                print(f"Error in emotion processing: {e}")
        
        # Always process landmarks for drawing
        try:
            res = self.holis.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Draw landmarks
            if res.face_landmarks:
                self.drawing.draw_landmarks(frame, res.face_landmarks, self.holistic.FACEMESH_CONTOURS)
            if res.left_hand_landmarks:
                self.drawing.draw_landmarks(frame, res.left_hand_landmarks, self.hands.HAND_CONNECTIONS)
            if res.right_hand_landmarks:
                self.drawing.draw_landmarks(frame, res.right_hand_landmarks, self.hands.HAND_CONNECTIONS)
        except Exception as e:
            print(f"Error in landmark drawing: {e}")
        
        # Display current emotion and frame counter
        cv2.putText(frame, self.current_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Frame: {self.frame_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        return av.VideoFrame.from_ndarray(frame, format="bgr24")

# Function to generate music search URLs
def generate_music_urls(emotion, language="", singer=""):
    search_terms = []
    
    # Add language if selected
    if language:
        search_terms.append(language)
    
    # Add singer if selected
    if singer:
        search_terms.append(singer)
    
    # Add detected emotion
    search_terms.append(emotion)
    
    # Add "songs" to make it more specific
    search_terms.append("songs")
    
    # Create search query and URLs
    search_query = " ".join(search_terms)
    encoded_query = urllib.parse.quote(search_query)
    
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    spotify_url = f"https://open.spotify.com/search/{encoded_query}"
    
    return youtube_url, spotify_url, search_query

# Function to initialize session states
def init_session_states():
    if "detected_emotion" not in st.session_state:
        st.session_state.detected_emotion = "neutral"
    if "camera_active" not in st.session_state:
        st.session_state.camera_active = False
    if "emotion_processor" not in st.session_state:
        st.session_state.emotion_processor = None

# Function to create dropdown options
def get_dropdown_options():
    languages = ["", "English", "Hindi", "Spanish", "French", "German", "Italian", "Japanese", "Korean", "Chinese", "Portuguese", "Russian", "Arabic", "Telugu", "Tamil", "Bengali", "Marathi", "Gujarati", "Punjabi", "Kannada", "Malayalam", "Other"]
    
    singers = ["", "Taylor Swift", "Ed Sheeran", "Arijit Singh", "Shreya Ghoshal", "A.R. Rahman", "Lata Mangeshkar", "Kishore Kumar", "Adele", "Bruno Mars", "Beyonce", "The Weekend", "Drake", "Billie Eilish", "Post Malone", "Ariana Grande", "Justin Bieber", "Dua Lipa", "BTS", "Blackpink", "Other"]
    
    return languages, singers

# Camera control functions
def start_camera():
    st.session_state.camera_active = True
    st.rerun()

def stop_camera():
    st.session_state.camera_active = False
    st.rerun()

# Function to handle camera streaming with network security improvements
def handle_camera_stream():
    if st.session_state.camera_active:
        webrtc_ctx = webrtc_streamer(
            key="emotion-detection",
            desired_playing_state=st.session_state.camera_active,
            video_processor_factory=Emotion_Processor,
            media_stream_constraints={
                "video": {
                    "width": {"ideal": 640},
                    "height": {"ideal": 480},
                    "frameRate": {"ideal": 20}
                },
                "audio": True
            },
            rtc_configuration={
                "iceServers": [
                    {"urls": ["stun:stun.l.google.com:19302"]},
                    {"urls": ["stun:stun1.l.google.com:19302"]},
                ]
            },
            async_processing=True
        )
        
        # Update emotion in session state
        if webrtc_ctx.video_processor:
            st.session_state.detected_emotion = webrtc_ctx.video_processor.current_emotion
            return True, webrtc_ctx.video_processor.current_emotion
        else:
            return False, "neutral"
    return None, "neutral"

# Function to validate recommendation request
def can_recommend_songs():
    return st.session_state.detected_emotion and st.session_state.detected_emotion != "neutral"