# MAKING THE MENUS
class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  
  def __repr__(self):
    return self.name + " menu available from " +str(self.start_time) +" to " +str(self.end_time)
  
  def calculate_bill(self,purchased_items):
    total_cost=0
    for item in purchased_items:
      for key in self.items.keys():
        if item==key:
          total_cost+=self.items[key]
    return total_cost

#BRUNCH
brunch_menu={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
#print(brunch_items)

brunch=Menu('Brunch',brunch_menu,11,16)
#print(brunch.items)
#EARLY BIRD
early_bird_menu={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird=Menu('Early Bird',early_bird_menu,15,18)
#DINNER
dinner_menu={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner=Menu('Dinner',dinner_menu,17,23)
#KIDS MENU
kids_menu={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids=Menu("Kids",kids_menu,11,21)

#print(brunch)
breakfast_order=['pancakes','home fries','coffee']

print(brunch.calculate_bill(breakfast_order))

early_bird_order=['salumeria plate','mushroom ravioli (vegan)']

print(early_bird.calculate_bill(early_bird_order))
#CREATING THE FRANCHISES
all_menus=[brunch,early_bird,dinner,kids]

class Franchise:
  def __init__(self,address,menus):
    self.address=address
    self.menus=menus
  
  def __repr__(self):
    return "The address is "+ str(self.address)
  
  def available_menus(self,time):
    available_menus=[]
    for menu in all_menus:
      if time >=menu.start_time and time <=menu.end_time:
        available_menus.append(menu.name)
    return available_menus
  

flagship_store=Franchise('1232 West End Road', all_menus)

new_installment=Franchise('12 East Mulberry Street', all_menus)

#print(flagship_store)


print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
# CREATING BUSINESSES!
franchise_list=[flagship_store,new_installment]

arepas_menu={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas=Menu("Take a' Arepa",arepas_menu,10,20)
all_menus.append(arepas)
print(all_menus)

arepas_place=Franchise('189 Fitzgerald Avenue',all_menus)
class Business:
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
  
basta_fazoolin=Business("Basta Fazoolin' with my Heart",franchise_list)

arepa=Business("Take a'Arepa",franchise_list)
