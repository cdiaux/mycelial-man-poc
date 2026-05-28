from dataclasses import dataclass
import time
import json

@dataclass
class GraftProposal:
    source_org: str
    target_org: str
    layer_name: str
    delta_b64: str           # AES-encrypted + Base64
    shape: list
    surprise_score: float
    privacy_cost: float
    graft_id: str
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

    def to_dict(self):
        return {
            "source_org": self.source_org,
            "target_org": self.target_org,
            "layer_name": self.layer_name,
            "delta_b64": self.delta_b64,
            "shape": self.shape,
            "surprise_score": self.surprise_score,
            "privacy_cost": self.privacy_cost,
            "graft_id": self.graft_id,
            "timestamp": self.timestamp,
        }
