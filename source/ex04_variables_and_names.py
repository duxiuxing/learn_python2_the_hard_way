# coding=utf-8
# 习题 4: 变量和命名
# 变量名采用小写字母，单词之间以下划线作为分隔符，这只是一种命名规范
# 注意：print在拼接输出内容的时候，会自动加空格

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print '----------'

print 'Learn', "PYTHON", "the HARD WAY"
