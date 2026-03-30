# Project Charter: Modular MLOps Framework MVP

## 1. Project Vision
We are building a production-grade, modular Machine Learning framework designed for rapid, reproducible experimentation (ideal for Kaggle competitions or ML research). We are transitioning away from monolithic Jupyter Notebooks toward a software engineering "Lasagna Architecture" (strict separation of concerns) to build a scalable, plug-and-play MLOps system.

## 2. Core Architectural Principles
- **No Notebooks for Core Logic:** Jupyter Notebooks are strictly for Exploratory Data Analysis (EDA). All feature engineering, modeling, and validation logic must live in Python packages.
- **Configuration-Driven:** Hardcoding is forbidden. All experiment parameters, file paths, and feature selections must be defined in external YAML config files.
- **Object-Oriented Design (OOP):** We rely heavily on Abstract Base Classes (ABCs) to enforce standard contracts (e.g., `.fit()` and `.transform()`) for all models and features.
- **Total Reproducibility:** Every experiment must be executable via a single command line instruction (e.g., `python run_experiment.py --config configs/exp.yaml`). A **global random seed** must be set at the very beginning of the orchestrator script to ensure deterministic behavior across all libraries (NumPy, Pandas, Scikit-Learn, PyTorch, etc.).
- **Experiment & Artifact Tracking:** Flat files are insufficient for long-term tracking. Logs, metrics, and models must be integrated with an experiment tracker (e.g., MLflow or Weights & Biases) to visually compare YAML configs against validation metrics.
- **Data Versioning:** Input datasets must be immutable. Data should be tracked using Data Version Control (DVC) or strict timestamping/versioning conventions in file names to guarantee reproducible runs even if underlying data changes.

## 3. Directory Structure
The project must strictly adhere to this layout:

project_root/
├── data/                   # Raw and processed datasets (ignored in git; versioned via DVC)
├── configs/                # YAML configuration files
├── outputs/                # Local generated models, logs, and OOF predictions (backed by tracker)
├── src/                    # Core framework package
│   ├── __init__.py
│   ├── base.py             # Abstract Base Classes (BaseModel, BaseFeature)
│   ├── features/           # Feature engineering classes
│   ├── models/             # Model wrapper classes & Factory
│   ├── validation/         # Cross-validation strategies
│   └── utils/              # Low-level helpers (Logger, I/O, Tracking config)
├── tests/                  # Unit tests for core logic and custom features (pytest)
├── .pre-commit-config.yaml # Pre-commit hooks for linting and formatting
├── pyproject.toml          # Dependency management and tool configurations
└── run_experiment.py       # The main orchestrator script

## 4. Coding Standards (Instructions for AI)
When generating code for this project, the AI MUST obey the following rules:
1. **Type Hinting & Checking:** Use Python type hints (`: str`, `-> pd.DataFrame`) for all function arguments and return types. Code must pass `mypy` strict checks.
2. **Docstrings:** Include clear, concise docstrings for all classes and methods.
3. **Automated Formatting:** Code must conform to standard formatting tools (e.g., `Ruff`, `Black`, `Flake8`). This is enforced via pre-commit hooks.
4. **No `print()` Statements:** Use the custom `utils/Logger` module for all terminal outputs and experiment tracker logging.
5. **Modularity:** Do not write 500-line files. If a file gets too complex, break it down.
6. **Pandas Performance:** Always prioritize memory-efficient Pandas operations (e.g., vectorization over iterating through rows).