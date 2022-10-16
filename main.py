from utils import city
        
mycity = city()
#mycity.setup()
print("="*50)
print(f"There are {mycity.CARS_NUM} cars")
print(f"Their positions are {mycity.cars_positions}")
print(f"There are {mycity.USERS_NUM} users")
print(f"Their positions are {mycity.users_positions}")
print(f"The city dimensions are {mycity.city_dimensions[0]} x {mycity.city_dimensions[1]}")

print("="*50)
