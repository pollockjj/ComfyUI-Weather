from __future__ import annotations

import os
from pathlib import Path

import folder_paths


_WEATHER_ROOT = Path(__file__).resolve().parent


def get_weather_root() -> Path:
    return _WEATHER_ROOT


def get_assets_dir() -> Path:
    return _WEATHER_ROOT / "assets"


def get_input_dir() -> Path:
    return Path(folder_paths.get_input_directory()).resolve()


def get_model_cache_dir() -> Path:
    override = os.environ.get("WEATHER_MODEL_CACHE", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return Path(folder_paths.models_dir).resolve() / "weather"


def get_huggingface_cache_dir() -> Path:
    override = os.environ.get("HF_HOME", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return get_model_cache_dir() / "huggingface"

