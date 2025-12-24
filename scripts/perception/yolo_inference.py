import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YOLOInferenceNode(Node):
    def __init__(self):
        super().__init__('yolo_inference_node')
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt') # Model yolu buraya
        self.subscription = self.create_subscription(
            Image,
            'camera/image_raw',
            self.image_callback,
            10)
        self.get_logger().info('YOLOv8 Inference Node Aktif...')

    def image_callback(self, msg):
        # ROS Görüntüsünü OpenCV'ye çevir
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        # Çıkarım yap
        results = self.model(cv_image, stream=True)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Tespit edilen nesne bilgileri
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                if conf > 0.5:
                    self.get_logger().info(f'Nesne Tespit Edildi: Sınıf {cls}, Güven {conf:.2f}')
        
def main(args=None):
    rclpy.init(args=args)
    node = YOLOInferenceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
