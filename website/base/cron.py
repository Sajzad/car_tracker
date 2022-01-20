import random
from .models import Assignment, LatLong


def to_do():
	print("try")
	try:
		assignments = Assignment.objects.all()
		total = assignments.count()
		upto = 60//total
		if upto<1:
			upto = 1
		for _ in range(upto):
			for item in assignments:
				assignment_id = item.id
				lat = round(random.uniform(10.33, 66.66), 2)
				lng = round(random.uniform(10.55, 99.33), 2)
				LatLong.objects.create(
					assignment_id = assignment_id,
					lat = lat,
					lng = lng)
	except Exception as e:
		print(e)

def my_scheduled_job():
	to_do()

