# inference.py — Single webcam (no blue) + Image select/upload inference
import os
import cv2
import gradio as gr
from ultralytics import YOLO

# Silence Ultralytics config dir warning (optional)
os.environ.setdefault("YOLO_CONFIG_DIR", "./.ultralytics")

# ---- constants (tune here) ----
MODEL_PATH = "deploy_model/best.pt"
CONF = 0.40
IMGSZ = 160
IOU  = 0.60

# Predefined repo assets (adjust extensions if needed)
ASSET_OPTIONS = [
    "assets/inf_1.jpg",
    "assets/inf_2.jpg",
    "assets/inf_3.jpg",
    "assets/inf_4.jpg",
]

# ---- load once ----
model = YOLO(MODEL_PATH)

# ---------- helpers ----------
def _yolo_on_bgr_return_rgb(bgr_image):
    """
    Run YOLO on a BGR image, draw predictions, return RGB image for Gradio.
    """
    # YOLO inference (on BGR)
    r = model.predict(bgr_image, imgsz=IMGSZ, conf=CONF, iou=IOU, verbose=False)[0]
    annotated_bgr = r.plot()              # plot() returns BGR
    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
    return annotated_rgb

# ---------- webcam pipeline ----------
def predict_webcam(rgb_frame):
    """
    Gradio webcam gives RGB. Convert to BGR before YOLO,
    then convert back to RGB for display (fixes blue tint).
    """
    if rgb_frame is None:
        return None
    bgr = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
    return _yolo_on_bgr_return_rgb(bgr)

# ---------- image inference (select/upload) ----------
def predict_from_selected(path):
    """
    Read image from disk (cv2.imread -> BGR), run YOLO, return RGB.
    """
    if not path:
        return None
    bgr = cv2.imread(path)  # BGR
    if bgr is None:
        return None
    return _yolo_on_bgr_return_rgb(bgr)

def predict_from_upload(file):
    """
    'file' is a tempfile path from Gradio Upload; read (BGR) -> YOLO -> RGB.
    """
    if file is None:
        return None
    # file can be dict-like or str depending on Gradio version; handle both
    path = file if isinstance(file, str) else getattr(file, "name", None)
    if not path:
        return None
    bgr = cv2.imread(path)
    if bgr is None:
        return None
    return _yolo_on_bgr_return_rgb(bgr)

# ---------- UI ----------
def show():
    gr.Markdown("## Live Emotion Recognition")

    with gr.Tabs():
        with gr.Tab("Webcam"):
            cam = gr.Image(
                sources=["webcam"],
                streaming=True,
                type="numpy",
                image_mode="RGB",   # Gradio expects RGB
                show_label=False,
            )
            cam.stream(fn=predict_webcam, inputs=cam, outputs=cam)

        with gr.Tab("Image Inference"):
            with gr.Row():
                selector = gr.Dropdown(
                    choices=ASSET_OPTIONS,
                    value=ASSET_OPTIONS[0] if ASSET_OPTIONS else None,
                    label="Choose a repo image",
                )
                run_btn = gr.Button("Run on Selected")
            out_sel = gr.Image(label="Selected Image Result", interactive=False)

            run_btn.click(fn=predict_from_selected, inputs=selector, outputs=out_sel)

            gr.Markdown("---")
            uploader = gr.File(label="Or upload an image", file_types=["image"])
            out_up = gr.Image(label="Uploaded Image Result", interactive=False)
            uploader.change(fn=predict_from_upload, inputs=uploader, outputs=out_up)

if __name__ == "__main__":
    with gr.Blocks(theme=gr.themes.Glass()) as demo:
        show()
    demo.launch(server_name="0.0.0.0", server_port=7860)