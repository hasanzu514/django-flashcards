from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


def add(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		if not request.POST['answer'] or not request.POST['answer'].isnumeric() :
			my_answer = "Hey you didn't write an answer or number!"
			correct = False
			return render(request, 'add.html', {
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'correct':correct,
				})

		answer = int(request.POST['answer'])
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) + int(old_num_2)

		if answer == correct_answer:
			my_answer = "Correct! " + str(old_num_1) + " + " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = True
		else:	
			my_answer = "Incorrect! " + str(old_num_1) + " + " + str(old_num_2) + " is not " + str(answer)  + "! " + str(old_num_1) + " + " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = False

		return render(request, 'add.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'correct':correct
			})


	return render(request, 'add.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def subtract(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		if not request.POST['answer'] or not request.POST['answer'][1:].isnumeric() :
			my_answer = "Hey you didn't write an answer or number!"
			correct = False
			return render(request, 'subtract.html', {
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'correct':correct,
				})

		answer = int(request.POST['answer'])
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) - int(old_num_2)

		if answer == correct_answer:
			my_answer = "Correct! " + str(old_num_1) + " - " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = True
		else:	
			my_answer = "Incorrect! " + str(old_num_1) + " - " + str(old_num_2) + " is not " + str(answer)  + "! " + str(old_num_1) + " - " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = False

		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'correct':correct
			})


	return render(request, 'subtract.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def multiply(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		if not request.POST['answer'] or not request.POST['answer'].isnumeric() :
			my_answer = "Hey you didn't write an answer or number!"
			correct = False
			return render(request, 'multiply.html', {
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'correct':correct,
				})

		answer = int(request.POST['answer'])
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) * int(old_num_2)

		if answer == correct_answer:
			my_answer = "Correct! " + str(old_num_1) + " x " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = True
		else:	
			my_answer = "Incorrect! " + str(old_num_1) + " x " + str(old_num_2) + " is not " + str(answer)  + "! " + str(old_num_1) + " x " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = False

		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'correct':correct
			})


	return render(request, 'multiply.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def divide(request):
	from random import randint

	factor = True
	while factor:
		num_1 = randint(0,10)
		num_2 = randint(1,10)
		if num_1%num_2 == 0:
			break


	if request.method == "POST":
		if not request.POST['answer'] or not request.POST['answer'].isnumeric() :
			my_answer = "Hey you didn't write an answer or number!"
			correct = False
			return render(request, 'divide.html', {
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'correct':correct,
				})

		answer = int(request.POST['answer'])
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(int(old_num_1) / int(old_num_2))



		if answer == correct_answer:
			my_answer = "Correct! " + str(old_num_1) + " / " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = True
		else:	
			my_answer = "Incorrect! " + str(old_num_1) + " / " + str(old_num_2) + " is not " + str(answer)  + "! " + str(old_num_1) + " x " + str(old_num_2) + " = " + str(correct_answer)  + "."
			correct = False

		return render(request, 'divide.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'correct':correct
			})


	return render(request, 'divide.html', {
		'num_1':num_1,
		'num_2':num_2,
		})