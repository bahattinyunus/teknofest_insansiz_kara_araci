# 🛰️ Operasyonel Protokoller (Standard Operating Procedures)

Bu döküman, sistemin güvenli ve etkili bir şekilde devreye alınması için gereken protokolleri tanımlar.

---

## 🏁 Bölüm 1: Ön Hazırlık Protokolü (Pre-Flight)
1. **Güç Kontrolü:** Batarya voltajının 12.6V (3S) veya 16.8V (4S) seviyesinde olduğundan emin olun.
2. **Sensör Temizliği:** LiDAR aynasının ve kamera lenslerinin tozdan arındırılması.
3. **Haberleşme:** Yer istasyonu ile robot arasındaki gecikmenin (latency) < 50ms olması.

## 🚀 Bölüm 2: Operasyon Başlatma
Sistemi ayağa kaldırmak için terminalde şu sıralamayı izleyin:

```bash
# 1. Hardware abstraction layer (HAL)
ros2 launch ika_bringup hardware.launch.py

# 2. Perception & Localization
ros2 launch ika_perception intelligence.launch.py

# 3. Navigation & Mission Control
ros2 run ika_mission mission_manager
```

## ⚠️ Bölüm 3: Acil Durum Protokolü (Fail-Safe)
Sistem aşağıdaki durumlarda otomatik olarak **HARD-STOP** moduna geçer:
- Lidar verisi kesilirse.
- Engel mesafesi < 5cm olursa.
- ROS2 Heartbeat mesajı gelmezse.

---
> [!IMPORTANT]
> Operasyon sırasında robotun 2 metre çapında kimsenin bulunmadığından emin olun.
