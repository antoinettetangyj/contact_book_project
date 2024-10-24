#-*- coding: utf-8 -*-
#contact_book/main.py

"""This module provides Contacts application."""

import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():

    """Contacts main function."""

    #create application
    app = QApplication(sys.argv)

    #connect to database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)

    #create main window
    win = Window()
    win.show()

    #run event loop
    sys.exit(app.exec())