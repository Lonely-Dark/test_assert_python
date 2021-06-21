def exc(text):
	assert text != '', "Nothing" #вызывает ошибку, если в функцию exc не передали аргумент
	print(text + '!') 
	
exc('')