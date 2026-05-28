from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

class PayloadEncryptor:
    def __init__(self):
        # In production: load from environment variable or secure vault
        self.key = os.urandom(32)  # 256-bit key
        print(f"[ENCRYPTION] AES-GCM key generated (keep this secret!)")

    def encrypt(self, data: bytes) -> str:
        """Encrypt bytes and return Base64 string"""
        aesgcm = AESGCM(self.key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, None)
        combined = nonce + ciphertext
        return base64.b64encode(combined).decode('utf-8')

    def decrypt(self, encrypted_b64: str) -> bytes:
        """Decrypt Base64 string back to bytes"""
        aesgcm = AESGCM(self.key)
        combined = base64.b64decode(encrypted_b64)
        nonce = combined[:12]
        ciphertext = combined[12:]
        return aesgcm.decrypt(nonce, ciphertext, None)
