# This Python file uses the following encoding: utf-8
import os
from pathlib import Path

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import numpy as np


from PySide2 import QtWidgets
import sys

# Local Module Imports
import app_framework as af

# Create GUI application
app = QtWidgets.QApplication(sys.argv)
form = af.MyApp()
form.show()
app.exec_()



