# 🛰️ Teknofest İKA: İstihbarat ve Strateji Özet Kararı

**DOKÜMAN NO:** İK-2025-TB-001  
**SINIFLANDIRMA:** ELITE / TACTICAL  
**KONU:** 2025 Yarışma Senaryosu ve Stratejik Yaklaşım

---

## 1. Görev Ortamı Analizi
Yarışma parkuru, fiziksel engellerin ötesinde; dinamik olarak değişen, karmaşık ışık koşullarına sahip ve haberleşme kısıtlarının olabileceği bir "Muharebe Alanı" simülasyonudur.

### Kritik Tehditler:
- **Dinamik Engeller:** Hareketli hedefler ve beklenmedik bariyerler.
- **Zayıf Işık/Gölge:** YOLOv8 modellerinin robust (dayanıklı) olmasını gerektiren değişken ortamlar.
- **Zemin Değişkenliği:** Tekerlekli araçlar için odometri kaymalarını tetikleyen kaygan/pürüzlü yüzeyler.

## 2. Stratejik Hedefler (Objectives)
- **Hız ve Hassasiyet:** Nav2 parametrelerinin parkur genişliğine göre optimize edilmesi.
- **Sıfır Hata Payı:** Hedef tespitinde %98+ doğruluk oranı.
- **Otonom Kurtarma:** Robotun sıkışma (stuck) durumundan 3 saniyenin altında çıkabilmesi.

---

## 3. Taktiksel Yol Haritası (Milestones)
1. **[FAZ-1]** Sensör Kalibrasyonu (Stereo & LiDAR alignment).
2. **[FAZ-2]** Haritalama ve Local Planner ince ayarları.
3. **[FAZ-3]** Yapay Zeka modelinin yerinde (edge device) test edilmesi.

> [!TIP]
> İstihbarat, başarının %50'sidir. Parkuru ezberlemek yerine, bilinmeyene karşı tepki veren bir algoritma geliştirin.
