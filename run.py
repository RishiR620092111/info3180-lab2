#! /usr/bin/env python
import os
from flask import render_template
from flask import Flask
from app import app
import time
from app import app
app.run(debug=True,host="0.0.0.0",port=8080)