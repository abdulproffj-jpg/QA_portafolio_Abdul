import os
import requests

# Base folder
base_dir = "cv-website"
logos_dir = os.path.join(base_dir, "logos")
os.makedirs(logos_dir, exist_ok=True)

# Example Icons8 direct links (replace with the ones you need)
icons = {
    "selenium.png": "https://img.icons8.com/color/96/selenium-test-automation.png",
    "appium.png": "https://img.icons8.com/color/96/appium.png",
    "java.png": "https://img.icons8.com/color/96/java-coffee-cup-logo.png",
    "python.png": "https://img.icons8.com/color/96/python.png",
    "javascript.png": "https://img.icons8.com/color/96/javascript.png",
    "mysql.png": "https://img.icons8.com/color/96/mysql-logo.png",
    "postgresql.png": "https://img.icons8.com/color/96/postgreesql.png",
    "github.png": "https://img.icons8.com/material-outlined/96/github.png",
    "gitlab.png": "https://img.icons8.com/color/96/gitlab.png",
    "bitbucket.png": "https://img.icons8.com/color/96/bitbucket.png",
    "windows11.png": "https://img.icons8.com/color/96/windows-11.png",
    "linux.png": "https://img.icons8.com/color/96/linux.png",
    "oracle.png": "https://img.icons8.com/color/96/oracle-logo.png",
    "salesforce.png": "https://img.icons8.com/color/96/salesforce.png",
    "c.png": "https://img.icons8.com/color/96/c-programming.png",
    "cplusplus.png": "https://img.icons8.com/color/96/c-plus-plus-logo.png",
}

def download_and_save(name, url):
    try:
        print(f"Downloading {name}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        file_path = os.path.join(logos_dir, name)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved {name}")
    except Exception as e:
        print(f"❌ Failed {name}: {e}")

# Run downloads
for name, url in icons.items():
    download_and_save(name, url)

print("🎉 All icons downloaded into cv-website/logos/")
