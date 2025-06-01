import torch
from pathlib import Path

# Load model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

# Run inference
results = model('data/images/test_2.jpg')  # changes path to images

# Save or show
results.print()
results.save()  # output saved in runs/detect/exp
