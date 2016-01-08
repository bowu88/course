# -*- coding:utf-8 -*-
import queue
import re
import threading
import time
from course.mr_login import mr_login
from course.mr_show import mr_show

class ThreadClass(threading.Thread):
    def __init__(self,qe,show):
        threading.Thread.__init__(self)
        self.qe = qe
        self.show=show
    def run(self):
        while True:
            qid=self.qe.get()
            self.show.choseClass(qid)
            self.qe.task_done()

def main():
    mrlogin=mr_login()
    if mrlogin.door():
        print('login successfully!')
        mrshow =mr_show()
        mrshow.choseClass()
        '''qe=queue.Queue()
        for i in range(1):
            t = ThreadClass(qe,mrshow)
            t.setDaemon(True)
            t.start()
        for i in range(1):
            qe.put(i)
        qe.join()'''
if __name__=='__main__':
    st=time.time()
    main()
    print('总用时间','%f'%(time.time()-st))


    