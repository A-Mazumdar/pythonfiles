import random

year = 2017

month = 1

day31=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

day30=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

day28=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

next=[]
x=0
y=0

def nextday(dins,mahs,saal):
    
    if mahs in [1,3,5,7,8,10,12]:

        if mahs != 12:
            
            if dins[0] == 31:
                 next.append("{}/{}/{}".format(1,mahs+1,saal))
    
            if dins[1] == 31 :
                 next.append("{}/{}/{}".format(1,mahs+1,saal))

            if dins[2] == 31 :
                 next.append("{}/{}/{}".format(1,mahs+1,saal))


        if mahs == 12:
            if dins[0] == 31:
                 next.append("{}/{}/{}".format(1,1,saal+1))
    
            if dins[1] == 31 :
                 next.append("{}/{}/{}".format(1,1,saal+1))

            if dins[2] == 31 :
                 next.append("{}/{}/{}".format(1,1,saal+1))

    else:

          next.append("{}/{}/{}".format((dins[0]+1),mahs,saal))
          next.append("{}/{}/{}".format((dins[1]+1),mahs,saal))
          next.append("{}/{}/{}".format((dins[2]+1),mahs,saal))
            

    if mahs in [2,4,6,9,11]:

            if mahs == 2:
                
                if dins[0] == 28:
                     next.append("{}/{}/{}".format(1,1,saal+1))
    
                if dins[1] == 28:
                     next.append("{}/{}/{}".format(1,1,saal+1))

                if dins[2] == 28 :
                     next.append("{}/{}/{}".format(1,1,saal+1))

        
            if dins[0] == 31:
                 next.append("{}/{}/{}".format(1,mahs+1,saal))

            if dins[1] == 31 :
                 next.append("{}/{}/{}".format(1,mahs+1,saal))

            if dins[2] == 31 :
                 next.append("{}/{}/{}".format(1,mahs+1,saal))

        
    else:
          next.append("{}/{}/{}".format((dins[0]+1),mahs,saal))
          next.append("{}/{}/{}".format((dins[1]+1),mahs,saal))
          next.append("{}/{}/{}".format((dins[2]+1),mahs,saal))
           


def printnext():
    print("XXXXXXXXXXXXXXXXnew lineXXXXXXXX")
    for jack in next:
        print (jack)


            


def main():
    
    x=0
    year = 2017

    month = 1

    day31=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    day30=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    day28=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    
    while  x<38:

        if month == 13:
            month = 1
            year+=1

        if month in [1,3,5,7,8,10,12]:
        
            day1,day2,day3 = random.sample(day31, 3)
            tray = [day1,day2,day3]
            tray.sort()
    

        if month in [2,4,6,9,11]:
            day1,day2,day3 = random.sample(day28, 3)
            tray = [day1,day2,day3]
            tray.sort()


        
        print("{}/{}/{}".format(tray[0],month,year))
        print("{}/{}/{}".format(tray[1],month,year))
        print("{}/{}/{}".format(tray[2],month,year))
        nextday(tray,month,year)

        tray=[]
        
        x= x+1
        month+=1


    printnext()

main()
    
