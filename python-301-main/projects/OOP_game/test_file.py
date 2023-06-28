import pytest
import OOP_game_project


def test_input():
    OOP_game_project.text
    assert type(OOP_game_project.text)== str

def test_oponent_angelus():
    assert OOP_game_project.angelus[0]=="The librarian"
    assert OOP_game_project.angelus[1]=="baseball bat"
    assert OOP_game_project.angelus[2]==80