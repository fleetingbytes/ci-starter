from importlib.metadata import version as get_version

from .lib import (
    generate_base_workflow,
    generate_helper_script,
    generate_reusable_workflow,
    generate_semantic_release_config,
    update_actions,
)

__all__ = (
    "generate_base_workflow",
    "generate_helper_script",
    "generate_reusable_workflow",
    "generate_semantic_release_config",
    "update_actions",
)

__version__ = get_version(__package__)
