'''
Created on Jul 23, 2011

@author: mathos
'''
import sys

from util import *

import sphinx
from sphinx.config import Config
from sphinx.errors import ExtensionError, ConfigError, VersionRequirementError


@with_app(buildername='html')
def test_core_config(app):
	cfg = app.config
	app.builder.build_all()
