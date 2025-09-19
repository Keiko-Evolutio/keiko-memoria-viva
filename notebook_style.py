
"""Shared plotting style utilities for Jupyter notebooks in the project."""

from __future__ import annotations

import os
from pathlib import Path

import random
from typing import Any, Dict, Iterable, Mapping, Sequence, Final

# Ensure Matplotlib can write configuration/cache files in restricted environments
_MPL_CONFIG_DIR = Path(__file__).resolve().parent / ".matplotlib_cache"
_MPL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ["MPLCONFIGDIR"] = str(_MPL_CONFIG_DIR)

_FONTCONFIG_CACHE_DIR = _MPL_CONFIG_DIR / "fontconfig-cache"
_FONTCONFIG_CACHE_DIR.mkdir(parents=True, exist_ok=True)
if not os.environ.get("FC_CACHEDIR"):
    os.environ["FC_CACHEDIR"] = str(_FONTCONFIG_CACHE_DIR)

_XDG_CACHE_DIR = _MPL_CONFIG_DIR / "xdg-cache"
_XDG_CACHE_DIR.mkdir(parents=True, exist_ok=True)
if not os.environ.get("XDG_CACHE_HOME"):
    os.environ["XDG_CACHE_HOME"] = str(_XDG_CACHE_DIR)

_home = Path(os.environ.get("HOME", str(Path.home())))
if not _home.exists() or not os.access(_home, os.W_OK | os.X_OK):
    os.environ["HOME"] = str(_MPL_CONFIG_DIR)


import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler


__all__ = [
    "SEED",
    "rng",
    "DEFAULT_BASE_COLORS",
    "DEFAULT_COLOR_ALIASES",
    "COLOR_CYCLE_KEYS",
    "resolve_palette",
    "setup_plot_style",
    "PLOT_COLORS",
]

# -------------------------------------------------------------------------
# Reproducibility
# -------------------------------------------------------------------------
SEED: Final[int] = 42
random.seed(SEED)
rng: np.random.Generator = np.random.default_rng(SEED)

# -------------------------------------------------------------------------
# Color definitions
# -------------------------------------------------------------------------
DEFAULT_BASE_COLORS: Dict[str, str] = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "tertiary": "#2ca02c",
    "quaternary": "#d62728",
    "accent": "#17becf",
    "neutral": "#7f7f7f",
    "support": "#9467bd",
    "muted": "#8c564b",
}

# Aliases provide semantic or domain-specific labels that point to base colors.
# They can reference either base colors or other aliases (which are resolved recursively).
DEFAULT_COLOR_ALIASES: Dict[str, str] = {
    # Generic semantic labels
    "baseline": "neutral",
    "threshold": "tertiary",
    "highlight": "quaternary",
    "positive": "primary",
    "negative": "quaternary",
    "warning": "secondary",
    "info": "accent",
    "supporting": "support",
    # Backwards compatibility with existing notebooks
    "speicherquote": "primary",
    "schwellenwert": "threshold",
    "biologisch": "quaternary",
    "gespeichert": "primary",
    "ausgefiltert": "secondary",
    "thalamus": "primary",
    "amygdala": "secondary",
    "pfc": "tertiary",
    "adaptiv": "accent",
    "delta": "secondary",
}

COLOR_CYCLE_KEYS: Sequence[str] = (
    "primary",
    "secondary",
    "tertiary",
    "quaternary",
    "accent",
    "support",
)

_DEFAULT_RC_PARAMS: Dict[str, Any] = {
    "figure.figsize": (8, 5),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "font.size": 11,
}


def _resolve_alias(
    key: str,
    base_colors: Mapping[str, str],
    alias_map: Mapping[str, str],
    _seen: Iterable[str] | None = None,
) -> str:
    """Resolve an alias to an actual color hex code."""
    if key in base_colors:
        return base_colors[key]

    seen = set(_seen or ())
    if key in seen:
        raise ValueError(f"Cyclic color alias definition detected: {' -> '.join(seen)} -> {key}")
    seen.add(key)

    target = alias_map.get(key)
    if target is None:
        raise KeyError(f"Unknown color identifier: {key}")
    return _resolve_alias(target, base_colors, alias_map, seen)


def resolve_palette(
    *,
    base_colors: Mapping[str, str] | None = None,
    aliases: Mapping[str, str] | None = None,
) -> Dict[str, str]:
    """Build a resolved palette dictionary from base colors and aliases."""
    merged_colors: Dict[str, str] = {**DEFAULT_BASE_COLORS}
    if base_colors:
        merged_colors.update(base_colors)

    merged_aliases: Dict[str, str] = {**DEFAULT_COLOR_ALIASES}
    if aliases:
        merged_aliases.update(aliases)

    palette: Dict[str, str] = {}

    # First, include base colors explicitly
    for name, hex_code in merged_colors.items():
        palette[name] = hex_code

    # Then resolve aliases (allowing alias -> alias chains)
    for alias, target in merged_aliases.items():
        palette[alias] = _resolve_alias(target, merged_colors, merged_aliases)

    return palette


def _build_color_cycle(palette: Mapping[str, str], cycle_keys: Sequence[str]) -> Sequence[str]:
    colors = [palette[key] for key in cycle_keys if key in palette]
    if not colors:
        colors = list(dict.fromkeys(palette.values()))
    return colors


def setup_plot_style(
    *,
    base_colors: Mapping[str, str] | None = None,
    aliases: Mapping[str, str] | None = None,
    cycle_keys: Sequence[str] | None = None,
    rc_params: Mapping[str, Any] | None = None,
    update_global_palette: bool = True,
) -> Dict[str, str]:
    """Configure Matplotlib/Seaborn style and return the resolved palette."""
    palette = resolve_palette(base_colors=base_colors, aliases=aliases)

    # Apply optional seaborn style (falls back silently)
    try:
        plt.style.use("seaborn-v0_8-whitegrid")
    except Exception:
        pass

    rc_update: Dict[str, Any] = {**_DEFAULT_RC_PARAMS}
    if rc_params:
        rc_update.update(rc_params)

    cycle = _build_color_cycle(palette, cycle_keys or COLOR_CYCLE_KEYS)
    rc_update["axes.prop_cycle"] = cycler(color=list(cycle))

    plt.rcParams.update(rc_update)

    # Re-seed global RNGs so that figures remain reproducible
    random.seed(SEED)
    np.random.seed(SEED)

    if update_global_palette:
        global PLOT_COLORS
        PLOT_COLORS = dict(palette)

    return palette


# Apply default style immediately on import for convenience.
PLOT_COLORS: Dict[str, str] = resolve_palette()
setup_plot_style(update_global_palette=True)
