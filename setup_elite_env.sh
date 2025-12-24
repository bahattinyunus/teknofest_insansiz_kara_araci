#!/bin/bash
set -e

echo "🚀 [ELITE] Teknofest IKA Gelistirme Ortami Hazirlaniyor..."

# ROS2 Humble Kurulum Kontrolu
if [ ! -d "/opt/ros/humble" ]; then
    echo "❌ ROS2 Humble bulunamadi! Lutfen once ROS2 Humble kurun."
    exit 1
fi

echo "✅ ROS2 Humble Tespit Edildi."

# Sistem Paketleri
echo "📦 Sistem paketleri guncelleniyor..."
sudo apt-get update && sudo apt-get install -y \
    python3-pip \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox

# Python Bagimliliklari
echo "🐍 Python bagimliliklari yukleniyor..."
pip3 install -r requirements.txt

echo "🏗️  Ortam Hazir! 'source /opt/ros/humble/setup.bash' komutunu calistirmayi unutmayin."
