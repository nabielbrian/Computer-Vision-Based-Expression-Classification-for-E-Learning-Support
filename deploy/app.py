import gradio as gr
import bio, eda, inference

APP_NAME = "AbuLearn"
LOGO_PATH = "assets/Logo_Finpro_AbuLearn.png"
REPO_URL = "https://github.com/FTDS-assignment-bay/p2-final-project-ftds-030-hck-group01-abulearn-project"

with gr.Blocks(theme=gr.themes.Glass()) as demo:
    gr.HTML("""
    <style>
      /* --- Floating logo on the splash --- */
      #welcome-logo img{
        width:320px !important; max-width:80%;
        margin:0 auto; display:block;
        animation: floatY 5s ease-in-out infinite, glowPulse 3s ease-in-out infinite;
        filter: drop-shadow(0 12px 25px rgba(0,0,0,0.25));
        transition: transform .4s ease;
      }
      #welcome-logo img:hover{ transform: scale(1.12); }
      @keyframes floatY{ 0%,100%{transform:translateY(0)} 50%{transform:translateY(-20px)} }
      @keyframes glowPulse{ 0%,100%{filter:drop-shadow(0 0 18px rgba(255,107,107,.6))}
                            50%{filter:drop-shadow(0 0 36px rgba(255,107,107,.9))} }
      /* --- TANGIBLE Start button (strong selectors so it wins) --- */
      .start-btn button, .start-btn .gr-button{
        background: linear-gradient(145deg, #ff6b6b, #ff4d4d) !important;
        color:#fff !important;
        font-size:1.2rem !important; font-weight:800 !important;
        border:none !important; border-radius:12px !important;
        padding:14px 28px !important;
        box-shadow: 0 6px 12px rgba(0,0,0,.25), inset 0 2px 4px rgba(255,255,255,.3) !important;
        transition: all .2s ease !important;
      }
      .start-btn button:hover, .start-btn .gr-button:hover{
        background: linear-gradient(145deg, #ff4d4d, #ff1a1a) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(0,0,0,.30), inset 0 2px 4px rgba(255,255,255,.3) !important;
      }
      .start-btn button:active, .start-btn .gr-button:active{
        transform: translateY(2px) !important;
        box-shadow: 0 3px 6px rgba(0,0,0,.2) inset !important;
      }
      /* --- Center the Tabs and style like pills (target via elem_id) --- */
      #main-tabs [role="tablist"]{
        display:flex !important;
        justify-content:center !important;
        gap:16px !important;
        padding:16px 0 !important;
        border-bottom: none !important;   /* hide underline bar */
      }
      #main-tabs [role="tab"]{
        border-radius:999px !important;
        padding:12px 20px !important;
        font-weight:700 !important;
        background: rgba(255,255,255,.10) !important;
        border:1px solid rgba(255,255,255,.15) !important;
        transition: all .2s ease !important;
      }
      #main-tabs [role="tab"][aria-selected="true"]{
        background:#ff6b6b !important; color:#fff !important;
        border-color: transparent !important;
        box-shadow:0 6px 16px rgba(255,107,107,.35) !important;
      }
      #main-tabs [role="tab"]:hover{ filter:brightness(1.05); transform:translateY(-1px); }
    </style>
    """)

    # ------------------ WELCOME / SPLASH ------------------
    with gr.Group(visible=True) as welcome_page:
        with gr.Column():
            gr.Image(value=LOGO_PATH, show_label=False, elem_id="welcome-logo")
            gr.Markdown("""
                <div style="text-align:center; margin-top:32px;">
                  <h1 style="margin:0; font-size:2.5rem;">Welcome to AbuLearn</h1>
                  <p style="margin-top:10px; font-size:1.2rem;">
                    Your personalized learning experience starts here.
                  </p>
                </div>
            """)
            # ▶︎ play emoji + tangible styles
            start_btn = gr.Button("▶︎ Start now", size="lg", elem_classes=["start-btn"])

    # ------------------ MAIN APP ------------------
    with gr.Group(visible=False) as main_container:
        # Title + GitHub badge
        gr.HTML(f"""
        <div id="app-header" style="display:flex;justify-content:center;align-items:center;gap:12px;">
          <h1 style="margin:0;">{APP_NAME}</h1>
          <a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">
            <img src="https://img.shields.io/badge/GitHub-Repo-blue?logo=github&style=flat-square" alt="GitHub Repo">
          </a>
        </div>
        """)

        with gr.Accordion("ℹ️ About us", open=False):
            gr.Markdown(
                "AbuLearn is an interactive webcam-powered platform for recognizing emotions during online learning. "
                "By inferring expressions such as happiness, sadness, neutrality, or surprise, it helps instructors "
                "understand engagement and tailor more effective, supportive e-learning experiences."
            )

        # Give Tabs an elem_id so CSS can center them reliably
        with gr.Tabs(elem_id="main-tabs"):
            with gr.Tab("👤 Profile"):
                bio.show()
            with gr.Tab("📊 EDA"):
                eda.show()
            with gr.Tab("🎥 Inference (Webcam)"):
                inference.show()

    # ------------------ Wiring ------------------
    def start_app():
        return gr.update(visible=False), gr.update(visible=True)

    start_btn.click(start_app, inputs=None, outputs=[welcome_page, main_container])

if __name__ == "__main__":
    demo.launch()