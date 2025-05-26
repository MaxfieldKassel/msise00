#!/usr/bin/env python
import setuptools
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        # mark platform‑specific
        self.root_is_pure = False
        # use the py3 ABI tag so it works on any Python 3.x
        self.python_tag = "py3"

setuptools.setup(
    setup_requires=["wheel"],
    cmdclass={"bdist_wheel": bdist_wheel},
)