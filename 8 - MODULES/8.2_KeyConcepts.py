#Datetime module
#strptime()
#strftime()

from datetime import datetime 

#create a date using year,month, day 

birthday = datetime(1996, 8, 30, 8, 20)
birthday.year

# creating a date using datetime.now()
# current day time
datetime(2018,1,1)-datetime(2017,1,1)
#printa diferença de tempo 
datetime.now()-datetime(2018,1,1)
#diferença dias, segundos e afins


##strptime()

#checar no site a data do argumento 
parsed_date = datetime.strptime('Jan 15, 20218', )
parsed_date = datetime.strptime('Jan 15, 20218', '%b %d, %Y')

parsed_date.month
parsed_date.year 


## strftime()
#take day time 

#cria uma string de uma int
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')


