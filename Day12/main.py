# global Scope
player_health = 10

def game():
	def drink_potion():
		potion_strength = 2
		print(potion_strength)
	drink_potion()


game_level = 3
def create_enemy():
	enemies = ["Skeleton", "Zombie", "Alien"]
	if game_level < 5:
		new_enemy = enemies[0]
	print(new_enemy)

enemies = 1

def increase_enemies():
	print(f"enemies insde function: {enemies}")
	return enemies + 1

print(f"enemies outside function: {enemies}")
