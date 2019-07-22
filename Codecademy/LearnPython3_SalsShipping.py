# Codecademy Solution - Sal's Shipping
# Write a program that asks the user for the weight of their package and then tells them which method of
# shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

def ground_shipping_cost(weight):
  price_per_pound = 0
  if (weight <= 2):
    price_per_pound = 1.5
  elif (weight <= 6):
    price_per_pound = 3
  elif (weight <= 10):
    price_per_pound = 4
  else:
    price_per_pound = 4.75
  return price_per_pound * weight + 20

def drone_shipping_cost(weight):
  price_per_pound = 0
  if (weight <= 2):
    price_per_pound = 4.5
  elif (weight <= 6):
    price_per_pound = 9
  elif (weight <= 10):
    price_per_pound = 12
  else:
    price_per_pound = 14.25
  return price_per_pound * weight

def shipping_option(weight):
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)
  if (ground < drone) and (ground < premium_ground):
    print("Ground shipping is cheapest at $" + str(ground))
  elif (drone < ground) and (drone < premium_ground):
    print("Drone shipping is cheapest at $" + str(drone))
  else:
    print("Premium shipping is cheapest at $" + str(premium_ground))

premium_ground = 125

package_weight = float(input("Enter the package weight in pounds (lbs) to calculate shipping costs: "))
shipping_option(package_weight)
input('Press Enter to exit')