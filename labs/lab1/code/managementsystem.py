#Program for Hotel and flight booking
import random
# class to check if flight/hotel are available for the specified dates
class Booking:
    def __init__(self):
        pass

    def checkAvailability(self,**kwargs):
        booking_type = kwargs['booking_type']
        booking_class = kwargs['booking_class']
        if booking_type == "Airline":
            departure_date = kwargs['departure_date']
            airline = kwargs['airline']
            if airline.AIRLINE_SEATS[booking_class] != 0 :
                print ("Flight Available\t")
                return True
            else:
                print ("Flight Not Available\n")
                return False
        elif booking_type == "Hotel":
            if H1.HOTEL_ROOM[booking_class] != 0:
                print ("Hotel Available\n")
                return True
            else:
                print ("Hotel Not Available\n")
                return False
# To make a reservation
    def makeReservation(self,**kwargs):
        booking_type = kwargs['booking_type']
        customer = kwargs['customer']
        availability_status = kwargs['availability_status']
        if availability_status and booking_type == "Airline":
            booking_class = kwargs['booking_class']
            airline = kwargs['airline']
            airline.AIRLINE_SEATS[booking_class] -= 1
            customer.customer_record['Wallet'] += airline.AIRLINE_PRICE[booking_class]
            customer.customer_record['Booking ID']['Airline'] = "AIR" + str(random.randrange(10,1000,2))
        elif (availability_status == True) and (booking_type == "Hotel"):
            booking_class = kwargs['booking_class']
            hotel = kwargs['hotel']
            hotel.HOTEL_ROOM[booking_class] -= 1
            customer.customer_record['Wallet'] += hotel.HOTEL_PRICE[booking_class]
            customer.customer_record['Booking ID']['Hotel'] = "HOT" + str(random.randrange(10,1000,2))

# Class for airlines describing the type of ticket with price
class Airline(Booking):
    def __init__(self,airline_name):
        super(Airline, self).__init__()
        self.airline_name = airline_name
        self.AIRLINE_SEATS = { 'Business Class' : 50,
                               'First Class'    : 50,
                               'Premium Economy': 100,
                               'Regular Economy': 150
                             }
        self.AIRLINE_PRICE = { 'Business Class' : 2500,
                               'First Class'    : 2000,
                               'Premium Economy': 1800,
                               'Regular Economy': 1500
                             }

# Class for Hotel describing the type of room with price
class Hotel(Booking):
    def __init__(self,hotel_name):
        Booking.__init__(self)
        self.hotel_name = hotel_name
        self.HOTEL_ROOM = {'Penthouse'             : 10,
                           'King Deluxe Bedroom'    : 20,
                           'Queen Deluxe Bedroom'   : 20,
                           'Kind Standard Bedroom' : 30,
                           'Queen Standard Bedroom': 50
                           }
        self.HOTEL_PRICE = {'Penthouse'            : 1000,
                            'King Deluxe Bedroom'    : 700,
                            'Queen Deluxe Bedroom'   : 600,
                            'Kind Standard Bedroom' : 450,
                            'Queen Standard Bedroom': 350
                           }
# Class to check if its possible to make reservation
class Bookable(object):
    def is_available(self, **kwargs):
        raise NotImplementedError
# private variable
    def __make_reservation(self, **kwargs):
        raise NotImplementedError
# Customer details for a particular booking
class Customer:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.cost = 0
        self.customer_record = {'Name'  : self.f_name + " " + self.l_name,
                                'Wallet': self.cost,
                                'Booking ID' : {}
                               }
    def printcustomerrecord(self):
            for k,v in self.customer_record.items():
                print(k + "\t" + str(v) + "\n")

#Pass necessary calls
C1 = Customer("Bhargavi","Siddipeta")
A1 = Airline("Air India")
availability = A1.checkAvailability(airline = A1, booking_type = "Airline", booking_class = "Business Class", departure_date = "07072014")
A1.makeReservation(airline = A1, customer = C1, booking_type = "Airline", booking_class = "Business Class", availability_status = availability)
H1 = Hotel("Sheraton")
availability = H1.checkAvailability(airline = H1, booking_type = "Hotel", booking_class = "Penthouse", checkin = "07072014", checkout = "07102014")
H1.makeReservation(hotel = H1, customer = C1, booking_type = "Hotel", booking_class = "Penthouse", availability_status = availability)
C1.printcustomerrecord()