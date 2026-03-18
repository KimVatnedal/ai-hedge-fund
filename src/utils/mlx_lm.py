"""
mlx_lm.py — MLX LM stub for non-Apple-Silicon platforms.

MLX local inference is only available on Apple Silicon (macOS).
On Linux this module is imported for API compatibility only.
"""


def ensure_mlx_and_model(model_name: str) -> bool:
    """Stub: MLX LM not available on this platform."""
    raise RuntimeError(
        "MLX LM inference is only supported on Apple Silicon (macOS). "
        "Use --model with a cloud provider instead."
    )
