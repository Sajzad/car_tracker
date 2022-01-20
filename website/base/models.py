from django.db import models
import random



def random_number(length):
    return ''.join([str(random.randint(0,9)) for _ in range(6)])

# Create your models here.

class Car(models.Model):
	car = models.CharField(max_length=50)

	def __str__(self):
		return self.car

class Operator(models.Model):
	name = models.CharField(max_length=30)
	unique_name = models.CharField(max_length=30, null=True, blank=True)
	code = models.CharField(max_length=10,null=True, blank=True)

	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		op_obj = Operator.objects.filter(name=self.name)
		if op_obj.exists():
			while True:
				unique_name = self.name+str(random.randint(1,100))
				op_obj = op_obj.filter(name=unique_name)
				if op_obj.exists():
					print(unique_name)
					continue
				else:
					self.unique_name = unique_name
					break
		else:
			self.unique_name = self.name

		code = random_number(6)
		check_code = op_obj.filter(code=code)
		if check_code.exists():
			while True:
				code = random_number(6)
				op_obj = op_obj.filter(code=code)
				if op_obj.exists():
					continue
				else:
					self.code = code
					break
		else:
			self.code = code



		super(Operator, self).save(*args, **kwargs)

class City(models.Model):
	name = models.CharField(max_length=30)
	file = models.FileField(upload_to='city/', default=None)

	def __str__(self):
		return self.name

class Assignment(models.Model):
	operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.operator.name

class LatLong(models.Model):
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment_items')
	lat = models.DecimalField(max_digits=5, decimal_places=3, default=0)
	lng = models.DecimalField(max_digits=5, decimal_places=3, default=0)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.assignment.operator.name