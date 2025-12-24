# ⚡ Elektronik ve Güç Sistemi Mimari Reçetesi

Otonom bir aracın "kalbi" olan elektronik sistemlerin bağlantı şeması ve prensipleri.

## 1. Güç Dağıtım Ünitesi (PDU)
- **Ana Güç:** 3S (11.1V) veya 4S (14.8V) LiPo Batarya.
- **Regülasyon:**
    - Jetson Orin için: 5V/4A veya 12V regülatör (Modeline göre).
    - Motor Sürücüleri: Doğrudan batarya voltajı.
    - Sensörler (Lidar/Cam): USB üzerinden veya 5V/12V regüleli hat.

## 2. Veri Akışı ve Haberleşme
- **Master:** Nvidia Jetson (ROS2).
- **Slave:** STM32 veya Arduino (Motor Kontrolcü & Encoder okuyucu).
- **Protocol:** UART, CAN Bus veya USB-Serial.

## 3. Kablolama ve Gürültü (EMI)
- Yüksek akım geçen kabloları (motor kabloları), veri kablolarından (lidar/cam) uzak tutun.
- Ferrit halkalar (ferrite beads) kullanarak elektriksel gürültüyü minimize edin.

---
> [!CAUTION]
> Ters polarlama (artı-eksi ters bağlama) ana işlemcinizi yakabilir. Daima multimetre ile kontrol yapın!
