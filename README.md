# Step 1: สร้าง venv (optional)
python -m venv venv
source venv/bin/activate  # บน Windows: venv\Scripts\activate

# Step 2: ติดตั้ง lib
pip install -r requirements.txt

# Step 3: รัน detect / change path to images
python detect.py

output will be save in path runs/detect/exp
