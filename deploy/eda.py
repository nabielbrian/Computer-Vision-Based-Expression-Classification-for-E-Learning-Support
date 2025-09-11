def show():
    import gradio as gr
    from pathlib import Path

    # ---- Paths to your pre-rendered images ----
    IMG1 = "assets/Eda_1.png"  # Expression distribution
    IMG2 = "assets/Eda_2.png"  # Image resolution
    IMG3 = "assets/Eda_3.png"  # Engagement grouping

    # ---- Dataset badge (HF Space) ----
    HF_SPACE_URL = "https://huggingface.co/spaces/ghozyreuski/abulearn-expression-detector"

    # ---- Analysis texts (concise; from your notes) ----
    ANALYSIS_TEXT = {
        "Expression distribution": (
            "**Class Balance (Train)**\n\n"
            "- **Surprise** most samples (~2,819)\n"
            "- **Neutral** fewest (~1,616)\n"
            "- Others ~1,900–2,300\n\n"
        ),
        "Image resolution": (
            "**Image Resolution (Train)**\n\n"
            "- Avg: **96×96 px**; dataset standardized.\n\n"
        ),
        "Engagement levels (8 → 3)": (
            "**Engagement Distribution (Train)**\n\n"
            "- **Nominally Engaged** largest (~36.6%)\n"
            "- **Very Engaged** smallest (~29.1%)\n\n"
        ),
    }

    # Map selectbox option -> image path
    OPTION_TO_IMG = {
        "Expression distribution": IMG1,
        "Image resolution": IMG2,
        "Engagement levels (8 → 3)": IMG3,
    }

    # Small guard so missing files don’t crash the UI
    for p in OPTION_TO_IMG.values():
        if not Path(p).exists():
            # Gradio will show a broken image if missing; this message helps during setup
            gr.Markdown(f"> ⚠️ Expected image not found: `{p}`")

    # ---- UI header with dataset badge ----
    gr.HTML(
        f"""
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:space-between;">
          <h2 style="margin:0;">Exploratory Data Analysis</h2>
          <a href="{HF_SPACE_URL}" target="_blank" rel="noopener">
            <img src="https://img.shields.io/badge/Dataset-HF%20Space-orange?logo=huggingface" 
                 alt="Dataset on Hugging Face">
          </a>
        </div>
        """
    )

    # ---- Preface (placeholder) ----
    gr.Markdown(
        "_Preface :_ This dashboard summarizes analyses for AbuLearn. "
        "It highlights dataset balance, input resolution characteristics, and a derived engagement grouping used for downstream modeling."
    )

    # ---- Selector + outputs ----
    selector = gr.Dropdown(
        choices=list(OPTION_TO_IMG.keys()),
        value="Expression distribution",
        label="Select EDA view",
    )
    img = gr.Image(label=None, show_label=False)
    notes = gr.Markdown()

    def _update(selected: str):
        path = OPTION_TO_IMG.get(selected, IMG1)
        text = ANALYSIS_TEXT.get(selected, "")
        return path, text

    # initialize once
    init_path, init_text = _update(selector.value)
    img.value = init_path
    notes.value = init_text

    # wire interactions
    selector.change(fn=_update, inputs=selector, outputs=[img, notes])