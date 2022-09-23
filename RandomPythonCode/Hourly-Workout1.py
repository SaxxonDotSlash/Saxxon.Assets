import time

currenttime = time.ctime()
starttime = "Sat Aug 29 12:05:00 2020"



def start_increasing_workout():
    print("Start time: %s" % time.ctime())
    print("Please do 1 lap around yard, and 10 push ups, sit ups, jumping jacks, and pull ups.")
    while 1==1:
        if currenttime == "Sat Aug 12 1:00:00 2020":
            print("Time is: %s" % time.ctime())
            print("Please do 2 laps around yard, and 20 push ups, sit ups, jumping jacks, and pull ups.")
            while 1==1:
                if currenttime == "Sat Aug 12 2:00:00 2020":
                    print("Time is: %s" % time.ctime())
                    print("Please do 3 laps around yard, and 30 push ups, sit ups, jumping jacks, and pull ups.")
                    while 1==1:
                        if currenttime == "Sat Aug 12 3:00:00 2020":
                            print("Time is: %s" % time.ctime())
                            print("Please do 4 laps around yard, and 40 push ups, sit ups, jumping jacks, and pull ups.")
                            while 1==1:
                                if currenttime == "Sat Aug 12 4:00:00 2020":
                                    print("Time is: %s " % time.ctime())
                                    print("Please do 5 laps around yard, and 50 push ups, sit ups, jumping jacks, and pull ups.")
                                    while 1==1:
                                        if currenttime == "Sat Aug 12 5:00:00 2020":
                                            print("Time is: %s" % time.ctime())
                                            print("Please do 4 laps around yard, and 40 push ups, sit ups, jumping jacks, and pull ups.")
                                            while 1==1:
                                                if currenttime == "Sat Aug 12 6:00:00 2020":
                                                    print("Time is: %s" % time.ctime())
                                                    print("Please do 3 laps around yard, and 30 push ups, sit ups, jumping jacks, and pull ups.")
                                                    while 1==1:
                                                        if currenttime == "Sat Aug 12 7:00:00 2020":
                                                            print("Time is: %s" % time.ctime())
                                                            print("Please do 2 laps around yard, and 20 push ups, sit ups, jumping jacks, and pull ups.")
                                                            while 1==1:
                                                                if currenttime == "Sat Aug 12 8:00:00 2020":
                                                                    print("Time is: %s" % time.ctime())
                                                                    print("Please do 1 lap around yard, and 10 push ups, sit ups, jumping jacks, and pull ups.")
                                                                    print("Congrats! You've finished the Increasing Hourly Workout Program. Have A Nice Day!")



def countup():
    print("Start time: %s" % time.ctime())

#countup()
while 1==1:
    if starttime == time.ctime():
        start_increasing_workout()
