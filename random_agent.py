import constants
import random

class Agent:
	def __init__(self, id):
		self.id = id
		self.PLAYER_TURN_INDEX = 0
		self.PROPERTY_STATUS_INDEX = 1
		self.PLAYER_POSITION_INDEX = 2
		self.PLAYER_CASH_INDEX = 3
		self.PHASE_NUMBER_INDEX = 4
		self.PHASE_PAYLOAD_INDEX = 5
		self.DEBT_INDEX = 6
		self.STATE_HISTORY_INDEX = 7
		
		self.CHANCE_GET_OUT_OF_JAIL_FREE = 40
		self.COMMUNITY_GET_OUT_OF_JAIL_FREE = 41

	def getBSMTDecision(self, state):
		current_player = self.id - 1
		n = random.randint(1,4)
		debt = 0
		debt = self.parseDebt(state, current_player)[1]
		
		money = state[self.PLAYER_CASH_INDEX][current_player]
		actual_debt = debt - money
		if n == 1 and debt == 0:
			return self.buying_strategy(state, current_player)
		elif n == 2:
			(remaining_debt, return_sell_list) = self.selling_strategy(state, current_player, actual_debt)
			if len(return_sell_list) != 0:
				return ("S", return_sell_list)
			else:
				return None
		elif n == 3:
			return self.mortgage_strategy(state, current_player, actual_debt)
		else:
			return None


	def mortgage_strategy(self, state, current_player, debt):
		owned_properties = self.get_owned_property_not_morgaged(state, current_player)
		actual_properties_ids = []
		for id in owned_properties:
			actual_properties_ids.append(constants.property_to_space_map[id])
		list_mortgage_properties = []
		for property in actual_properties_ids:
			n = random.randint(0, 1)
			if n == 1:
				debt -= constants.board[property]["price"] * 0.5
				list_mortgage_properties.append(property)
				if debt <= 0:
					break
		if len(list_mortgage_properties) == 0:
			return None
		else:
			return ("M", list_mortgage_properties)

	def get_owned_property_not_morgaged(self, state, current_player):
		owned_properties = []
		i = 0
		for status in state[self.PROPERTY_STATUS_INDEX]:
			if current_player == 0 and status > 0 and status != 7 and i in constants.property_to_space_map:
				owned_properties.append(i)
			elif current_player == 1 and status < 0 and status != -7 and i in constants.property_to_space_map:
				owned_properties.append(i)
			i = i + 1
		return owned_properties


	def selling_strategy(self, state, current_player, debt):
		monopoly_groups = self.findMonopolyGroups(state, current_player)
		number_of_houses = 4
		return_sell_list = []
		while number_of_houses > 0:
			groups = self.find_groups(monopoly_groups, number_of_houses, current_player, state)
			n = random.randint(0, 1)
			if len(groups) != 0 and n == 1:
				(remaining_debt, total_houses_sold_per_group) = self.clear_debt(groups, number_of_houses, debt)
				self.create_sell_list(total_houses_sold_per_group, groups, return_sell_list)
				debt = remaining_debt
				if remaining_debt <= 0:
					break

			number_of_houses = number_of_houses - 1
		return (debt, return_sell_list)

	def create_sell_list(self, total_houses_sold_per_group, groups, return_sell_list):
		i = 0
		for group in groups:
			for property in group:
				number_of_houses_sold = total_houses_sold_per_group[i]
				return_sell_list.append((property, number_of_houses_sold))
			i = i + 1

	def clear_debt(self, groups, number_of_houses, debt):
		total_houses_sold_per_group = {}
		i = 0
		for group in groups:
			total_houses_sold = 0
			while number_of_houses > 0 and debt > 0:
				for property in group:
					debt -= constants.board[property]['build_cost'] * 0.5
				total_houses_sold = total_houses_sold + 1
				number_of_houses = number_of_houses - 1

			total_houses_sold_per_group[i] = total_houses_sold
			i = i + 1
		return (debt, total_houses_sold_per_group)

	def buying_strategy(self, state, current_player):
		monopoly_groups = self.findMonopolyGroups(state, current_player)
		if len(monopoly_groups) == 0:
			return None
		number_of_houses = 0
		group = []
		while number_of_houses < 4:
			group = self.find_group_investment(monopoly_groups, number_of_houses, current_player, state)
			if len(group) != 0 : break
			number_of_houses = number_of_houses + 1

		if len(group) == 0:
			return None
		buy_list = []

		for property in group:
			buy_list.append((property, 1))
		return ("B", buy_list)

	def find_groups(self, monopoly_groups, number_houses, current_player, state):
		status = [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]]
		groups = []
		for group in monopoly_groups:
			isGroupFound = True
			for property_id in group:
				state_property_id = constants.space_to_property_map[property_id]
				if status[current_player][number_houses] != state[self.PROPERTY_STATUS_INDEX][state_property_id]:
					isGroupFound = False
			if isGroupFound:
				groups.append(group)
		return groups

	def find_group_investment(self, monopoly_groups, number_houses, current_player, state):
		n = random.randint(0,1)
		status = [[1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]]
		for group in monopoly_groups:
			investment = state[self.PLAYER_CASH_INDEX][current_player] * 0.5
			for property_id in group:
				state_property_id = constants.space_to_property_map[property_id]
				if status[current_player][number_houses] == state[self.PROPERTY_STATUS_INDEX][state_property_id]:
					if constants.board[property_id]['build_cost'] != 0:
						investment -= constants.board[property_id]['build_cost']
			if investment >= 0 and investment != state[self.PLAYER_CASH_INDEX][current_player] * 0.5 and n == 1:
				return group
		return []

	def findMonopolyGroups(self, state, current_player):
		monopoly_groups = []
		range_status = [[1, 6], [-6, -1]]
		properties_status = state[self.PROPERTY_STATUS_INDEX]
		i = 0
		for status in properties_status:
			if status >= range_status[current_player][0] and status <= range_status[current_player][
				1] and i in constants.property_to_space_map:
				property_id = constants.property_to_space_map[i]
				groupElements = constants.board[property_id]["monopoly_group_elements"]
				have_monopoly = True
				for element in groupElements:
					state_property_id = constants.space_to_property_map[element]
					status_element = state[self.PROPERTY_STATUS_INDEX][state_property_id]
					if status_element >= range_status[current_player][0] and status_element <= \
							range_status[current_player][1]:
						have_monopoly = True
					else:
						have_monopoly = False
						break
				if have_monopoly == True:
					group = []
					if constants.board[property_id]['build_cost'] != 0:
						group.append(property_id)
						for element in groupElements:
							group.append(element)
						monopoly_groups.append(group)
			i = i + 1
		d = {}
		unique_monopoly_groups = []
		for group in monopoly_groups:
			for property in group:
				if property not in d:
					unique_monopoly_groups.append(group)
					for p in group:
						d[p] = 1
		return unique_monopoly_groups

	def respondTrade(self, state):
		n = random.randint(0,1)
		if n == 1:
			return True
		return False

	def buyProperty(self, state):
		(debt, receiver) = self.parseDebt(state, self.id - 1)
		property = constants.board[state[self.PHASE_PAYLOAD_INDEX]]

		current_player = state[self.PLAYER_TURN_INDEX] % 2
		playerCash = state[self.PLAYER_CASH_INDEX][current_player]

		n = random.randint(0,1)
		if playerCash >= debt and n == 1:
			return True
		else:
			return False

	def auctionProperty(self, state):

		playerPosition = state[self.PHASE_PAYLOAD_INDEX][0]
		propertyPrice = constants.board[playerPosition]['price']
		current_player = state[self.PLAYER_TURN_INDEX] % 2
		current_player_money = state[self.PLAYER_CASH_INDEX][current_player]
		n = random.randint(0, current_player_money)
		return n

	def receiveState(self, state):
		pass

	def parseDebt(self, state, current_player):
		debt = state[self.DEBT_INDEX]
		money_owed = 0
		source = 0
		if current_player == 0:
			money_owed = debt[1]
			source = debt[0]
		else:
			money_owed = debt[3]
			source = debt[2]
		return  (source, money_owed)

	def jailDecision(self, state):
		n = random.randint(0, 3)
		current_player = state[self.PLAYER_TURN_INDEX] % 2
		playerCash = state[self.PLAYER_CASH_INDEX][current_player]
		check_list = [1, -1]
		if state[self.PROPERTY_STATUS_INDEX][self.CHANCE_GET_OUT_OF_JAIL_FREE] == check_list[current_player] and n == 0:
			return ("C", self.CHANCE_GET_OUT_OF_JAIL_FREE)
		elif state[self.PROPERTY_STATUS_INDEX][self.COMMUNITY_GET_OUT_OF_JAIL_FREE] == check_list[current_player] and n == 1:
			return ("C", self.COMMUNITY_GET_OUT_OF_JAIL_FREE)
		elif playerCash >= 50 and n == 2:
			return ("P")
		else:
			return ("R")

	def respondMortgage(self, state):
		n = random.randint(0, 1)
		if n == 1:
			return True
		return False
