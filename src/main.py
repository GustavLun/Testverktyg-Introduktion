
#Item class
class Item:
    def __init__(self, item_name, price, amount):
        self.name = item_name
        self.price = price
        self.amount = amount


#Inventory
class Inventory:
    def __init__(self):
        self.InventoryItems = []

    def set_item (self, Item):
        self.InventoryItems.append(Item)



    def rent(self,item_name):
        for each in self.InventoryItems:

            if each.name == item_name:
                if each.amount > 0:
                    each.amount -= 1

                    return True

        return False


    def get_amount_left(self, item_name):
        for each in self.InventoryItems:

            if each.name == item_name:
                return each.amount


#Excursion

class Excursion:
    def __init__(self):
        self.member_list = []
        self.rent_dictionary = {"item": "renter"}

    def get_members(self):
        return self.member_list


    def add_member(self, member_name):
        self.member_list.append(member_name)
        if member_name in self.member_list:
            return True
        else:
            return False

    def remove_member(self, member_name):
        self.member_list.remove(member_name)
        if member_name in self.member_list:
            if member_name in self.member_list:
                return True
            else:
                return False


    def rent_item(self, item_name, member_name):
        self.rent_dictionary[member_name] = item_name
        return self.rent_dictionary[member_name]



