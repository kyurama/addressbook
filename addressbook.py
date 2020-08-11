# console based address book, able to add, retrieve, and update entries.
# saves entries in a .txt

import io

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

	def setFirstName(self, firstName):
		self.firstName = firstName

	def setLastName(self, lastName):
		self.lastName = lastName

	def setEmail(self, email):
		self.email = email

	def setPhone(self, phone):
		self.phone = phone

	def setstreetAddr(self, streetAddr):
		self.streetAddr = streetAddr

	def setCity(self, city):
		self.city = city

	def setState(self, state):
		self.state = state

	def setZip(self, zipCode):
		self.zipCode = zipCode

	def printEntry(self):
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

entry = AddrEntry('James', 'Taylor', 'kyu@gmail.com', '256-555-5555', '100 oak street', 'Opelika', 'AL', '36803')

entry.printEntry()