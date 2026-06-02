"""
Configuration settings for the hiring agent application.

This module contains global configuration flags that control application behavior,
including development mode settings that enable caching and CSV export functionality.

Attributes:
    DEVELOPMENT_MODE (bool): When True, enables:
        - Local caching of PDF extractions (cache/)
        - Local caching of GitHub API responses
        - CSV export of evaluation results (resume_evaluations.csv)
"""

# Global development mode flag - controls caching and CSV export
DEVELOPMENT_MODE = True
