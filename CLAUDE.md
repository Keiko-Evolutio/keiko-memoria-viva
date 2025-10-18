# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Keiko Memoria Viva** is a research project implementing biologically-inspired memory systems for multi-agent architectures. The project translates neurobiological principles into software structures, focusing on adaptive, efficient, and scalable memory capabilities for artificial agents.

## High-Level Architecture

### Core Memory Modules

The project implements three interconnected biological memory concepts:

1. **Selective Memory Filtering** (`selective_memory_filtering/`)
   - Filters relevant vs. irrelevant information based on context
   - Implements consolidation mechanisms to prevent impulsive storage
   - Uses priority assignment for urgent vs. routine information

2. **Plastic Memory** (`plastic_memory/`)
   - Implements synaptic plasticity (LTP/LTD) for adaptive memory weights
   - Dynamically adjusts feature importance based on experience
   - Provides interactive explainability for decision-making

3. **Adaptive Forgetting** (`adaptive_forgetting/`)
   - Models memory decay using Ebbinghaus forgetting curves
   - Implements spacing effects and interference handling
   - Provides homeostatic scaling for resource optimization

4. **Banking Agent Example** (`banking_agent_detailed_example/`)
   - Integrates all three memory concepts in a multi-agent banking system
   - Demonstrates practical application with customer interaction scenarios
   - Shows adaptive learning from feedback with automatic archival

### Key Design Patterns

- **Notebook-First Development**: Primary implementation in Jupyter notebooks (`.ipynb` files)
- **Shared Styling**: Central `notebook_style.py` provides consistent visualization across modules
- **Biological Inspiration**: Each module maps specific neuroscience concepts to software implementations
- **Interactive Visualizations**: Heavy use of ipywidgets for parameter exploration

## Common Development Commands

### Environment Setup
```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (using uv package manager)
uv sync
```

### Working with Notebooks
```bash
# Start JupyterLab (preferred)
jupyter lab

# Or classic Jupyter Notebook
jupyter notebook
```

### Code Quality
```bash
# Auto-fix and format code
make lint

# Check without modifications
make check

# Individual operations
make fix      # Run Ruff auto-fixes
make format   # Format code with Ruff
```

### Running Individual Notebooks
```bash
# Each module has its main implementation notebook
jupyter notebook adaptive_forgetting/adaptive_forgetting.ipynb
jupyter notebook plastic_memory/plastic_memory.ipynb
jupyter notebook selective_memory_filtering/selective_memory_filtering.ipynb
jupyter notebook banking_agent_detailed_example/banking_agent_detailed_example.ipynb
```

## Project Structure

```
keiko-memoria-viva/
├── adaptive_forgetting/           # Adaptive forgetting mechanisms
│   ├── adaptive_forgetting.ipynb  # Main implementation
│   └── work-in-progress.ipynb     # Development work
├── plastic_memory/                # Synaptic plasticity implementation
│   └── plastic_memory.ipynb       # Core LTP/LTD mechanisms
├── selective_memory_filtering/    # Context-based filtering
│   └── selective_memory_filtering.ipynb  # Insurance case study
├── banking_agent_detailed_example/  # Integrated use case
│   ├── banking_agent_detailed_example.ipynb  # Main example
│   └── work-in-progress.ipynb     # Detailed implementation
├── notebook_style.py               # Shared visualization configuration
├── pyproject.toml                  # Project configuration
└── Makefile                        # Development commands
```

## Key Technical Details

### Python Requirements
- Python 3.10+ (supports 3.10, 3.11, 3.12, 3.13)
- Virtual environment in `.venv/`

### Core Dependencies
- Scientific stack: numpy, pandas, matplotlib, plotly, seaborn
- Jupyter ecosystem: notebook, jupyterlab, ipywidgets
- Package management: uv (modern Python package manager)

### Code Style
- Line length: 88 characters (Black-compatible)
- Linting: Ruff with rules E, W, F, I, B, C4, UP
- Type checking: mypy with strict configuration
- Pre-commit hooks for automatic formatting

### Important Constants
- `SEED = 42` used throughout for reproducibility
- Consistent color palette defined in `notebook_style.py`
- WCAG-compliant visualization colors

## Working with the Codebase

### When Modifying Notebooks
1. Import shared styling: `from notebook_style import setup_plot_style`
2. Use consistent seed for reproducibility: `np.random.seed(42)`
3. Follow existing widget patterns for interactive elements
4. Document biological concepts alongside implementations

### When Adding New Modules
1. Create a dedicated directory under root
2. Include a main implementation notebook
3. Use `work-in-progress.ipynb` for experimental code
4. Import and use `notebook_style.py` for visualizations

### Testing Approach
- The project uses interactive notebooks for demonstration
- Each notebook contains example usage and visualizations
- Focus on parameter exploration through widgets rather than unit tests

## Important Notes

- **Language**: Documentation primarily in German, code comments in English
- **Research Focus**: This is a research project, not production software
- **Notebook Execution**: Notebooks may have long-running cells with interactive widgets
- **MCP Integration**: Project includes `.mcp.json` for Model Context Protocol servers
- **License**: CC BY-NC 4.0 (Attribution-NonCommercial)

## Key Biological Concepts to Understand

When working with this codebase, familiarity with these concepts helps:

1. **Ebbinghaus Forgetting Curves**: Mathematical models of memory decay over time
2. **LTP/LTD (Long-Term Potentiation/Depression)**: Synaptic strength modifications
3. **Spacing Effect**: Improved retention through distributed practice
4. **Homeostatic Plasticity**: Maintaining stability while allowing change
5. **Memory Consolidation**: Transfer from short-term to long-term storage
6. **Interference Theory**: How new information affects existing memories

## Current Development Focus

Based on recent commits, the project is actively developing:
- Interactive visualizations for memory dynamics
- Expanding the MemoryTrace class with neurobiological properties
- Refining the banking agent use case
- Improving notebook documentation and usability