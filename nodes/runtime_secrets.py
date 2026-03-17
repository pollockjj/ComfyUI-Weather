from __future__ import annotations

import os


_RUNTIME_KEYS: dict[str, str | None] = {
    "open_meteo": None,
    "jua": None,
}


def set_open_meteo_key(value: str | None) -> None:
    normalized = (value or "").strip()
    _RUNTIME_KEYS["open_meteo"] = normalized or None


def set_jua_key(value: str | None) -> None:
    normalized = (value or "").strip()
    _RUNTIME_KEYS["jua"] = normalized or None


def get_open_meteo_key() -> str | None:
    runtime_value = _RUNTIME_KEYS.get("open_meteo")
    if runtime_value:
        return runtime_value
    env_value = os.environ.get("OPEN_METEO_API_KEY", "").strip()
    return env_value or None


def get_jua_key() -> str | None:
    runtime_value = _RUNTIME_KEYS.get("jua")
    if runtime_value:
        return runtime_value
    env_value = os.environ.get("JUA_API_KEY", "").strip()
    return env_value or None


def resolve_jua_key(api_key_input: str | None) -> str:
    key = (api_key_input or "").strip() or (get_jua_key() or "")
    if not key or ":" not in key:
        raise ValueError(
            "API key must be in format 'key_id:key_secret'. Get one at https://developer.jua.ai/"
        )
    return key

