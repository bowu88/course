# -*- coding:utf-8 -*-
import queue
import re
import threading
import time
from course.mr_login import mr_login
from course.mr_show import mr_show
from course.mr_select import mr_select


def main():
    mrlogin=mr_login()
    if mrlogin.door():
        #mrshow=mr_show()
        #print(mrshow.showClass())
        mrselect=mr_select('\327\324\310\273\277\306\321\247')#people cuture
        mrselect.door()
if __name__=='__main__':
    st=time.time()
    main()
    print('总用时间','%f'%(time.time()-st))


    