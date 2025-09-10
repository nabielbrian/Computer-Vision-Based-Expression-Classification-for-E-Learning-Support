<p align="center">
  <img src="assets/Logo_Finpro_AbuLearn.png" alt="AbuLearn Logo" width="240">
</p>

<h1 align="center">AbuLearn — Expression Classification for E-Learning Support</h1>

<p align="center">
  <a href="https://huggingface.co/spaces/ghozyreuski/abulearn-expression-detector/tree/main/assets">
    <img alt="Deploy on Hugging Face" src="https://img.shields.io/badge/Deploy-HuggingFace-blue?logo=huggingface">
  </a>
</p>

---

## Our goal
Give educators lightweight, real-time insight into student engagement during online classes by classifying facial expressions (not identities) and summarizing session-level trends—so teaching can be adapted quickly and ethically.

## Problem statement
Online learning reduces the natural feedback teachers get in physical classrooms. Without clear non-verbal cues, it’s hard to gauge attention, confusion, or disengagement. We need a privacy-aware system that infers engagement signals from facial expressions to support timely teaching interventions—without recording or identifying students.

## Objective
- **Model:** Real-time, 8-class facial expression classifier (Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, Surprise).
- **Target UX:** Webcam input → live prediction + rolling engagement summary; exportable session report.
- **Performance:** Prioritize balanced accuracy/F1 across classes; latency suitable for live use on modest hardware.
- **Privacy:** No face ID; no raw video storage by default; on-device processing when possible.

## Dataset
- **Source format:** AffectNet (YOLO-style) split into train/val/test.
- **Classes (8):** `Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, Surprise`
- **Typical layout:**
