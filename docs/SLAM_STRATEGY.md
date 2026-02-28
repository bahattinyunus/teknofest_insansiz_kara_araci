# 🛰️ Gökbörü SLAM Stratejisi (Dinamik Haritalama)

Bu belge, otonom aracın bilinmeyen ortamlarda konumunu belirleme ve eş zamanlı haritalama (SLAM) yapma stratejisini detaylandırır.

## 🛠️ Yaklaşım 1: 2D Lidar SLAM (Başlangıç)
*Kullanılan Araçlar: SLAM Toolbox / Gmapping*

- **Girdi:** 2D Lidar Scan + Odometri (Encoder).
- **Avantaj:** Düşük hesaplama gücü (Jetson Nano/Orin Nano dostu).
- **Dezavantaj:** Engebeli arazilerde (z-ekseni değişimi) harita bozulması.

## 🚀 Yaklaşım 2: 3D Lidar-Inertial SLAM (İleri Seviye)
*Hedeflenen Algoritma: LIO-SAM (Lidar Inertial Odometry via Smoothing and Mapping)*

Gökbörü projesi, Teknofest ve uluslararası arenalarda yüksek hassasiyet için **LIO-SAM** mimarisini benimser:

- **Tight Coupling:** IMU verileri ile Lidar bulutları "sıkı bağ" yöntemiyle birleştirilir. Bu, ani robot hareketlerindeki kaymaları önler.
- **Loop Closure:** Robot daha önce geçtiği bir noktayı tanıdığında harita üzerindeki kümülatif hataları düzeltir.
- **Factor Graph:** Veriler bir faktör grafiği üzerinde optimize edilerek gerçek zamanlı performans sağlanır.

## 📊 Donanım Gereksinimleri
| Sensör | Model (Önerilen) | Rol |
| :--- | :--- | :--- |
| **Lidar** | Velodyne VLP-16 / Ouster OS1 | 3D Çevresel Tarama |
| **IMU** | Xsens Mti / Bosch BNO055 | Oryantasyon ve İvme |
| **GPS** | RTK-GNSS (U-blox F9P) | Global Konum Düzeltme |

---
> [!IMPORTANT]
> SLAM performansı, sensör kalibrasyonunun (extrinsics) doğruluğuna doğrudan bağlıdır. Tüm sensörler `base_link` merkezine göre mm hassasiyetinde tanımlanmalıdır.
