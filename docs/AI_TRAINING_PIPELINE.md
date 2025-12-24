# 🧠 AI Eğitim Hattı (YOLOv8 Pipeline)

İKA'nın nesneleri (tabela, engel, insan) tanıması için gereken yapay zeka eğitim süreci.

## 1. Veri Seti Hazırlığı
1. **Veri Toplama:** Parkur benzeri ortamlardan en az 500-1000 kare fotoğraf çekin.
2. **Etiketleme (Labeling):** [Roboflow](https://roboflow.com) veya [CVAT](https://cvat.ai) kullanarak `Traffic_Sign`, `Obstacle`, `Human` sınıflarını işaretleyin.
3. **Format:** Verileri `YOLOv8` formatında dışa aktarın.

## 2. Eğitim (Training)
```python
from ultralytics import YOLO

# Modeli yükle (Nano versiyonu Jetson için idealdir)
model = YOLO('yolov8n.pt')

# Eğitimi başlat
model.train(data='custom_data.yaml', epochs=100, imgsz=640)
```

## 3. Optimizasyon (TensorRT)
Jetson üzerinde yüksek FPS almak için modelinizi TensorRT formatına dönüştürün:
```bash
yolo export model=best.pt format=engine device=0
```

---
> [!TIP]
> Eğitim sırasında "Augmentation" (parlaklık, döndürme) kullanarak modelin farklı ışık koşullarına dayanıklılığını artırın.
