#// we need the date time module 
from datetime import datetime

class GenerateQuote:
    
    # .. overide the init function
    def __init__(self, vSize, distance, helpers, floors, job_date):
        
        
        # .. discount 
        self.off_peak_discount = 10 # // percent 
        self.on_peak_discount = 15 # percent 
        self.lDistance = 100 # kms
        self.tGateFee = 0.0
        
        # onpeak 
        self.peakDays = [25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5]
        self.date = job_date 
        self.distance = distance
        # self.date = datetime.strptime(job_date, '%Y-%m-%d')
        
        # ... params 
        self.sDistanceParams = {
            
        #.. key   base,   pricePerKM,   HelperFee,  floorFee,  tall gate 
            1.0: [200, 15.5*distance, 150*helpers, 50*floors,  self.tGateFee],
            1.5: [300, 17.0*distance, 200*helpers, 60*floors, self.tGateFee]
 
        }\
        .get(float(vSize))
        
                #... long term movement 
        self.lDistanceParams = {
            #// key  base, pricePerKM, HelperFee, Price Per Floor
                1.0: [200, 15.5*distance, 150*helpers, 50*floors, self.tGateFee],
                1.5: [300, 17.0*distance, 200*helpers, 60*floors, self.tGateFee]
                #//
        }\
        .get(float(vSize))
        
    # check off peak 
    def __peak_discount(self, quote):
        
        # .. define date 
        _date = self.date
        if(isinstance(_date, str)):
            _date = datetime.strptime(self.date, '%Y-%m-%d')

        # ... check date 
        if(_date.day not in self.peakDays):
            # ... return 
            return quote*(self.off_peak_discount/100.0), True
        
        # ... else just return 
        return quote*(self.on_peak_discount/100.0), False 
    
    # calculate quote 
    def __calculate_quote(self):
        
        # .. check distance to choose correct formular 
        if(self.distance < self.lDistance): 
            return sum(self.sDistanceParams)
        
        # else long distance 
        return sum(self.lDistanceParams)
    

    # .. generate quote 
    @property
    def base_discounts(self):

        # ... generate 
        quote = self.__calculate_quote()
        dPeak, apply = self.__peak_discount(quote)
        
        # .. check
        if(apply):
            return quote, dPeak
        # ... else
        return (quote + dPeak), 0