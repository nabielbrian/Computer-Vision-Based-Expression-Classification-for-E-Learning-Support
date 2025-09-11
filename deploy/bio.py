import gradio as gr

TEAM = [
    {
        "name": "Muhammad Al Ghifari",
        "title": "Data Scientist",
        "photo": "assets/agi.png",
        "github": "https://github.com/alghfrimh",
        "linkedin": "https://www.linkedin.com/in/alghfrimh/",
    },
    {
        "name": "Ghozy Alfisyahr Reuski",
        "title": "Data Analyst / Data Engineering",
        "photo": "assets/ghozy.png",
        "github": "https://github.com/GhozyAlfisyahrReuski",
        "linkedin": "https://www.linkedin.com/in/ghozy-alfisyahr-reuski-1133481ba/",
    },
    {
        "name": "Brian Nabiel Raharja",
        "title": "Data Analyst",
        "photo": "assets/brian.png",
        "github": "https://github.com/nabielbrian",
        "linkedin": "https://www.linkedin.com/in/briannabiel/",
    },
    {
        "name": "Ali Abdurahman",
        "title": "Data Engineering",
        "photo": "assets/ali.png",
        "github": "https://github.com/aliabdurrahman10",
        "linkedin": "https://www.linkedin.com/in/aliabdurrahman/",
    },
]

DESCRIPTION = (
    "The team worked with real-world datasets to tackle a common issue in e-learning: "
    "online classes often struggle to keep students engaged. Without face-to-face interaction, "
    "instructors find it challenging to assess attentiveness and emotional state. \n\n"
    "To address this, the team explored the field of **machine learning** and its implementation "
    "in **computer vision**, focusing on emotion recognition through facial expressions. "
    "This research led to the creation of **AbuLearn**, an interactive webcam-powered platform "
    "that classifies emotions such as happiness, sadness, neutrality, or surprise then further "
    "classifying into states of focus. By providing these insights, AbuLearn helps educators "
    "better understand student engagement and design more effective and supportive e-learning experiences."
)

def show():
    gr.Markdown("## Team")

    gr.HTML("""
    <style>
      .bio-card { 
        background:#ffffff; border-radius:16px; padding:16px;
        box-shadow:0 8px 20px rgba(0,0,0,.08); text-align:center;
      }
      .bio-img img { border-radius:50%; object-fit:cover; }
      .bio-name { margin:10px 0 0; color:#0b3a6f; font-weight:800; font-size:1.05rem; }
      .bio-role { margin:0; color:#124e78; font-weight:700; }
      .bio-img .edit-buttons, .bio-img [data-testid="image"] ~ div { display:none !important; }
      .badges { margin-top: 10px; display:flex; gap:8px; justify-content:center; flex-wrap:wrap; }
    </style>
    """)

    for i in range(0, len(TEAM), 2):
        with gr.Row():
            for j in range(2):
                if i + j < len(TEAM):
                    m = TEAM[i + j]
                    with gr.Column(scale=1, min_width=280):
                        with gr.Group(elem_classes=["bio-card"]):
                            gr.Image(value=m["photo"], show_label=False, height=170, elem_classes=["bio-img"])
                            gr.HTML(f"<div class='bio-name'>{m['name']}</div><div class='bio-role'>{m['title']}</div>")

                            # Badges row
                            badges_html = "<div class='badges'>"
                            if m["github"]:
                                badges_html += f"""
                                <a href="{m['github']}" target="_blank" rel="noopener noreferrer">
                                    <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=for-the-badge"/>
                                </a>
                                """
                            if m["linkedin"]:
                                badges_html += f"""
                                <a href="{m['linkedin']}" target="_blank" rel="noopener noreferrer">
                                    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge"/>
                                </a>
                                """
                            badges_html += "</div>"
                            gr.HTML(badges_html)
                else:
                    with gr.Column(scale=1, min_width=280):
                        gr.HTML("&nbsp;")

    with gr.Group(elem_classes=["bio-card"]):
        gr.Markdown(DESCRIPTION)