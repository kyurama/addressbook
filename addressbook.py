# console based address book, able to add, retrieve, and update entries.
# saves entries in a .txt

import sqlite3
import os
from sqlite3 import Error

class AddrEntry():
	def __init__(self, firstName, lastName, email, phone, streetAddr, city, state, zipCode):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.phone = phone
		self.streetAddr = streetAddr
		self.city = city
		self.state = state
		self.zipCode = zipCode

	def set_first_name(self, firstName):
		self.firstName = firstName

	def set_last_name(self, lastName):
		self.lastName = lastName

	def set_email(self, email):
		self.email = email

	def set_phone(self, phone):
		self.phone = phone

	def set_street_addr(self, streetAddr):
		self.streetAddr = streetAddr

	def set_city(self, city):
		self.city = city

	def set_state(self, state):
		self.state = state

	def set_zip(self, zipCode):
		self.zipCode = zipCode

	def print_entry(self):
		print("+------------------------------------------+")
		fullName = self.firstName + ' ' + self.lastName
		cityState = self.city + ', ' + self.state
		print(f"| Name: {fullName.ljust(35)}|")
		print(f"| Email Address: {self.email.ljust(26)}|")
		print(f"| Phone Number: {self.phone.ljust(27)}|")
		print(f"| Street Address: {self.streetAddr.ljust(25)}|")
		print(f"| City: {cityState.ljust(35)}|")
		print(f"| Zip: {self.zipCode.ljust(36)}|")
		print("+------------------------------------------+")

def create_connection(db_file):
	""" Create DB Conneciton """
	conn = None

	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

# main program interaction
def get_user_input():
	print("Address Book Program\n")
	userInput = input("What would you like to do?(? for help) ").upper()
	while userInput != 'Q':
		if userInput == '?':
			print("(C)reate new entry")
			print("(D)elete existing entry")
			print("(Q)uit the program")
			print("(R)etrieve existing entry")
			print("(U)pdate existing entry")
			print("(?) Opens this menu")
		elif userInput == 'C':
			print("Adding a new entry")
			addr = AddrEntry(input('First Name: '), input('Last Name: '), input('Email Address: '), input('Phone Number: '), input('Street Address: '), input('City: '), input('State: '), input('Zip Code: '))
		elif userInput == 'D':
			pass
		elif userInput == 'R':
			pass
		elif userInput == 'U':
			pass
		else:
			print("Invalid Input")

create_connection(os.path.expanduser(r"~/Documents/addresses.db"))
