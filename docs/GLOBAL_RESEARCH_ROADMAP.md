# 🗺️ Global Araştırma ve Geliştirme Yol Haritası (2025-2026)

Bu belge, **Gökbörü İKA** projesinin uluslararası standartlara (URC, ERC, IGVC) ulaşması için izleyeceği teknik stratejiyi ve öğrenim kaynaklarını detaylandırır.

## 🚀 Faz 1: Algılama ve Durumsal Farkındalık (Perception)
*Hedef: Karışık dış mekanlarda %99.9 nesne tanıma ve hassas derinlik algısı.*

- **LIO-SAM Entegrasyonu:** Sadece Lidar değil, IMU ve Odometri verilerini sıkı bir şekilde bağlayan (tightly-coupled) LIO-SAM algoritmasına geçiş.
- **TensorRT Optimizasyonu:** YOLOv8 modellerinin Jetson Orin üzerinde nano-saniye seviyesinde çalışması için FP16/INT8 quantizasyonu.
- **Multi-Spectral Füzyon:** Termal kamera verilerinin RGB verileriyle üst üste bindirilerek gece/gündüz kesintisiz hedef tespiti.

## 🛰️ Faz 2: Otonom Navigasyon ve Karar Mekanizmaları
*Hedef: Dinamik engeller arasında akıcı ve etik rota planlama.*

- **Nav2 Behavior Trees:** Karmaşık görevleri (örneğin: "hedefe git but engel varsa bekle ve yeniden planla") yönetmek için davranış ağları (Behavior Trees) kullanımı.
- **MPC (Model Predictive Control):** Klasik PID yerine, aracın fiziksel sınırlarını ve gelecekteki durumunu hesaba katan Model Öngörülü Kontrol.
- **VFH+ (Vector Field Histogram):** Klasik costmap yerine, yerel engellerden kaçarken aracın hız vektörünü anlık optimize eden algoritma.

## ⚙️ Faz 3: Sistem Güvenilirliği ve Yazılım Mimarisi
*Hedef: Endüstriyel seviyede (Level 4/5) otonomi ve hata toleransı.*

- **Lifecycle Nodes:** ROS2 yönetilebilir düğüm (Managed Nodes) yapısına geçerek, sensörler hazır olmadan navigasyonun başlamasını engellemek.
- **DDS QoS Profilleme:** Kritik veriler (komutlar) için `Reliable`, yüksek hacimli veriler (lidar) için `Best Effort` profillerinin yapılandırılması.
- **HIL (Hardware-in-the-Loop):** Gerçek kontrol kartlarını (Pixhawk/STM32) Gazebo simülasyonuna bağlayarak donanım bazlı testler.

## 📚 Referans Alınan Ekosistemler
- [RoboJackets Software Docs](https://github.com/RoboJackets/igvc-software) - Modüler yapı ve CI/CD standartları.
- [ERC Remote Navigation](https://github.com/EuropeanRoverChallenge/ERC-Remote-Navigation-Sim) - Uzaktan operasyon ve telemetri protokolleri.
- [URC Autonomy Solutions](https://github.com/RoboNav-URC) - Dış mekan otonomisi ve waypoint yönetimi.

---
> [!TIP]
> Bu yol haritası statik değildir. Her yarışma dönemi sonunda elde edilen tecrübelerle güncellenir.
