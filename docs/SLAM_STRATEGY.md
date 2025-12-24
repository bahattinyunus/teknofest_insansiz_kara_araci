# 🗺️ SLAM Stratejisi ve Haritalama Rehberi

Teknofest İKA parkurunda başarılı bir otonomi için yüksek hassasiyetli bir harita şarttır.

## 1. Algoritma Seçimi
- **SLAM Toolbox (Asynchronous):** Dinamik ve büyük haritalar için ROS2 ekosisteminde en kararlı seçenektir.
- **Google Cartographer:** LiDAR + IMU entegrasyonu (Loop Closure) konusunda üstündür ancak konfigürasyonu daha karmaşıktır.

## 2. Kritik Parametreler
- `resolution:` 0.05 (Donanım gücüne göre 0.01'e kadar çekilebilir).
- `max_laser_range:` Sensör kapasitesine göre set edilmeli (RPLidar A1 için ~12m).
- `minimum_time_interval:` 0.5sb (CPU yükünü azaltmak için).

## 3. Tuningleme İpuçları
- Aracınızı simülasyonda veya gerçekte çok hızlı döndürmeyin; lidar verilerinde "smearing" (bulanıklık) oluşur.
- Odometri verisinde kayma varsa, LiDAR tabanlı odometri (`rf2o` gibi) paketlerini deneyin.

---
> [!IMPORTANT]
> Haritayı kaydetmeyi unutmayın: `ros2 run nav2_map_server map_saver_cli -f my_map`
