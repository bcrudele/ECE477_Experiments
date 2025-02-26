import supervision as sv
import numpy as np
from collections import deque

class BallTracker:
    def __init__(self, buffer_size: int = 10):
        self.buffer = deque(maxlen=buffer_size)

    def update(self, detections: sv.Detections) -> sv.Detections:
        xy = detections.get_anchors_coordinates(sv.Position.CENTER)
        self.buffer.append(xy)

        if len(detections) == 0:
            return detections

        centroid = np.mean(np.concatenate(self.buffer), axis=0)
        distances = np.linalg.norm(xy - centroid, axis=1)
        index = np.argmin(distances)
        return detections[[index]]

def callback(patch: np.ndarray) -> sv.Detections: 
    result = model.infer(patch, confidence=0.3)[0]
    return sv.Detections.from_inference(result)

h, w, _ = frame.shape

slicer = sv.InferenceSlicer(
    callback = callback,
    overlap_filter = sv.OverlapFilter.NON_MAX_SUPPRESSION,
    slice_wh = (w // 2 + 100, h // 2 + 100),
    overlap_ratio_wh = None,
    overlap_wh = (100, 100),
    iou_threshold = 0.1
)

detections = slicer(frame)