import os

README_PATH = 'README.md'

try:
    with open(README_PATH, 'r', encoding='utf-16le') as f:
        content = f.read()
except:
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

# 1. Add Lore Link if not exists
lore_badge = "\n| **[📖 PROTOCOL ZERO (GÖKBÖRÜ LORE)](docs/LORE.md)** |"
if "PROTOCOL ZERO" not in content and "| **[IV. 2025" in content:
    content = content.replace("| **[IV. 2025", lore_badge + "\n| **[IV. 2025")

# 2. Add Epic Quote after badges
quote = """
> _"Savaş alanı artık barut ve çelikten ibaret değil; silikon, algoritmalar ve görünmez frekansların saltanatı başladı."_
> 
> **— [Gökbörü Manifesto / Protocol Zero](docs/LORE.md)**
"""
if "silikon, algoritmalar ve görünmez" not in content:
    # insert after the div align center closes
    parts = content.split("</div>", 1)
    if len(parts) == 2:
        content = parts[0] + "</div>\n\n" + quote + parts[1]

# 3. Add Mermaid Diagram
mermaid = """
### 🧠 Neural Architecture & Sensor Fusion Diagram

```mermaid
graph TD
    subgraph SENSORS [Sensor Fusion Matrix]
        L[LiDAR VLP-16] -->|Point Cloud 3D| FUS{Fusion Engine}
        C[ZED 2i Depth Cam] -->|RGB-D| FUS
        I[IMU 9-DOF] -->|Orientation| FUS
    end
    
    subgraph AI [Tonyukuk Neural Core]
        FUS -->|Unified Workspace| YOLO[YOLOv8 TensorRT]
        YOLO -->|Threat / Target| NAV[Nav2 A* Planner]
    end
    
    subgraph CONTROL [Drive Systems]
        NAV -->|Vector| PID[Dynamic PID Controller]
        PID --> M1(Motor FL/RL)
        PID --> M2(Motor FR/RR)
    end
    
    style SENSORS fill:#020617,stroke:#38bdf8,stroke-width:2px,color:#fff
    style AI fill:#020617,stroke:#818cf8,stroke-width:2px,color:#fff
    style CONTROL fill:#020617,stroke:#34d399,stroke-width:2px,color:#fff
```
"""
if "Neural Architecture & Sensor Fusion Diagram" not in content:
    if "## 🧩 Sistem Mimarisi" in content:
        content = content.replace("## 🧩 Sistem Mimarisi", "## 🧩 Sistem Mimarisi\n" + mermaid)

# 4. Add Terminal Start
terminal = """
### ⚡ System Ignition (Guardian AI)

To initialize the simulated diagnostic interface and experience the power of the Gökbörü core:

```bash
# [<] Bypassing root security protocol...
$ git clone https://github.com/bahattinyunus/teknofest_insansiz_kara_araci.git
$ cd teknofest_insansiz_kara_araci

# [<] Initiating Sentinel Diagnostic
$ python scripts/guardian_cli.py
```
"""
if "System Ignition (Guardian AI)" not in content:
    if "## 🛠️ Kurulum" in content:
         content = content.replace("## 🛠️ Kurulum", "## 🛠️ Kurulum\n" + terminal)

try:
    with open(README_PATH, 'w', encoding='utf-16le') as f:
        f.write(content)
except Exception:
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("README enhanced with Mermaid, Quotes, and Terminal commands.")
