import pytest
import reduced_game
from tud_test_base import set_keyboard_input,get_display_output
from class_ import Hero, Oponent,Wolves,Final_Oponent
import class_


def test_first_Hero():
    assert reduced_game.player.name=="xabi"
    assert reduced_game.player.main_strength=="sword"
    assert reduced_game.player.hp==10000

def test_Oponent_1():
    assert reduced_game.angelus.name=="The librarian"
    assert reduced_game.angelus.main_strength=="baseball bat"
    assert reduced_game.angelus.hp==80

def test_Oponent_2():
    assert reduced_game.bisontus.name=="The Bison"
    assert reduced_game.bisontus.main_strength=="Hands"
    assert reduced_game.bisontus.hp==90

def test_Oponent_3():
    assert reduced_game.ear_plucker.name=="Ear chopper"
    assert reduced_game.ear_plucker.main_strength=="bowie knife"
    assert reduced_game.ear_plucker.hp==95

def test_Oponent_4():
    assert reduced_game.the_driller.name=="Mr driller"
    assert reduced_game.the_driller.main_strength=="drill"
    assert reduced_game.the_driller.hp==100

def test_final_wolves():
    assert reduced_game.Wolves_oponent.name=="Herd of wolves"
    assert reduced_game.Wolves_oponent.main_strength=="sharp teeth"
    assert reduced_game.Wolves_oponent.hp==30
    assert reduced_game.Wolves_oponent.run==10

def test_final_johny():
    assert reduced_game.Final_oponent.name=="sharpy Johnny"
    assert reduced_game.Final_oponent.main_strength=="chainsaw"
    assert reduced_game.Final_oponent.hp==100
    assert reduced_game.Final_oponent.extra_hp==10

def test_feed():
    reduced_game.player.feed()
    assert reduced_game.player.hp==10020

def test_poison():
    reduced_game.player.poison()
    assert reduced_game.player.hp==(10020-30)

def test_battle():
    Hero.battle(reduced_game.player,reduced_game.angelus)
    assert (reduced_game.player.hp==(10020-30) and reduced_game.angelus.hp==40) or (reduced_game.player.hp==(10020-40) and reduced_game.angelus.hp==80) or (reduced_game.player.hp==(10020-40) and reduced_game.angelus.hp==70)


def test_battle_super_attack():
    reduced_game.player.hp=100
    reduced_game.player.battle_super_attack(reduced_game.Final_oponent)
    assert (reduced_game.player.hp==100 and reduced_game.Final_oponent.hp==60) or (reduced_game.player.hp==50 and reduced_game.Final_oponent.hp==100) or (reduced_game.player.hp==80 and reduced_game.Final_oponent.hp==90)

def test_battle_run():
    reduced_game.player.hp=100
    reduced_game.player.battle_run_wolves(reduced_game.Wolves_oponent)
    assert (reduced_game.player.hp==100 and reduced_game.Wolves_oponent.hp==0) or (reduced_game.player.hp==70 and reduced_game.Wolves_oponent.hp==30) or (reduced_game.player.hp==90 and reduced_game.Wolves_oponent.hp==20)

def test_alive_check():
    reduced_game.angelus.hp=0
    assert reduced_game.angelus.alive_check()==False
    reduced_game.angelus.hp=10
    assert reduced_game.angelus.alive_check()==True

def test_Final_attack():
    reduced_game.Final_oponent.hp=200
    assert (reduced_game.Final_oponent.attack()==True and reduced_game.Final_oponent.hp>115) 
    reduced_game.Final_oponent.hp=10
    assert (reduced_game.Final_oponent.attack()==False and reduced_game.Final_oponent.hp<115)

