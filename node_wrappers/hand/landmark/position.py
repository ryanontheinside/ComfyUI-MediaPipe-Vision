# node_wrappers/hand/position.py
import logging
from typing import List, Tuple, Any, Optional

# Import the base class
from ...common.universal_landmark_nodes import LandmarkPositionBaseNode
# Import the specific landmark type for clarity and potential future use
from ....src.types import HAND_LANDMARKS

logger = logging.getLogger(__name__)
_category = "MediaPipeVision/Hand/HandLandmark/Position"

class HandLandmarkPositionNode(LandmarkPositionBaseNode):
    """Extracts position lists (x, y, z, vis, pres) for a specific landmark index
       from HAND_LANDMARKS across the batch."""
    CATEGORY = _category
    # Define the specific input type string this node expects
    LANDMARKS_TYPE = "HAND_LANDMARKS"
    DESCRIPTION = "Extracts lists of coordinates (x, y, z) and properties (visibility, presence) for a specific Hand Landmark index across an entire batch. Supports world coordinates. Outputs separate lists for each property."

    @classmethod
    def INPUT_TYPES(cls):
        # Define the specific input type for this node
        return {
            "required": {
                "landmarks": (cls.LANDMARKS_TYPE, {"forceInput": True}),
                "landmark_index": ("INT", {"default": 8, "min": 0, "max": 20, "tooltip": "Index Tip=8, Thumb Tip=4"}), # Hand specific default/range
                "use_world_coordinates": ("BOOLEAN", {"default": False, "tooltip": "Use world coordinates if available"}),
            }
        }

# --- Node Mappings ---
NODE_CLASS_MAPPINGS = {
    "HandLandmarkPosition": HandLandmarkPositionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HandLandmarkPosition": "Hand Landmark Position Extractor (Batch)",
} 