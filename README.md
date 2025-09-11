<p align="center">
  <img src="assets/Logo_Finpro_AbuLearn.png" alt="AbuLearn Logo" width="240">
</p>

<h1 align="center">AbuLearn — Expression Classification for E-Learning Support</h1>

<p align="center">
  <a href="https://huggingface.co/spaces/ghozyreuski/abulearn-expression-detector">
    <img alt="Deploy on Hugging Face" src="https://img.shields.io/badge/Deploy-HuggingFace-blue?logo=huggingface">
  </a>
</p>

## Repository Outline
```
p2-final-project-ftds-030-hck-group01-abulearn-project
│
├── /assets                         # Project's logo
│                     
├── /deploy/deploy_model                   # Packages for for deployment
│          ├── best.pt                     # Fine-tune model
│          └── deploy_config.json          # Best model configuration
│
├── /inf_images                     # Input images for inference ()
│
├── /raw_data                       # Raw dataset from kaggle
│
├── /sample_data                    # Sample dataset (7000 images) for training
│
│
├── abulearn_project_inference.ipynb             # Inference notebook
├── abulearn_project.ipynb                       # Main notebook
├── engagement_level.yaml                        # YOLO dataset config (paths & class names)
├── README.md                                    # Documentation
└── yolov8n.pt                                   # YOLO baseline model
```
---

## Our goal

<div align="justify">

Give educators lightweight, real-time insight into student engagement during online classes by classifying facial expressions (not identities) and summarizing session-level trends, so teaching can be adapted quickly.

## Problem statement

<div align="justify">

Online learning reduces the natural feedback teachers get in physical classrooms. Without clear non-verbal cues, it’s hard to gauge attention, confusion, or disengagement. We need a privacy-aware system that infers engagement signals from facial expressions to support timely teaching interventions, without recording or identifying students.

## Objective

<div align="justify">

- Build a computer-vision model to classify facial expressions into **eight emotions**: Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, and Surprise.
- Aggregate these emotions into **three engagement states** for simpler, actionable analytics:
  - **Very Engaged** = Happy, Surprise  
  - **Nominally Engaged** = Fear, Disgust, Contempt  
  - **Not Engaged** = Neutral, Sad, Anger
- Use the predicted engagement to inform **adaptive teaching strategies** (e.g., add interactive content when engagement drops, or provide clarification when confusion is detected).

## Dataset

<div align="justify">

- **Source:** [AffectNet (YOLO format) on Kaggle](https://www.kaggle.com/datasets/fatihkgg/affectnet-yolo-format)  
  **Usage in this project:** We downloaded **only the `train/` split** and used it as our **raw_data** (≈ **17.1k** image–label pairs).

- **Classes (8):**  
  `Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, Surprise`

## References

<div align="justify">

Madake, J., Shende, S., Bhatlawande, S., Shinde, R., Govekar, S., & Shilaskar, S. (2022).  
Student attentiveness detection system using deep learning. *2022 International Conference on Computational Performance Evaluation (ComPE)*, 498–502.  
https://doi.org/10.1109/ComPE57225.2022.10014782  

Barz, B., & Denzler, J. (2020).  
Do we train on test data? Purging CIFAR of near-duplicates. *Journal of Machine Learning Research, 21*(248), 1–38.  
https://arxiv.org/abs/1902.00423  

Sharma, M., Kaplan, B., Feizi, S., Goldblum, M., & Goldstein, T. (2019).  
On the importance of label quality for fine-grained classification. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops*, 1–10.  
https://arxiv.org/abs/1909.12913  

Reddit. (2020, April 21).  
Would duplicate images in a dataset noticeably affect training? *r/MachineLearning*. Retrieved from  
https://www.reddit.com/r/MachineLearning/comments/g7gxah/d_would_duplicate_images_in_a_dataset_noticeably/

---