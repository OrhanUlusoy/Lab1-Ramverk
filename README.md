# Lab1-Ramverk

## Installation
uv sync

## Kör miljöcheck
uv run check_env.py

## Notis om PyTorch (CPU vs GPU/CUDA)
Det här projektet använder `torch` via `uv` och låser beroenden i `uv.lock`.

- Om du inte har en CUDA-kompatibel GPU, är CPU-varianten helt OK (då blir `GPU: NO`).
- Om du har NVIDIA-GPU och vill att `GPU: YES` ska fungera, behöver du installera en CUDA-variant av PyTorch (ofta via PyTorchs egna paketindex) och därefter uppdatera `uv.lock`.
