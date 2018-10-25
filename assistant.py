#agent type: assistant
#percepts : tasks,start and completion times,priorityIndex measure,frequency of reminders
#actions : scheduled tasks,reminders.
import time;
class MyAssistant:
#current state of the agent
    def __init__(self):
        self.currentStateTime = time.asctime( time.localtime(time.time()) )
        self.currentStateTask = {'name': 'testName1','startTime':2, 'completionTime': 4,
                                  'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                  'postponable': 'False','postponments':5, 'duration':2,
                                  'scheduled':'False'}
        self.currentStateNotifications = {'name': 'testName', 'message': 'message','howOften':'how often should the notification be made'}
        self.currentConsideredpriorityIndex = 10
        self.consideredNextEventDictionary ={ 'eventNumber0' : {'name': 'testName1','startTime':2, 'completionTime': 4,
                                                                         'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                                                         'postponable': 'False','postponments':5, 'duration':2,
                                                                         'scheduled':'False'},
                                              'eventNumber1' : {'name': 'testName1','startTime':2, 'completionTime': 4,
                                                                        'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                                                        'postponable': 'False','postponments':5, 'duration':2,
                                                                        'scheduled':'False'},
                                              'eventNumber2' : {'name': 'testName1','startTime':2, 'completionTime': 4,
                                                                        'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                                                        'postponable': 'False','postponments':5, 'duration':2,
                                                                        'scheduled':'False'},
                                              'eventNumber3' : {'name': 'testName1','startTime':2, 'completionTime': 4,
                                                                        'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                                                        'postponable': 'False','postponments':5, 'duration':2,
                                                                        'scheduled':'False'},
                                              'eventNumber4' : {'name': 'testName1','startTime':2, 'completionTime': 4,
                                                                        'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 4,
                                                                        'postponable': 'False','postponments':5, 'duration':2,
                                                                        'scheduled':'False'}}
        self.currentStateNextEvent = "nextEvent"
        self.todayEventDict= { 'event0' : {'name': 'yakwanza','startTime':2, 'completionTime': 4,
                                                      'priorityIndex':9, 'timeLock' : 'True' ,'deadline': 5,
                                                      'postponable': 'False','postponments':0, 'scheduled':'False'},
                                'event1' : {'name': 'blah blah blah','startTime':0, 'completionTime': 0,
                                                          'priorityIndex':10, 'timeLock' : 'False' ,'deadline': 0,
                                                          'postponable': 'True','postponments':2, 'scheduled':'False'},
                                'event2' : {'name': 'haina satr time hii','startTime':0, 'completionTime': 0,
                                                          'priorityIndex':10, 'timeLock' : 'False' ,'deadline': 0,
                                                          'postponable': 'False','postponments':5,
                                                          'scheduled':'False'},
                                'event3' : {'name': 'yes yes','startTime':0, 'completionTime': 0,
                                                          'priorityIndex':7, 'timeLock' : 'True' ,'deadline': 4,
                                                          'postponable': 'False','postponments':5,
                                                          'scheduled':'False'},
                                'event4' : {'name': 'testName1','startTime':5, 'completionTime': 6,
                                                          'priorityIndex':6, 'timeLock' : 'True' ,'deadline': 4,
                                                          'postponable': 'False','postponments':5, 'duration':2,
                                                          'scheduled':'False'},
                                'event5'  : {'name': 'testName2','startTime':0, 'completionTime': 0,
                                                          'priorityIndex':5, 'timeLock' : 'True' ,'deadline': 4,
                                                          'postponable': 'False','postponments':5, 'duration':2,
                                                          'scheduled':'False'}}
#effectors ... these read the environment...for which case is our event consideredNextEventDictionary
    def eventIsTimeStamped(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        #value 0 means we have no deadline
        if eventDictionaryToConsider['startTime'] > 0:
            return True
        else:
            return False
    def eventHasDeadline(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        #value 0 means we have no deadline
        if eventDictionaryToConsider['deadline'] > 0:
            return True
        else:
            return False
    def eventHasBeenPostponed(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        #value 0 means we have never postponed it
        if eventDictionaryToConsider['postponments'] > 0:
            return True
        else:
            return False


    def isEventIsPostponable(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        if eventDictionaryToConsider['postponable'] == "True":
            return True
        else:
            return False

    def getEventname(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        return eventDictionaryToConsider['name']
    def getEventStartTime(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        return eventDictionaryToConsider['startTime']

    def getEventCompletionTime(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        return eventDictionaryToConsider['completionTime']

    def getEventDuration(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        print eventDictionaryToConsider['startTime'] - eventDictionaryToConsider['completionTime']

    def getEventPriorityIndex(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        return eventDictionaryToConsider['priorityIndex']
    def eventHasBeenScheduled(self,eventDictionaryToConsider):
        eventDictionaryToConsider = eventDictionaryToConsider
        if eventDictionaryToConsider['postponable'] == "True":
            return True
        else:
            return False

#actions
    def makeEventScheduled(self,eventDictionaryToConsider,startTime):
        eventDictionaryToConsider = eventDictionaryToConsider
        eventDictionaryToConsider['scheduled'] == True

    def giveEventAStartTime(self,eventDictionaryToConsider,startTime):
        eventDictionaryToConsider = eventDictionaryToConsider
        eventDictionaryToConsider['startTime'] == startTime

    def giveEventAnEndTime(self,eventDictionaryToConsider,completionTime):
        eventDictionaryToConsider = eventDictionaryToConsider
        eventDictionaryToConsider['completionTime'] == completionTime

#rules
    def scheduleEvents(self):
        #is the event having time stamps ... schedule this
        self.scheduledEventsDict = {}
        countTimeStampedEvents = 0
        for events in self.todayEventDict:
            if self.eventIsTimeStamped(self.todayEventDict[events]):
               self.giveEventAStartTime(self.todayEventDict[events],self.todayEventDict[events]['startTime'])
               self.scheduledEventsDict = self.todayEventDict[events]
               print self.scheduledEventsDict
               countTimeStampedEvents = countTimeStampedEvents + 1


    def getPriorityDIctionary(self,eventDictionaryToConsider):

    # getting next event
        #this will hold the nxt event dictionary
        self.nextEvent={}
    #1should come from a tuple of today's activities
        self.nextEventDict= self.todayEventDict
        priorityIndex=0

    #timestamp first

    # 2 should have the highest priorityIndex
        #this one gets possible candidates for nextEventDict according to priority ranking
        for priority in self.nextEventDict:
            eventNumber=0
            priorityIndex = self.nextEventDict[priority]['priorityIndex']
            if (int(priorityIndex) >= int(self.currentConsideredpriorityIndex)):
                    eventname="eventNumber"+str(eventNumber)
                    self.consideredNextEventDictionary[eventname]['name']=self.nextEventDict[priority]['name']
                    self.consideredNextEventDictionary[eventname]['startTime']=self.nextEventDict[priority]['startTime']
                    self.consideredNextEventDictionary[eventname]['completionTime']=self.nextEventDict[priority]['completionTime']
                    self.consideredNextEventDictionary[eventname]['priorityIndex']=self.nextEventDict[priority]['priorityIndex']
                    eventNumber = eventNumber+1
                    print self.consideredNextEventDictionary[eventname]['name']



    def startAnEvent(self):
        ticks = time.time()
        self.currentStateTask['name'] = raw_input("Enter name of the event");
        self.currentStateTask['startTime'] = time.asctime(ticks)
        eventDuration=input("Enter duration: ");


        print startTime

        self.currentStateTask['startTime'] = input("Enter a startTime: ");
        durationtime = input("Enter duration: ");
        self.currentStateTask['completionTime'] = input("Enter a startTime: ");

    def test(self):
        self.getEventDuration(self.currentStateTask)

def main():
    object=MyAssistant()
    object.scheduleEvents()
main()
