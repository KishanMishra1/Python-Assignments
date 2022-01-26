'''Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.

Go through the below program and complete it based on the comments mentioned in it.'''

#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=['AI101:MUM:LON:001','AI101:MUM:LON:002','SI456:MUM:SIN:145', 'EM456:MUM:DUB:098', 'SI456:MUM:SIN:050', 'SI456:MUM:SIN:051']

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    res=[]
    for i in ticket_list:
        str_list=i.split(':')
        res.append(str_list[2])
    return res.count(destination)
    #Remove pass and write your logic here

def find_passengers_per_flight():
    k=[]
    t=[]
    for i in ticket_list:
        flightno=i.split(":")
        k.append(flightno[0])
    for i in k:
        t.append(i+":"+str(k.count(i)))
    return t
    #Remove pass and write your logic here

def sort_passenger_list():
    res=[]
    a=find_passengers_per_flight()
    a=sorted(a,reverse=True)
    return a

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(find_passengers_per_flight())
print(sort_passenger_list())
