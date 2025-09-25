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
├── /deploy/deploy_model                   # Packages for deployment
│          ├── best.pt                     # Fine-tune model
│          └── deploy_config.json          # Best model configuration
│
├── /inf_images                     # Create this folder to input images before running inference
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

Provide recruiters with lightweight, real-time insights into **candidate engagement** during online interviews by classifying facial expressions (not identities) and summarizing session-level trends, so hiring decisions can be more objective and informed.

## Problem statement

<div align="justify">

Remote hiring has become the norm, but recruiters often struggle to assess **candidate focus, stress, or engagement** without face-to-face interaction.  
Traditional online interviews miss many non-verbal cues, which can lead to **bias, misjudgment, or incomplete evaluation**.  
We need a **privacy-aware system** that infers emotional and attentiveness signals from facial expressions to support HR decision-making — without storing or identifying personal data.


## Objective

<div align="justify">

- Build a **computer vision model** to classify facial expressions into **eight emotions**: Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, and Surprise.  
- Aggregate these emotions into **three engagement states** for HR-friendly analytics:
  - **Highly Engaged** = Happy, Surprise  
  - **Moderately Engaged** = Fear, Disgust, Contempt  
  - **Low Engagement** = Neutral, Sad, Anger  
- Provide **real-time engagement insights** during candidate interviews to support **fairer, data-informed hiring decisions**.  

## Dataset

<div align="justify">

- **Source:** [AffectNet (YOLO format) on Kaggle](https://www.kaggle.com/datasets/fatihkgg/affectnet-yolo-format)  
  **Usage in this project:** Only the `train/` split was used as **raw_data** (≈ **17.1k** image–label pairs).  

- **Classes (8):**  
  `Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, Surprise`

- **Engagement Mapping (3 states):**  
  - Highly Engaged → Happy, Surprise  
  - Moderately Engaged → Fear, Disgust, Contempt  
  - Low Engagement → Neutral, Sad, Anger  

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
