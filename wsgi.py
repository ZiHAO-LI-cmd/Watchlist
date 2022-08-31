# -*- coding:utf-8 -*-
"""
author: Zihao Li
date: 2022-09-01
"""
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

