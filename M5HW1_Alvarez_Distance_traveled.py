
# A program to show far was driven based off the speed and time
# CTI 110
# M5HW1
# Brittani Alvarez

def main():
    
    
    # making sure distance, speed and time start at 0

    distance = 0
    speed = 0.0
    time = 0.0

    # have speed entered
    
    speed = float(input('Enter the speed in mph: '))

    # time entered

    time = int(float(input('Enter how many hours you where driving: ')))
        
    # show distance traveled 

    print ('Hours \t Distance Traveled')
    print ('__________________________')
        
   
     #counting loop                 
    for hour in range(1, time + 1):
            distance = hour * speed
            print (hour, '\t' , distance)

                      
main()
