<p align="center">
  <img src="assets/Logo_Finpro_AbuLearn.png" alt="AbuLearn Logo" width="240">
</p>

<h1 align="center">AbuLearn — Expression Classification for E-Learning Support</h1>

<p align="center">
  <a href="https://huggingface.co/spaces/ghozyreuski/abulearn-expression-detector">
    <img alt="Deploy on Hugging Face" src="https://img.shields.io/badge/Deploy-HuggingFace-blue?logo=huggingface">
  </a>
</p>

---

## Our goal
Give educators lightweight, real-time insight into student engagement during online classes by classifying facial expressions (not identities) and summarizing session-level trends—so teaching can be adapted quickly.

## Problem statement
Online learning reduces the natural feedback teachers get in physical classrooms. Without clear non-verbal cues, it’s hard to gauge attention, confusion, or disengagement. We need a privacy-aware system that infers engagement signals from facial expressions to support timely teaching interventions—without recording or identifying students.

## Objective
lorem ipsum dolor jamet

## Dataset
- **Source:** [AffectNet (YOLO format) on Kaggle](https://www.kaggle.com/datasets/fatihkgg/affectnet-yolo-format)  
  The dataset is provided in YOLO-style format and is already split into `train`, `val`, and `test` sets.

- **Classes (8):**  
  `Anger, Contempt, Disgust, Fear, Happy, Neutral, Sad, Surprise`

- **Directory layout:**

## References

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

