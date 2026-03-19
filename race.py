
t=42+(42/60)
d=t/60
pace=t/10
paceminutes=int(pace)
paceseconds=((pace-paceminutes)*60)
avgpace=paceminutes+paceseconds
avgspeed=10/d
print("average pace is:", avgpace,'min/km')
print("average speed is:", avgspeed,"km/hr")
#where 10 is the distance travelled in kms by a runner in 42 mins and 42 secs
#think python ch 1 exercise 1-2