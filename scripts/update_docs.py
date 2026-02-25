import os

README_PATH = 'README.md'
REQUIREMENTS_PATH = 'requirements.txt'

def update_readme():
    try:
        with open(README_PATH, 'r', encoding='utf-16le') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            
    badge = "[![AUV System CI/CD Pipeline](https://github.com/bahattinyunus/teknofest_insansiz_kara_araci/actions/workflows/ci.yml/badge.svg)](https://github.com/bahattinyunus/teknofest_insansiz_kara_araci/actions/workflows/ci.yml)\n\n"
    
    # insert badge under <img src="assets/ika_banner.svg" ...
    if "<img src=\"assets/ika_banner.svg\"" in content:
        parts = content.split(">", 2) # split around first img tag
        # we have to find the end of the img tag. It's safer to just split by banner.svg line
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "ika_banner" in line:
                lines.insert(i + 1, '\n' + badge)
                break
        new_content = '\n'.join(lines)
    else:
        new_content = badge + content
        
    # Append the new module info
    if "## 🧩 Sistem Mimarisi" in new_content:
        lines = new_content.split('\n')
        for i, line in enumerate(lines):
            if "## 🧩 Sistem Mimarisi" in line:
                lines.insert(i + 1, "- **Configuration Loader**: Merkezi yapılandırma ve parametre yönetimi (`config/robot_params.yaml`)")
                lines.insert(i + 2, "- **Test Automation**: `pytest` tabanlı CI/CD entegre otomatik test sistemi")
                break
        new_content = '\n'.join(lines)
        
    try:
        with open(README_PATH, 'w', encoding='utf-16le') as f:
            f.write(new_content)
    except Exception:
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("README updated.")

def update_requirements():
    with open(REQUIREMENTS_PATH, 'a', encoding='utf-8') as f:
        f.write("\npytest==7.4.3\npyyaml==6.0.1\nflake8==6.1.0\n")
    print("Requirements updated.")

if __name__ == '__main__':
    update_readme()
    update_requirements()
