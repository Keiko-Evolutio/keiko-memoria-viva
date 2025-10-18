"""Zentrales Styling-Modul für alle Jupyter-Notebooks des Projekts."""

from __future__ import annotations

import random
from collections.abc import Iterable

import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

# Globale Zufallsquellen
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
rng = np.random.default_rng(SEED)

# Standardfarbpalette (WCAG-konform)
_DEFAULT_BASE_COLORS: dict[str, str] = {
    "primary": "#1f77b4",  # Blau
    "secondary": "#ff7f0e",  # Orange
    "tertiary": "#2ca02c",  # Grün
    "quaternary": "#d62728",  # Rot
    "accent": "#9467bd",  # Violett
    "neutral": "#7f7f7f",  # Grau
    "support": "#17becf",  # Cyan
}

# Vordefinierte semantische Aliasse
_DEFAULT_ALIASES: dict[str, str] = {
    # General semantics
    "baseline": "neutral",
    "threshold": "quaternary",
    "positive": "tertiary",
    "negative": "quaternary",
    "retention": "primary",
    "decay": "secondary",
    "interference": "tertiary",
    # Notebook-specific semantics frequently used across plots
    # Map to base palette keys (not other aliases)
    "ltp": "tertiary",  # green
    "ltd": "quaternary",  # red
    "fraud": "secondary",  # orange (risk/suspicion)
    "fraud_risk": "secondary",  # synonym for convenience
    "synaptic_strength": "primary",  # blue
}

# Matplotlib-Grundkonfiguration
_DEFAULT_RC_PARAMS = {
    "figure.dpi": 100,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "legend.frameon": False,
}


def setup_plot_style(
    *,
    base_colors: dict[str, str] | None = None,
    aliases: dict[str, str] | None = None,
    cycle_keys: Iterable[str] | None = None,
    rc_params: dict[str, object] | None = None,
) -> dict[str, str]:
    """Initialisiert das Plot-Styling und gibt das Farbregister zurück.

    Args:
        base_colors: Optionale Überschreibung der Basisfarben.
        aliases: Zusätzliche semantische Aliasse.
        cycle_keys: Reihenfolge der Farben für den Matplotlib-Color-Cycle.
        rc_params: Zusätzliche Matplotlib-Parameter.

    Returns:
        Dictionary mit direkten und semantischen Farbnamen.
    """
    palette = {**_DEFAULT_BASE_COLORS}
    if base_colors:
        palette.update(base_colors)

    alias_map = {**_DEFAULT_ALIASES}
    if aliases:
        alias_map.update(aliases)

    # RC-Parameter anwenden
    plt.rcParams.update(_DEFAULT_RC_PARAMS)
    if rc_params:
        plt.rcParams.update(rc_params)

    # Farb-Zyklus konfigurieren
    cycle_sequence = list(cycle_keys or ("primary", "accent", "tertiary", "secondary"))
    valid_cycle = [palette[key] for key in cycle_sequence if key in palette]
    if valid_cycle:
        plt.rcParams["axes.prop_cycle"] = cycler(color=valid_cycle)

    # Farbregister inklusive Aliasse aufbauen
    resolved_colors = {**palette}
    for alias, base_key in alias_map.items():
        if base_key not in palette:
            raise KeyError(
                f"Alias '{alias}' referenziert unbekannte Basisfarbe '{base_key}'."
            )
        resolved_colors[alias] = palette[base_key]

    return resolved_colors


__all__ = ["setup_plot_style", "SEED", "rng"]
