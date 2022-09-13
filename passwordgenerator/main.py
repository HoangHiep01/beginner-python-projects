import random


def generate_password(password_length):

	lower_char = "abcdefghijklmnopqrstuvwxyz"
	upper_char = "abcdefghijklmnopqrstuvwxyz".upper()
	symbol = "!@#$%^&*()"
	number = "0123456789"
	sample = lower_char + upper_char + number + symbol

	password = random.sample(sample, password_length)

	return "".join(password)

def main():

	password_length = int(input("How long would you like your password to be: "))
	print("Your password is: ", generate_password(password_length))

if __name__ == "__main__":
	main()
