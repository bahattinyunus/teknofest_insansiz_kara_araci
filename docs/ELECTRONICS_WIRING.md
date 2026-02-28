# ⚡ Gökbörü Hardware Architecture & Electronics Wiring

Bu belge, otonom Kara Aracı'nın (İKA) fiziksel dünyayla nasıl etkileşime girdiğini, güç dağıtım matrisini ve sensör-bilgisayar arası iletişim protokollerini açıklar. **Bir robotik sistemin yazılımı ne kadar iyi olursa olsun, kalitesiz bir kablolama ve sinyal gürültüsü otonomiyi felç edecektir.**

## 1. Merkezi Hesaplama ve Veri Yolu (Compute Node)

Sistemin kalbinde, yoğun yapay zeka (YOLOv8) ve Navigasyon (Nav2, SLAM) işlemlerini yöneten **NVIDIA Jetson Orin Nano / Xavier NX** bulunur.

- **Düşük Seviye Kontrol (MCU):** Jetson, motor sürücülerine doğrudan pwm yollamaz. Bunun yerine, bir mikrodenetleyici (Örn: STM32F4 veya Teensy 4.1) ile haberleşir. 
- **Haberleşme Protokolü:** Jetson ile MCU arasında **CAN-Bus (Controller Area Network)** veya donanımsal **UART (Baud: 921600)** kullanılır. CAN-Bus, dış mekan (Teknofest) şartlarındaki elektriksel gürültüye (EMI) karşı çok daha dirençlidir. ROS2 ortamında `ros2_canopen` paketi üzerinden veriler `Twist` (Hız) ve `Odometry` (Tekerlek enkoderleri) mesajlarına çevrilir.

## 2. Sensör Matrisi ve Arayüzler

Araç üzerindeki her bir sensörün bant genişliği ve gecikme toleransları farklıdır:

| Sensör | Bağlantı Tipi | Frekans | Amaç |
| :--- | :--- | :---: | :--- |
| **2D / 3D LiDAR (Örn: RPLidar S2 / Velodyne)** | Ethernet (UDP) veya USB 3.0 | 10Hz - 20Hz | Pointcloud, Costmap Oluşturma, Engelden Kaçma |
| **ZED 2i / Intel RealSense (Depth Cam)** | USB 3.0 (Type-C, Yüksek Bant) | 30 FPS | V-SLAM, Derinlik Odometrisi (Visual Odometry), YOLOv8 |
| **IMU (Örn: BNO085, Pixhawk)** | I2C / SPI / CAN-Bus | 100Hz+ | Aracın yönelimi (Heading), EKF (Kalman Filtresi) beslemesi |
| **RTK GPS / GNSS** | UART (Seri Port) | 5Hz - 10Hz | Küresel Konumlandırma, Mutlak Koordinat referansı |

## 3. Güç Dağıtım ve Yönetim (Power Matrix)

İnsan taşıyabilen ağırlıktaki İKA'lar ciddi akım çeker. Sistem voltaj düşümlerini izole etmek için parçalı bir Batarya Yönetim Sistemi (BMS) kullanır.

- **Ana Kaynak:** 24V veya 48V Li-Ion / Li-Po Batarya (Örn: 6S 22000mAh)
- **Tahrik Hattı (Motorlar):** Bataryadan doğrudan (kalın AWG kablolarla ve dev sigortalarla) motor sürücülerine çekilir.
- **Lojik Hattı (Bilgisayar & Sensörler):** Motorların kalkış anında çektiği yüksek akım, voltajın anlık düşmesine neden olup Jetson'ı resetleyebilir. Bu yüzden araya:
  - **24V to 19V Buck/Boost Converter:** Jetson için stabil güç.
  - **24V to 12V Converter:** Lidar ve ağ Switch'leri için.
  - **24V to 5V (BEC):** MCU, sensörler ve Encoder devreleri için özel izole hat çekilir.

### 🛡️ Kritik Güvenlik (E-Stop) Altyapısı
Araç üzerinde **Donanımsal Acil Stop (E-Stop)** butonu bulunur. Yazılımsal acil durdurma (Cyber Defense Node) ne kadar iyi olursa olsun, E-Stop butonuna basıldığında motor sürücülerinin *Güç (VCC)* hattı fiziksel olarak kesilir, ancak Lojik hattı (Jetson/Sensörler) açık kalıp veri toplamaya devam eder.
