# Gökbörü SOTM - Elite Development Environment
FROM osrf/ros:humble-desktop-full

# Set non-interactive to avoid timezone prompts during builds
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    git \
    wget \
    curl \
    nano \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /home/gokboru_ws

# Copy repository contents into the container workspace
COPY . src/teknofest_insansiz_kara_araci

# Install Python requirements
RUN pip3 install --no-cache-dir -r src/teknofest_insansiz_kara_araci/requirements.txt || echo "No requirements.txt found or failed to install"

# Source ROS 2 base and alias the guardian CLI for easy access
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "alias guardian='python3 /home/gokboru_ws/src/teknofest_insansiz_kara_araci/scripts/guardian_cli.py'" >> ~/.bashrc

CMD ["/bin/bash"]
