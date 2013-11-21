#   This file is part of PyBuilder
#
#   Copyright 2011-2013 PyBuilder Team
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pybuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")

use_plugin("copy_resources")
use_plugin("filter_resources")
use_plugin("source_distribution")

use_plugin("python.coverage")
use_plugin("python.unittest")
use_plugin("python.integrationtest")
use_plugin("python.flake8")

use_plugin("python.pydev")


summary = "An extensible, easy to use continuous build tool for Python"
description = """PyBuilder is a continuous build tool for multiple languages.

PyBuilder primarily targets Python projects but due to its extensible
nature it can be used for other languages as well.

PyBuilder features a powerful yet easy to use plugin mechanism which
allows programmers to extend the tool in an unlimited way.
"""

authors = [Author("Alexander Metzner", "alexander.metzner@gmail.com"),
           Author("Maximilien Riehl", "max@riehl.io"),
           Author("Michael Gruber", "aelgru@gmail.com"),
           Author("Udo Juettner", "udo.juettner@gmail.com")]
url = "http://pybuilder.github.com"
license = "Apache License"
version = "0.9.15"

default_task = ["analyze", "publish"]


@init
def initialize(project):
    project.build_depends_on("mockito")
    project.build_depends_on("pyassert")
    project.build_depends_on("wheel")

    # Need to define that manually, because the pyfix plugin is not used
    # directly.
    project.build_depends_on("pyfix")

    project.set_property("integrationtest_parallel", True)

    project.set_property("coverage_break_build", False)
    project.get_property("coverage_exceptions").append("pybuilder.cli")
    project.get_property("coverage_exceptions").append("pybuilder.plugins.core_plugin")

    project.set_property("copy_resources_target", "$dir_dist")
    project.get_property("copy_resources_glob").append("LICENSE")

    project.get_property("filter_resources_glob").append("**/pybuilder/__init__.py")

    project.set_property("flake8_verbose_output", True)
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_ignore", "E501,W293")
    project.set_property('flake8_include_test_sources', True)

    project.get_property("source_dist_ignore_patterns").append(".project")
    project.get_property("source_dist_ignore_patterns").append(".pydevproject")
    project.get_property("source_dist_ignore_patterns").append(".settings")

    project.get_property("distutils_commands").append("bdist_wheel")
    project.set_property("distutils_classifiers", [
                         'Programming Language :: Python',
                         'Programming Language :: Python :: Implementation :: CPython',
                         'Programming Language :: Python :: Implementation :: PyPy',
                         'Programming Language :: Python :: 2.6',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.2',
                         'Programming Language :: Python :: 3.3',
                         'Development Status :: 3 - Alpha',
                         'Environment :: Console',
                         'Intended Audience :: Developers',
                         'License :: OSI Approved :: Apache Software License',
                         'Topic :: Software Development :: Build Tools',
                         'Topic :: Software Development :: Quality Assurance',
                         'Topic :: Software Development :: Testing'])
