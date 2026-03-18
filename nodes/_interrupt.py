from __future__ import annotations


def throw_if_interrupted() -> None:
    """Best-effort interrupt check that degrades to no-op off-host."""
    try:
        import comfy.model_management as model_management
    except Exception:
        return

    check = getattr(model_management, "throw_exception_if_processing_interrupted", None)
    if callable(check):
        check()
