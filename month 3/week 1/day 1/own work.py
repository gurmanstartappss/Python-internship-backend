# import threading 
# import time

# def task(name,n):
#     print(f"{threading.current_thread().name} {name} started")
#     time.sleep(n)
#     print(f"{threading.current_thread().name} {name} finished")
    
# t1=threading.Thread(target=task,args=("Gurman",4),name="worker 1")
# t2=threading.Thread(target=task,args=("Avantika",7),name="worker 2")
# t3=threading.Thread(target=task,args=("YO",2),name="worker 3")

# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

# #q1
# import threading 
# import time 

# def yo():
#     print(f"Thread 1:{threading.current_thread().name}")
#     time.sleep(2)
    
# t1=threading.Thread(target=yo,name="Thread 1")
# t2=threading.Thread(target=yo,name="Thread 2")
# t3=threading.Thread(target=yo,name="Thread 3")
# t4=threading.Thread(target=yo,name="Thread 4")
# t5=threading.Thread(target=yo,name="Thread 5")

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

#q2

import threading 
import time 

def yo(n):
    print(f"Square of {threading.current_thread().name}: {n*n}")
    time.sleep(2)
    
t1=threading.Thread(target=yo,args=(1,),name="1")
t2=threading.Thread(target=yo,args=(2,),name="2")
t3=threading.Thread(target=yo,args=(3,),name="3")
t4=threading.Thread(target=yo,args=(4,),name="4")
t5=threading.Thread(target=yo,args=(5,),name="5")
t6=threading.Thread(target=yo,args=(6,),name="6")
t7=threading.Thread(target=yo,args=(7,),name="7")
t8=threading.Thread(target=yo,args=(8,),name="8")
t9=threading.Thread(target=yo,args=(9,),name="9")
t10=threading.Thread(target=yo,args=(10,),name="10")




t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()