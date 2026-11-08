# Prokudin-Gorskii Color Image Reconstruction

## 📌 Project Overview
This repository contains the implementation of a digital image processing assignment focused on historical color photography preservation. Using the archival glass plate negatives from the **Library of Congress Prokudin-Gorskii Collection**, the project downloads 3-frame glass plate images (comprising Blue, Green, and Red color channels stacked vertically) and processes them to synthesize a single, full-color RGB image.

---

## 🛠️ Assignment Steps & Implementation

1. **Dataset Acquisition (`loc.gov`):** Downloaded at least 10 high-resolution 3-frame glass plate images from the official Library of Congress Prokudin-Gorskii archive.
2. **Image Cropping (Channel Separation):** Sliced each vertical source image into its 3 individual constituent color channels (Blue, Green, and Red).
3. **Channel Alignment & Combination:** Aligned the separate channels to correct shifts and combined them into a single integrated color image.
4. **Visualization & Plotting:** Generated analytical plots displaying each individual color channel separately alongside the final synthesized color image.

