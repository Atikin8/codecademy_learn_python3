def ground_shipping_cost(weight):
  cost=0
  if weight <=2:
    cost=1.5*weight+20
  elif weight >2 and weight<=6:
    cost=3*weight+20
  elif weight >6 and weight <=10:
    cost=4*weight+20
  else:
    cost=4.75*weight+20
  return cost

print(ground_shipping_cost(1))

premium_shipping_cost=125

def drone_shipping_cost(weight):
  cost=0
  if weight <=2:
    cost=4.5*weight
  elif weight >2 and weight<=6:
    cost=9*weight
  elif weight >6 and weight <=10:
    cost=12*weight
  else:
    cost=14.25*weight
  return cost

print(drone_shipping_cost(1))

def cheapest_method(weight):
  ground=ground_shipping_cost(weight)
  drone=drone_shipping_cost(weight)
  premium=premium_shipping_cost
  cheapest=ground
  method='Ground'
  if drone<cheapest and drone<premium:
    cheapest=drone
    method='Drone'
  if premium<cheapest:
    cheapest=premium
    method='Premium'

  print('You should ship using ' +method+' shipping, it will cost $'+str(format(cheapest,'.2f'))+' dollars.')

cheapest_method(4.8)
cheapest_method(41.5)