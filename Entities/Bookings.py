class Bookings:
  
    def __init__ (self, toolID, userName, bookInCondition, startDate, startTerm, expectedReturnDate, expectedTerm,
                  returnDate = "", bookOutCondition = "", pickUpLocation = "", dropOffLocation = ""):
        self.toolID = toolID
        self.userName = userName
        self.bookInCondition = bookInCondition
        self.startDate = startDate
        self.startTerm = startTerm
        self.expectedReturnDate = expectedReturnDate
        self.expectedTerm = expectedTerm
        self.returnDate = returnDate
        self.bookOutCondition = bookOutCondition
        self.pickUpLocation = pickUpLocation
        self.dropOffLocation = dropOffLocation
    
    def getToolID(self):
        return self.toolID
    
    def getUserName(self):
        return self.userName

    def getBookInCondition(self):
        return self.bookInCondition

    def getStartDate(self):
        return self.startDate

    def getStartTerm(self):
        return self.startTerm

    def getExpectedReturnDate(self):
        return self.expectedReturnDate

    def getExpectedTerm(self):
        return self.expectedTerm

    def getReturnDate(self):
        return self.returnDate
      
    def setReturnDate(self, returnDate):
        self.returnDate = returnDate

    def getBookOutCondition(self):
        return self.bookOutCondition

    def getPickUpLocation(self):
        return self.pickUpLocation

    def getDropOffLocation(self):
        return self.dropOffLocation

    def setPickUpLocation(self, location):
        self.pickUpLocation = location

    def setDropOffLocation(self, location):
        self.dropOffLocation = location