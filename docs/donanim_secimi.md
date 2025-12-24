# 🛠️ İKA Donanım Seçimi Rehberi

İnsansız Kara Aracı (İKA) tasarımında donanım seçimi, yazılımın başarısını doğrudan etkiler. İşte standart bir otonom İKA için önerilen bileşenler:

## 1. Merkezi İşlem Birimleri (Computing)
- **NVIDIA Jetson Orin Nano/NX:** AI ve görüntü işleme görevleri için en güçlü seçenek.
- **Raspberry Pi 5:** Daha düşük bütçeli veya hafif görevli araçlar için uygun.

## 2. Sensörler (Sensing)
- **LiDAR:** 
    - *LD19 (LDROBOT)* veya *RPLidar A1/A2 M8* (Başlangıç seviyesi)
    - *Hokuyo* veya *Velodyne* (Endüstriyel seviye)
- **Kameralar:**
    - *Intel RealSense D435i/D455:* Derinlik algısı ve SLAM için standart.
    - *OAK-D:* Dahili AI işlemcili stereo kamera.
- **IMU:** 
    - *BNO055* veya *WitMotion* serisi (Otonomi için kritik).

## 3. Tahrik ve Güç Sistemi
- **Motorlar:** Yüksek torklu DC fırçasız motorlar veya Step motorlar.
- **Batarya:** Li-Po veya Li-Ion (Yüksek deşarj kapasiteli).
- **Şasi:** Paletli sistemler (Engebeli arazi) veya Tekerlekli Ackerman (Hız).

---
> [!TIP]
> Gazebo simülasyonunda seçeceğiniz donanımların `.urdf` modellerinin olup olmadığını kontrol edin.
