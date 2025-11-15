import streamlit as st
import time
import json
import os
import math
import base64
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components


def _load_lottie(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def create_splash_loader(duration_seconds: float = 10.0, steps: int = 40):
    """Show a splash with background Lottie (`assets/back.json`) and centered logo Lottie
    (`assets/logo1.json`) above the title. Completes in 10 seconds with smooth animations.

    The function is idempotent per session via `st.session_state['splash_complete']`.
    """
    if 'splash_complete' not in st.session_state:
        st.session_state.splash_complete = False

    if st.session_state.splash_complete:
        return

    # Resolve asset paths
    base_dir = os.path.join(os.path.dirname(__file__), 'assets')
    bg_path = os.path.join(base_dir, 'back.json')
    logo_path = os.path.join(base_dir, 'logo1.json')

    lottie_bg = _load_lottie(bg_path)
    lottie_logo = _load_lottie(logo_path)

    # Basic CSS
    st.markdown("""
    <style>
    .splash-container { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:80vh; padding:1rem; }
    .splash-title { 
        font-size:3.0rem; 
        font-weight:700; 
        margin-top:0px;
        margin-bottom:2px;
        background:linear-gradient(45deg,#ff6b6b,#4ecdc4,#45b7d1,#96ceb4);
        background-size:300% 300%;
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        display:inline-block;
        white-space:nowrap;
        text-align:center;
        perspective: 1000px;
    }

    /* 3D flip animation for each letter */
    .flip-letter {
        display: inline-block;
        opacity: 0;
        transform-style: preserve-3d;
        transform: rotateX(-90deg);
        animation: flipIn 0.6s forwards, gradientShift 3s ease-in-out infinite;
        background: linear-gradient(45deg,#ff6b6b,#4ecdc4,#45b7d1,#96ceb4);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* caret implemented as a pseudo-element on the span */
    .typewriter-text::after {
        content: " ";
        display: inline-block;
        width: 10px;
        height: 1.1em;
        margin-left: 6px;
        background: rgba(255,255,255,0.85);
        vertical-align: middle;
        opacity: 0.9;
    }

    @keyframes flipIn {
        0% {
            opacity: 0;
            transform: rotateX(-90deg);
        }
        100% {
            opacity: 1;
            transform: rotateX(0);
        }
    }

    /* Music beat bars visualization */
    .beat-progress {
        width: 280px;
        height: 48px;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        gap: 6px;
        margin: 10px auto;
        padding: 8px 12px;
        background: rgba(0,0,0,0.18);
        border-radius: 24px;
        position: relative; /* allow overlay of percentage label */
    }

    .beat-bar {
        width: 8px;
        height: 5px;
        background: #4ecdc4;
        border-radius: 3px;
        transition: height 0.2s ease;
    }

    .progress-label {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        font-size: 0.95rem;
        color: rgba(255,255,255,0.95);
        font-weight: 600;
        text-shadow: 0 2px 8px rgba(0,0,0,0.6);
        pointer-events: none;
        z-index: 3;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes beatPulse {
        0%, 100% { height: 5px; opacity: 0.6; }
        50% { height: 28px; opacity: 1; }
    }

    @keyframes colorCycle {
        0% { background: #4ecdc4; }
        33% { background: #ff6b6b; }
        66% { background: #45b7d1; }
        100% { background: #4ecdc4; }
    }

    .loading-text { 
        font-size: 1.05rem;
        background: linear-gradient(45deg,#ff6b6b,#4ecdc4,#45b7d1);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 3s ease-in-out infinite;
        text-align: center;
        margin-top: 2px;
        font-weight: 500;
    }

    .loading-description { 
        color: rgba(255,255,255,0.75);
        max-width: 480px;
        text-align: center;
        margin-top: 2px;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

    # Placeholders so we can clear after completion
    bg_ph = st.empty()
    center_ph = st.empty()
    progress_ph = st.empty()
    status_ph = st.empty()

    # Show background Lottie (full-screen underlay) if available
    if lottie_bg is not None:
        try:
            bg_json = json.dumps(lottie_bg)
            bg_b64 = base64.b64encode(bg_json.encode('utf-8')).decode('utf-8')
            data_url = f"data:application/json;base64,{bg_b64}"

            bg_html = f"""
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player
                src="{data_url}"
                background="transparent"
                speed="1"
                loop
                autoplay
                style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:-9999;opacity:0.6;pointer-events:none;">
            </lottie-player>
            """

            # Inject using a tiny placeholder so Streamlit doesn't reserve large vertical space
            bg_ph.markdown(bg_html, unsafe_allow_html=True)
        except Exception:
            # fallback: show small bg via st_lottie (non-fixed)
            bg_ph.container().write("")
            with st.container():
                st_lottie(lottie_bg, height=300, loop=True, key='splash_bg')

    # Center column: logo, title, progress, status (no extra gaps)
    cols = center_ph.columns([1, 2, 1])
    with cols[1]:
        if lottie_logo is not None:
            # larger centered logo directly above title
            st_lottie(lottie_logo, height=260, loop=True, key='splash_logo')
        # Title (minimal margins) - 3D flip animation with gradient
        title_text = "viberecommender"
        letters_html = ''.join([f'<span class="flip-letter" style="animation-delay:{i*0.1}s;">{letter}</span>' for i, letter in enumerate(title_text)])
        st.markdown(f'<div style="margin-top:6px;margin-bottom:6px;text-align:center;"><h1 class="splash-title" style="margin:0;padding:0;">{letters_html}</h1></div>', unsafe_allow_html=True)

        # Music beat progress visualization (initial, 0%)
        progress_html = f"""
        <div class="beat-progress">
            {''.join([f'<div class="beat-bar" style="animation: beatPulse 0.8s ease-in-out {i*0.1}s infinite, colorCycle 3s ease-in-out infinite; height: 6px;"></div>' for i in range(15)])}
            <div class="progress-label">0%</div>
        </div>
        """
        progress_ph.markdown(progress_html, unsafe_allow_html=True)
        status_text = status_ph.empty()

    # Loading messages (optimized for 10-second duration)
    loading_messages = [
        "Initializing AI models...",
        "Setting up emotion detection...",
        "Loading recommendations...",
        "Almost ready...",
        "Launching..."
    ]

    # Timing
    duration = float(duration_seconds)
    steps = int(steps)
    sleep_per_step = duration / steps if steps > 0 else 0
    start_time = time.time()

    for i in range(steps + 1):
        # Compute elapsed and target progress
        elapsed = time.time() - start_time
        # Avoid overshooting
        t = min(1.0, elapsed / duration) if duration > 0 else 1.0
        progress = int(t * 100)

        # Update beat animation and status
        progress_html = f"""
        <div class="beat-progress">
            {''.join([f'<div class="beat-bar" style="animation: beatPulse {0.8 + (i%3)*0.1}s ease-in-out {i*0.1}s infinite, colorCycle 3s ease-in-out infinite; height: {5 + min(28, int((progress/100.0) * 28))}px;"></div>' for i in range(15)])}
            <div class="progress-label">{progress}%</div>
        </div>
        """
        progress_ph.markdown(progress_html, unsafe_allow_html=True)
        msg_idx = min(int((progress / 100) * len(loading_messages)), len(loading_messages) - 1)
        # Only show the loading message; numeric percentage is rendered inside the visualizer label.
        status_text.markdown(f"<div class='loading-text'>{loading_messages[msg_idx]}</div>", unsafe_allow_html=True)

        # Sleep only if we still have time remaining
        if elapsed < duration:
            time.sleep(sleep_per_step)

        # When we hit 100%, play a short fade-out and then finish the splash
        if progress >= 100:
            # small fade overlay that transitions to opaque, giving a smooth handoff
            fade_duration = 0.7
            # Enhanced fade: animate logo/title/beat bars out, fade background lottie and apply overlay
            overlay_html = ("""
            <div id="splash-fade-overlay" style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:#0b0d0f;opacity:0;transition:opacity __FADE__s ease;z-index:99998;"></div>
            <script>
            (function(){
                const fade = __FADE__;
                // helper to animate and hide elements gracefully
                function fadeOutSelector(sel, opts){
                    const el = document.querySelector(sel);
                    if (!el) return;
                    el.style.transition = 'opacity ' + fade + 's ease, transform ' + fade + 's ease';
                    el.style.transform = opts && opts.transform ? opts.transform : 'translateY(-6px) scale(0.98)';
                    el.style.opacity = '0';
                }

                // fade title and beat bars
                setTimeout(function(){
                    fadeOutSelector('.splash-title');
                    fadeOutSelector('.beat-progress');
                    // try to fade any lottie-player elements (background and possibly others)
                    const lotties = document.querySelectorAll('lottie-player');
                    lotties.forEach(function(lp){
                        lp.style.transition = 'opacity ' + fade + 's ease, transform ' + fade + 's ease';
                        lp.style.opacity = '0';
                        lp.style.transform = 'scale(0.98)';
                    });
                    // try to fade the logo produced by streamlit-lottie (it may render in a div)
                    const logo = document.querySelector('[data-testid="stImage"]');
                    if (logo) { logo.style.transition = 'opacity ' + fade + 's ease, transform ' + fade + 's ease'; logo.style.opacity = '0'; logo.style.transform='scale(0.9)'; }
                }, 10);

                // then bring up the overlay on the next tick so the effect blends
                setTimeout(function(){
                    const ov = document.getElementById('splash-fade-overlay');
                    if (ov) ov.style.opacity = '0.95';
                }, 20 + (fade*200));
            })();
            </script>
            """).replace('__FADE__', str(fade_duration))
            try:
                # Some browsers/Streamlit can render stray JS tokens if the IIFE closing appears outside script
                # Remove any accidental standalone IIFE close tokens before injecting.
                overlay_html = overlay_html.replace('})();', '')
                # Render overlay using the bg placeholder so it sits above the page
                bg_ph.markdown(overlay_html, unsafe_allow_html=True)
            except Exception:
                pass

            # wait for the fade to complete, then clear splash and allow main UI to render
            time.sleep(fade_duration + 0.05)
            try:
                bg_ph.empty()
                center_ph.empty()
                progress_ph.empty()
                status_ph.empty()
            except Exception:
                pass

            st.session_state.splash_complete = True
            return

    # Cleanup placeholders so main UI can show
    try:
        bg_ph.empty()
        center_ph.empty()
        progress_ph.empty()
        status_ph.empty()
    except Exception:
        pass

    st.session_state.splash_complete = True
