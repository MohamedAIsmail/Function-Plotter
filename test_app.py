import pytest
from PySide2 import QtCore


import app_framework

@pytest.fixture
def app(qtbot):
    test_app = app_framework.MyApp()
    qtbot.addWidget(test_app)
    return test_app

# First test case is correct input function & correct min and max values
def test_evaluation1(app, qtbot):
    qtbot.keyClicks(app.inputFunction, 'x^2')
    qtbot.keyClicks(app.minX, '-2')
    qtbot.keyClicks(app.maxX, '2')

    assert app.validation_msg.text() == 'Correct equation & values'

# Second test case is correct input function but without min and max values
def test_evaluation2(app, qtbot):
    qtbot.keyClicks(app.inputFunction, 'x^2')

    assert app.validation_msg.text() == 'Correct equation but you need to enter the min and max values of X'

# Third test case is wrong input function but with correct min and max values
def test_evaluation3(app, qtbot):
    qtbot.keyClicks(app.inputFunction, 'x2')
    qtbot.keyClicks(app.minX, '-2')
    qtbot.keyClicks(app.maxX, '2')

    assert app.validation_msg.text() == 'Correct values but you need to enter a correct equation'


# Fourth test case is correct input function but with wrong min and max values
def test_evaluation4(app, qtbot):
    qtbot.keyClicks(app.inputFunction, 'x^2')
    qtbot.keyClicks(app.minX, '2')
    qtbot.keyClicks(app.maxX, '-2')
    
    assert app.validation_msg.text() == 'Max X value must be greater than Min X value'
