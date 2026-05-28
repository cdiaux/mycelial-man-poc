from dataclasses import dataclass

@dataclass
class Config:
    model_id: str = "meta-llama/Llama-3.2-1B-Instruct"
    lora_rank: int = 8
    lora_alpha: int = 16
    dp_epsilon: float = 1.2
    dp_delta: float = 1e-5
    target_modules: list = None
    load_in_4bit: bool = True

    def __post_init__(self):
        if self.target_modules is None:
            self.target_modules = ["q_proj", "v_proj", "k_proj", "o_proj"]
