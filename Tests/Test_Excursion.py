import sys
from operator import contains

from src.main import Item, Inventory, Excursion

sys.path.insert(0, '..')
from __main__ import *

def test_get_members():
    ex = Excursion()
    assert ex.get_members() == ex.member_list

def test_add_member():
    ex = Excursion()
    test_name = "håkan"
    ex.add_member(test_name)
    assert ex.member_list.__contains__(test_name)

def test_remove_member():
    ex = Excursion()
    test_name = "håkan"
    ex.add_member(test_name)
    ex.remove_member(test_name)
    assert not ex.member_list.__contains__(test_name)

def test_register_item_rented():
    inv = Inventory()
    stav = Item("Gå stavar", 50, 10)
    inv.set_item(stav)

    ex = Excursion()
    test_name = "håkan"
    ex.add_member(test_name)
    ex.rent_item(test_name, stav)

    assert ex.rent_dictionary[test_name] == stav.name