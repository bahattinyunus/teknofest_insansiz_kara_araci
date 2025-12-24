import cv2
import numpy as np

def detect_traffic_sign(frame):
    # Basit bir renk maskeleme ile tabela (kirmizi) tespiti örneği
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Kirmizi renk araligi
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask = mask1 + mask2
    
    # Kontur bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Kirmizi Nesne/Tabela", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return frame

def main():
    # Kamera akisini simüle et veya dosyadan oku
    # cap = cv2.VideoCapture(0)
    print("Görüntü işleme örneği başlatılıyor... (Kamera kapalıdır)")
    
if __name__ == "__main__":
    main()
