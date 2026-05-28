import torch
import numpy as np

class DifferentialPrivacyEngine:
    def __init__(self, epsilon: float = 1.2, delta: float = 1e-5):
        self.epsilon = epsilon
        self.delta = delta
        self.budget = 8.0

    def privatize(self, tensor: torch.Tensor, sensitivity: float = 1.0) -> torch.Tensor:
        if self.budget <= 0:
            raise RuntimeError("Privacy budget exhausted")
        noise_scale = sensitivity * np.sqrt(2 * np.log(1.25 / self.delta)) / self.epsilon
        noise = torch.randn_like(tensor) * noise_scale
        self.budget -= self.epsilon
        return tensor + noise
