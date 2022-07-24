# -*- coding: utf-8 -*-
"""
@file
@brief Implements command line ``python -m ensae_teaching_cs <command> <args>``.
"""
import sys
from pyquickhelper.cli import cli_main_helper


def main(args, fLOG=print):
    """
    Implements ``python -m ensae_teaching_cs <command> <args>``.

    @param      args        command line arguments
    @param      fLOG        logging function
    """
    try:
        from .cli import inspect_source_code
    except ImportError:
        from ensae_teaching_cs.cli import inspect_source_code

    fcts = dict(inspect_source_code=inspect_source_code)
    cli_main_helper(fcts, args=args, fLOG=fLOG)


if __name__ == "__main__":
    main(sys.argv[1:])
