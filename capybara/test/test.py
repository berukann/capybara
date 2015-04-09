#!/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))

import capybara

c = capybara.Capybara(config_dir='./capybara/test/config/', tokens_dir='./capybara/test/tokens/')

