t1 = td.thread1(target=task1,name='t1')
t2 = td.thread1(target=task2,name='t2')
t1.start()
print("\n")
t2.start()
t1.join()
t2.join()