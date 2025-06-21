# NAME: Hilary Chol Libo Nyawella
# REG. NO. M25B13/050
# ACC. NO B33493

#CHALLANGE 1: EVEN AND ODD NUMBER,
def main():
	print("Welcome to the Indentation Race!")
	for i in range(5):
		print(f"Current number: {i}")
		if i % 2 == 0 and i != 4:
			print("Even number.")	
		elif i == 4:
			print("Race complete.")
		else: 	
			print("Odd number.")	
			
main()
		