"""Enkel miljö-/installationskontroll för kurslabben.

Syfte:
- Säkerställa att Python och viktiga paket (PyTorch, scikit-learn, pandas) är installerade.
- Visa versionsnummer.
- Kontrollera om CUDA/GPU finns tillgängligt och göra ett litet tensor-test.
"""

import sys

import pandas as pd
import sklearn
import torch

def main():
    print("=== Environment Check ===")
    # Grundinfo: Python-version och paketversioner.
    print(f"Python: {sys.version}")
    print(f"PyTorch: {torch.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print(f"pandas: {pd.__version__}")

    # GPU-check: om CUDA finns väljer vi GPU, annars CPU.
    if torch.cuda.is_available():
        print("GPU: YES")
        print("GPU name:", torch.cuda.get_device_name(0))
        device = "cuda"
    else:
        print("GPU: NO")
        device = "cpu"

    # Snabbt sanity-test: skapa en tensor på vald device och gör en enkel beräkning.
    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = x * 2
    print("Tensor test:", y)

    print("=== OK ===")

if __name__ == "__main__":
    # Kör endast när filen körs direkt (inte när den importeras).
    main()
