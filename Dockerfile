# ==========================================
# STAGE 1: Build & Dependency Resolution
# ==========================================
FROM osrf/ros:humble-desktop-full AS builder

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /build_ws/src

# Install build dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy code and install dependencies
COPY . /build_ws/src/teknofest_insansiz_kara_araci
WORKDIR /build_ws
RUN pip3 install --no-cache-dir -r src/teknofest_insansiz_kara_araci/requirements.txt || true

# ==========================================
# STAGE 2: Optimized Production Runtime
# ==========================================
FROM osrf/ros:humble-desktop-full

LABEL maintainer="bahattinyunus"
LABEL project="Gökbörü İKA"

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /home/gokboru_ws

# Copy built artifacts if any, and dependencies
COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
COPY . src/teknofest_insansiz_kara_araci

# Final environment tuning
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "alias guardian='python3 /home/gokboru_ws/src/teknofest_insansiz_kara_araci/scripts/guardian_cli.py'" >> ~/.bashrc

CMD ["/bin/bash"]
