class HourClock:
	
	def __init__(self, hours=0) -> int:
		self.count_hours = hours

	@property
	def hours(self):
		text_hours = ' часа.' if self.count_hours%10 in (2, 3, 4) else ' часов.'
		text_hours = ' час.' if self.count_hours == 1 else text_hours
		print(f'На часах сейчас ',self.count_hours, text_hours)
		return self.count_hours

	@hours.setter
	def hours(self, new):
		#print(f'',self.count_hours,' -- ',new)
		time_diff = abs(new - self.count_hours)
		self.count_hours = new % 12
		 
		# text_hours = ' часа.' if time_diff%10 in (2, 3, 4) else ' часов.'
		# text_hours = ' час.' if time_diff == 1 else text_hours
		# print(f'Время изменилось на ', time_diff, text_hours)
		return self.count_hours



clock = HourClock()
print(clock.__dict__)
clock.hours += 5
clock.hours += 5
clock.hours += 5
clock.hours -= 4
clock.hours
clock.hours = 123
clock.hours
