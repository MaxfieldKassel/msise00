#!/usr/bin/env python
import site
import setuptools
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

# PEP517 workaround
site.ENABLE_USER_SITE = True

class bdist_wheel(_bdist_wheel):
    """Mark wheel as non-pure (so it gets a linux_x86_64, macosx, etc. tag)."""
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

setuptools.setup(
    # pull metadata from setup.cfg
    setup_requires=["wheel"],
    cmdclass={"bdist_wheel": bdist_wheel},
)