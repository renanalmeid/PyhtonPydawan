#Our travel application users want to calculate the total expenses they may have to incur on a trip.

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate*trip_time
  hotel_total = hotel_rate*trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses (200, 100, 100, 5)