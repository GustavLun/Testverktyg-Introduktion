import sys

from src.main import Item, Inventory

sys.path.insert(0, '..')
from __main__ import *


def test_add_item_inventory():
    Inv = Inventory()
    value = False
    stav = Item("Gå stavar", 50, 10)
    Inv.set_item(stav)
    if stav in Inv.InventoryItems:
        value = True
    assert value == True


def test_remove_item_inventory():
    Inv = Inventory()
    stav = Item("Gå stavar", 50, 10)
    value = stav.amount - 1
    Inv.set_item(stav)
    Inv.rent("Gå stavar")
    assert stav.amount == value


def test_display_inventory():
     Inv = Inventory()
     stav = Item("Gå stavar", 50, 10)
     Inv.set_item(stav)
     assert Inv.get_amount_left("Gå stavar") == stav.amount