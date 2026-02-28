# 🧠 AI Eğitim ve Yaygınlaştırma Hattı (Pipeline)

Bu belge, Gökbörü İKA'nın görsel zekasının (YOLOv8) nasıl eğitildiğini ve optimize edildiğini açıklar.

## 🛡️ 1. Veri Toplama (Sourcing)
- **Gerçek Zamanlı Veri:** Yarışma parkuru ve benzeri ortamlardan alınan 10k+ kare.
- **Sentetik Veri:** Gazebo ve Unity tabanlı simülasyonlardan otomatik etiketlenmiş görüntüler.
- **Data Augmentation:** Parlaklık değişimi, gürültü ekleme ve perspektif kaydırma ile modelin dayanıklılığı artırılır.

## 🏷️ 2. Etiketleme (Labeling)
- **Format:** YOLOv8 (normalized x_center, y_center, width, height).
- **Araçlar:** CVAT / Roboflow.
- **Sınıflar (Classes):**
    1. `Obstacle` (Genel Engel)
    2. `Human` (Canlı Unsur)
    3. `Sign_Stop` (Dur Tabelası)
    4. `Sign_Direction` (Yön Tabelası)

## ⚡ 3. Model Optimizasyonu (TensorRT)
Jetson Orin üzerinde gerçek zamanlı (30+ FPS) performans için model dönüştürme:
```bash
yolo export model=yolov8n.pt format=engine device=0 half=true
```

## 📈 Performans Metrikleri
- **mAP@.5:** 0.85+
- **Inference Latency:** < 20ms (Jetson Orin)
- **False Positive Rate:** < %2

---
> [!TIP]
> Eğitim aşamasında `transfer learning` kullanılarak COCO datasetindeki ağırlıklar başlangıç noktası olarak alınır.
