import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from visualization import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-radio")
    assert radio_items is not None
