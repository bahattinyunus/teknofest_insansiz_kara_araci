import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class MissionManager(Node):
    """
    Teknofest IKA Gorev Yoneticisi
    Sirasiyla: Kalkis -> Devriye -> Hedef Tespiti -> Aksiyon -> Donus
    """
    def __init__(self):
        super().__init__('mission_manager')
        self.state = "IDLE"
        self.get_logger().info('Gorev Yoneticisi Aktif. Durum: %s' % self.state)
        
        # Basit bir durum makinesi timer'i
        self.timer = self.create_timer(2.0, self.state_machine)

    def state_machine(self):
        if self.state == "IDLE":
            self.get_logger().info("Gorev Baslatiliyor...")
            self.state = "NAVIGATING"
        
        elif self.state == "NAVIGATING":
            self.get_logger().info("Hedef Noktasina Gidiliyor...")
            # Burada Nav2'ye goal gonderilir
            self.state = "SEARCHING"
            
        elif self.state == "SEARCHING":
            self.get_logger().info("Hedef Araniyor (YOLOv8 Aktif)...")
            # Görüntü işleme verisi beklenir
            self.state = "ACTION"
            
        elif self.state == "ACTION":
            self.get_logger().info("Hedef Tespit Edildi! Aksiyon Icra Ediliyor...")
            self.state = "COMPLETED"
            
        elif self.state == "COMPLETED":
            self.get_logger().info("Gorev Tamamlandi. Baslangic Noktasina Donuluyor.")
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = MissionManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
