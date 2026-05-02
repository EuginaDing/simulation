import random as random
import logging  
import datetime as dt
import os   
class Customer:
    
    def __init__(self, timein=0, timeout=0, desk_time=0, lineID=0, served=False, cID=0):
        self.timein = timein
        self.timeout = timeout
        self.desk_time = desk_time
        self.lineID = lineID
        self.served = served
        self.cID=cID
        
class Line:
    def __init__(self, maxLength):
        self.line_customers = list(Customer())
        self.maxlength = maxLength
    def checkFull(self):
        if len(self.customers) < self.maxlength:
            return False
        else:
            return True
                
class LineOperator:
    def __init__(self, maxNoLines):
        self.lines = list[Line] 
        self.maxNoLines = maxNoLines
        self.all_customers=list[Customer]
        for i in range(self.maxNoLines):
            self.lines.append(Line(random.randint(10,15)))
            
    def findMinLine(self):
        min_lineLen=float('inf')
        min_lineID=0
        for line in self.lines:
            if len(line.line_customers)<min_lineLen and line.checkFull()==False:
                min_lineLen=len(line.line_customers)
                min_lineID=self.lines.index(line)
        return min_lineID    
    
    def findMaxLine(self): 
        max_lineLen=0
        max_lineID=0
        for line in self.lines:
            if len(line.line_customers)>max_lineLen:
                max_lineLen=len(line.line_customers)
                max_lineID=self.lines.index(line)
        return max_lineID    
      
    def addCustomer(self, simulation_time):
        #find the line with the least customers and add the customer to that line
        min_lineID=self.findMinLine()
        if self.lines[min_lineID].checkFull()==False:
            customer = Customer()
            customer.timein = simulation_time
            customer.lineID = min_lineID
            customer.cID = len(self.customers)
            self.lines[min_lineID].line_customers.append(customer)
            self.customers.append(customer)
            
            return customer
        else:
            return None
        
    def removeCustomer(self, simulation_time):  
         
        max_lineID=self.findMaxLine()
        if len(self.lines[max_lineID].line_customers)>0:
            customer=self.lines[max_lineID].line_customers.pop(0)
            customer.served=True
            customer.timeout=simulation_time
            return customer
        else:
            return None
        
    def calculateWait(self, simulation_time):
        total_wait = [0] * self.maxNoLines
        total_customers = [0] * self.maxNoLines
        avg_wait = [0] * self.maxNoLines
        for customer in self.all_customers:
            if customer.served == False:
                customer.timeout = simulation_time
            total_wait[customer.lineID] += (customer.timeout - customer.timein)
            total_customers[customer.lineID] += 1
        for i in range(self.maxNoLines):
            if total_customers[i] > 0:
                avg_wait[i] = total_wait[i] / total_customers[i]
                
        return (total_wait, avg_wait)
    
    def calculateServiceTime(self):
        total_service_time = 0
        avg_service_time = 0
        customer_serviced = 0
        for customer in self.all_customers:
            if customer.served == True:
                total_service_time += (customer.timeout - customer.timein)+customer.desk_time
                customer_serviced += 1
        if len(self.all_customers) > 0:
            avg_service_time = total_service_time / customer_serviced
        return (total_service_time, avg_service_time)   
        