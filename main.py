from operator import xor
from tarfile import SOLARIS_XHDTYPE
import time
from jdatetime import datetime, timedelta
import random
from time import sleep
from pkg_resources import parse_requirements
import resources
from threading import Thread
import ctypes
from win10toast import ToastNotifier
import xlsxwriter
import time
import random
from time import sleep
import sys
import jdatetime
from fpdf import FPDF
from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QLabel,QTableWidget,QTableWidgetItem,QWidget,QListWidget
import sqlite3
import ntplib
from persiantools.jdatetime import JalaliDate

import os
import sys

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)



connection = sqlite3.connect(application_path+"\\main.db")



les = []#
cel = []#
loginer = []#
examlist = []#
cont = 1#
qclist=[]#
testnum=0
testnum2=0
testnum3=0
list11=[]
scorec=[]
questions=[]
class mainapp(QMainWindow):
    def __init__(self):
        super(mainapp, self).__init__()
        loadUi(application_path+"\\main.ui", self)
 
        self.pages.setCurrentIndex(0)
        self.log_in.clicked.connect(self.getusersinfo)
        self.chng_to_s.clicked.connect(self.changetos)
        self.chng_to_l.clicked.connect(self.changetol)
        self.sign_in.clicked.connect(self.createac)
        self.pushButton.clicked.connect(self.checkact)
        # Exits
        self.e1.clicked.connect(self.exito)
        self.e2.clicked.connect(self.exito)
        # cel10nb
        self.test10.clicked.connect(self.changetot10)
        self.submitinfo.clicked.connect(self.t10info)
        self.t_forward.clicked.connect(self.nxtq)
        self.t_back.clicked.connect(self.bakq)
        self.ex_btn.clicked.connect(self.showq)
        self.ex_btn2.clicked.connect(self.showq2)
        self.submitq.clicked.connect(self.subq)
        self.discoverbtn.clicked.connect(self.see_exames)
        self.ok.clicked.connect(self.see_scores)
        self.search_btn.clicked.connect(self.search_it)
        self.listx.itemDoubleClicked.connect(self.listxdef)
        self.listexam.itemDoubleClicked.connect(self.showthestu)
        self.listexam.itemClicked.connect(self.acti)
        self.searchforex.clicked.connect(self.listexams)
        self.removeexam.clicked.connect(self.remex)
        self.savexl.clicked.connect(self.xl)
        # self.btnnextq2.clicked.connect(self.nxtq)
        self.submitq_2.clicked.connect(self.subq2)
        self.taiidnomreh.clicked.connect(self.updatescore)
        self.label_nmd.clicked.connect(self.back1)
        self.listWidget_2.itemDoubleClicked.connect(self.updateandshow)
        self.taiidnomreh_2.clicked.connect(self.tnomreh)
        self.reload1.clicked.connect(self.reload)
        self.d_forward.clicked.connect(self.nxtq)
        self.btnnextq.clicked.connect(self.t_sabt)
        self.btnnextq2.clicked.connect(self.t_sabt)
        self.d_back.clicked.connect(self.bakq)
        self.test15()
    def test15(self):
        self.frame_84.setVisible(True)
    def getusersinfo(self):


        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        u = self.l_username.text()
        p = self.l_password.text()
        
        cursor.execute("select password from query where username='%s'" % u)
        passw = cursor.fetchone()
        if p == "" and u == "":
            self.l_error.setText("هیچ چیزی را وارد نکرده اید")
        elif u == "":
            self.l_error.setText("نام کاربری را وارد نکرده اید")
        elif p == "":
            self.l_error.setText("رمز عبور را وارد نکرده اید")
        elif u == "":
            self.l_error.setText("نام کاربری را وارد نکرده اید")
        elif passw == None:
            self.l_error.setText("نام کاربری وجود ندارد")
        else:
            passw = passw[0]
            if p == passw:
                cursor.execute("select pos from query where username='%s'" % u)
                posw = cursor.fetchone()
                posw = posw[0]
                if posw == 1:
                    self.pages.setCurrentIndex(2)
                    cursor.execute(
                        "select fname from query where username='%s'" % u)
                    d_fname = cursor.fetchone()
                    d_fname = d_fname[0]
                    self.d_pro.setText(d_fname)
                    loginer.insert(1, u)
                    tread111 = Thread(target=self.welllog)
                    tread111.start()
                    self.l_error.setText("")
                if posw == 2:
                    self.pages.setCurrentIndex(3)
                    cursor.execute(
                        "select fname from query where username='%s'" % u)
                    m_fname = cursor.fetchone()
                    m_fname = m_fname[0]
                    self.m_pro.setText(m_fname)
                    loginer.insert(1, u)
                    tread111 = Thread(target=self.welllog)
                    
                    t1 = str(datetime.now() - timedelta(days=10))
                    t2 = str(datetime.now())
                    
                    t1=((t1.replace("-", "/"))[0:10])
                    t2=((t2.replace("-", "/"))[0:10])
                    self.time1.setText(t1)
                    self.time2.setText(t2)
                    self.searchforex.click()
                    self.discoverbtn.click()
                    self.l_error.setText("")
                       
            
            if p != passw:
                self.l_error.setText("رمز عبور درست نیست")

        connection.commit()
    
    def createac(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        n = self.s_fname.text()
        p = self.s_password.text()
        rep = self.s_password2.text()
        u = self.s_username.text()
        pos1 = self.ch_stu.isChecked()
        pos2 = self.ch_tea.isChecked()

        if u == '' and p == '' and rep == '' and n == '':
            self.s_error.setText("هیچ چیزی وارد نکرده اید")
            return
        elif u == '':
            self.s_error.setText("نام کاربری را وارد نکرده اید")
            return
        elif p == '':
            self.s_error.setText("رمز عبور را وارد نکرده اید")
            return
        elif n == '':
            self.s_error.setText("اسم خود را وارد نکرده اید")
            return
        elif pos1 is False and pos2 is False:
            self.s_error.setText("دانش آنوز هستید یا معلم ؟")
            return
        elif pos1 == True:
            positionn = 1
        elif pos2 == True:
            positionn = 2

        cursor.execute("select username from query where username='%s'" % u)
        res = cursor.fetchone()
        if res is None:
            if p == rep:
                if positionn == 1 or 2:
                    data = (n, u, p, positionn)
                    cursor.execute("insert into query VALUES (?,?,?,?)", data)
                    connection.commit()
                if positionn == 1:
                    self.pages.setCurrentIndex(2)
                    cursor.execute(
                        "select fname from query where username='%s'" % u)
                    d_fname = cursor.fetchone()
                    d_fname = d_fname[0]
                    self.d_pro.setText(d_fname)
                    tread121 = Thread(target=self.wellsign)
                    tread121.start()
                    self.s_error.setText("")
                if positionn == 2:
                    self.pages.setCurrentIndex(3)
                    cursor.execute(
                        "select fname from query where username='%s'" % u)
                    m_fname = cursor.fetchone()
                    connection.commit()
                    m_fname = m_fname[0]
                    self.m_pro.setText(m_fname)
                    data3 = (n, u)
                    cursor.execute("insert into teacher VALUES (?,?)", data3)
                    connection.commit()
                    loginer.append(self.s_username.text())
                    tread121 = Thread(target=self.wellsign)
                    tread121.start()
                    t1 = str(datetime.now() - timedelta(days=10))
                    t2 = str(datetime.now())
                    self.listexams
                    t1=((t1.replace("-", "/"))[0:10])
                    t2=((t2.replace("-", "/"))[0:10])
                    self.time1.setText(t1)
                    self.time2.setText(t2)
                    self.s_error.setText("")
                else:
                    self.s_error.setText("دانش آنوز هستید یا معلم")

            else:
                self.s_error.setText("رمز عبور یکسان نیست")

        else:
            self.s_error.setText("نام کاربری وجود دارد")
        self.s_error.setText("")
        connection.commit()
        
    def welllog(self):
        toaster = ToastNotifier()
        toaster.show_toast("به برنامه خوش آمدید","بانک سوالات و آزمون انلاین")
        
    def wellsign(self):
        toaster = ToastNotifier()
        toaster.show_toast("خوشحالیم که به جمع ما اضافه شدی","بانک سوالات و آزمون انلاین")

    def changetot10(self):
        self.pages.setCurrentIndex(4)
        f = str(datetime.now() + timedelta(days=1))
        s = str(datetime.now())
        s=s.split( )
        s=s[0]
        s=s.replace("-","/")
        f=f.split( )
        f=f[0]
        f=f.replace("-","/")
        self.sdate.setText(s)
        self.fdate.setText(f)
    def t10info(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        global testnum,a,questions,scorec,qclist
        if 1==1:
            xy = self.testnum_btn.currentText()
            xy = xy.replace(" تستی" , "")
            testnum=int(xy)
            e10n = self.examname.text()
            e10g = self.grade.currentText()
            e10ti = (self.timetext.text())
            e10ti=(int(e10ti))*60
            e10doshvari =self.doshvari.currentText()
            e10nowe_azmon = self.nowe_azmon.currentText()
            e10show_score=self.show_score.isChecked()
            t = str(datetime.now())
            Internet_date_and_time=((t.replace("-", ""))[0:8])
            if e10show_score is True:
                e10show_score="t"
            else:
                e10show_score="f"        

            e10use_arzyabi=self.use_arzyabi.isChecked()
            if e10use_arzyabi is True:
                e10use_arzyabi="t"
            else:
                e10use_arzyabi="f"        
            e10tn = loginer
            e10tn = str(e10tn)
            e10tn = e10tn.replace("'", "")
            e10tn = e10tn.replace("[", "")
            e10tn = e10tn.replace("]", "")
            lesy = self.combol.currentText()
            les.clear()
            
            st1 = self.stime.text()
            sd = self.sdate.text()
            ft1 = self.ftime.text()
            fd = self.fdate.text()
            
            st = st1.split(" ")
            ft = ft1.split(" ")
            if str(st[1])=="PM" :
                ui = (str(st[0])).split(":")
                poi=ui[0]
                loi=ui[1]
                poi=int(poi)+12
                st2 = str(poi)+":"+loi
            else:
                st2 = str(st[0])


            if str(ft[1])=="PM" :
                ui = (str(ft[0])).split(":")
                poi=ui[0]
                loi=ui[1]
                poi=int(poi)+12
                ft2 = str(poi)+":"+loi
            else:
                ft2 = str(ft[0])


            st2 = st2.replace(":" , "")
            ft2 = ft2.replace(":" , "")
            if len(st2) == 3:
                st2 = "0" + st2
            else:
                pass
            if len(ft2) == 3:
                ft2 = "0" + ft2
            else:
                pass
            sd = sd.replace("/" , "")
            fd = fd.replace("/" , "")
            start1 = int( sd + st2)
            finish1 = int( fd + ft2)
            
            if e10n=="":
                self.s_error_2.setText("نام آزمون را وارد نکردید")
            elif e10ti=="":
                self.s_error_2.setText("مدت زمان آزمون را وارد نکردید")
            else :
                e10ti = int(e10ti)
                a=""
                xs="jj"
                while xs!=None:
                    a=""
                    for i in range(5):
                        x=str(random.randint(1,9))
                        a=a+x
                    cursor.execute("select code from examten where code='%s'" % (a))
                    xs = cursor.fetchone()
                    connection.commit()
                    
                    if xs is None:
                        discrip = self.descriptive.isChecked()
                        testy = self.test.isChecked()
                        status = "t"
                        noeazmoon = ""
                        
                        if  testy == True:
                            self.codeex.setText(f"کد آزمون  : {a}")
                            noeazmoon = "t"
                            datat10 = (e10n, e10tn, e10ti, e10g, lesy,testnum,e10doshvari,e10nowe_azmon,e10show_score,e10use_arzyabi,a,Internet_date_and_time,start1,finish1,status,noeazmoon)
                            cursor.execute(
                                "insert into examten(examdb,teacherun,time1,grades,lesdb,testnumdb,dif,type,scoretf,arztf,code,datetime,open,close,activate,azmoontype) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datat10)
                            connection.commit()
                            examlist.insert(1, a)
                            self.pages.setCurrentIndex(5)
                            self.etmam_t.setVisible(False)
                            
                            
                            questions=[""]*testnum
                            qclist=[""]*testnum
                            
                        if discrip == True:
                            self.codeex_4.setText(f"کد آزمون  : {a}")
                            noeazmoon = "d"
                            datat10 = (e10n, e10tn, e10ti, e10g, lesy,testnum,e10doshvari,e10nowe_azmon,e10show_score,e10use_arzyabi,a,Internet_date_and_time,start1,finish1,status,noeazmoon)
                            cursor.execute(
                                "insert into examten(examdb,teacherun,time1,grades,lesdb,testnumdb,dif,type,scoretf,arztf,code,datetime,open,close,activate,azmoontype) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datat10)
                            connection.commit()
                            examlist.insert(1, a)
                            self.pages.setCurrentIndex(8)
                            
                            
                            questions=[""]*testnum
                            scorec=[""]*testnum
                        self.etamam_d.setVisible(False)
                        self.d_back_frame.setVisible(False)
                        self.t_back_frame.setVisible(False)
                        self.etmam_t.setVisible(False)




    def nxtq(self):
        self.etamam_d.setVisible(False)
        global cont,qclist,testnum,questions,cel,datajj,scorec
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        cel = examlist[0]
        
        cursor.execute("select azmoontype from examten where code=?",(cel,))
        x = cursor.fetchone()
        x=x[0]
        soorat_t = self.mainq.text()
        gh1 = self.test1.text()
        gh2 = self.test2.text()
        gh3 = self.test3.text()
        gh4 = self.test4.text()
        soorat_d = self.sorat.text()
        tozihat  = self.javab.text()
        score  = self.nomreh.text()
        if soorat_t == "" and gh1 == "" and gh2 == "" and gh3 == "" and gh4 == "" :
            self.t_error.setText("لطفا تمام موارد مورد نیاز را وارد کنید")
        if soorat_d == "" and tozihat == "" and score == "":
            self.d_error.setText("لطفا تمام موارد مورد نیاز را وارد کنید")
        else:
            if 1==1:
                if cont<=testnum:
                    if x=="t":
                        self.t_back_frame.setVisible(True)
                        cel = examlist[0]
                        
                        qxo = self.mainq.text()
                        t1xo = self.test1.text()
                        t2xo = self.test2.text()
                        t3xo = self.test3.text()
                        t4xo = self.test4.text()
                        tcxo = self.ctest.currentText()
                        tcxo=tcxo.replace("گزینه ","")
                        tcxo=tcxo.replace(" ","")
                        datajj = qxo +" ,"+ t1xo +" ,"+ t2xo +" ,"+ t3xo +" ,"+ t4xo +" ,"+ tcxo
                        
                        
                        questions[cont-1]=datajj
                        
                        qclist[cont-1]=tcxo
                
                        self.mainq.setText("")
                        self.test1.setText("")
                        self.test2.setText("")
                        self.test3.setText("")
                        self.test4.setText("")
                        if cont!=testnum:
                            self.qnum_label.setText(f"{cont+1}/{testnum}")
    
                        cont +=1
            
                        iiii=questions[cont-1]
                        if iiii!="":
                            iiii=iiii.split(",")
                            self.mainq.setText(iiii[0])
                            self.test1.setText(iiii[1])
                            self.test2.setText(iiii[2])
                            self.test3.setText(iiii[3])
                            self.test4.setText(iiii[4])
                        
                        if cont==(int(testnum)):
                            
                            self.etmam_t.setVisible(True)
                            self.t_forward_frame.setVisible(False)

                    else:
                        self.d_back_frame.setVisible(True)
                        cel = examlist[0]
                        

                        nqc = self.nomreh.text()
                        jqc = self.javab.text()
                        sqc = self.sorat.text()
                        datajjj = sqc + " ," + jqc
                        questions[cont-1]=datajjj
                        
                        scorec[cont-1]=nqc
                        
                        
                        
                        qclist.append(jqc)
                        self.nomreh.setText("")
                        self.javab.setText("")
                        self.sorat.setText("")
                        if cont!=testnum:
                            self.qnum_label2.setText(f"{cont+1}/{testnum}")
    
                        cont +=1
            
                        iiii=questions[cont-1]
                        oooo=scorec[cont-1]
                        if iiii!="":
                            iiii=iiii.split(",")
                            self.nomreh.setText(oooo)
                            self.sorat.setText(iiii[0])
                            self.javab.setText(iiii[1])
                    
                        
                        if cont==(int(testnum)):
                            
                            self.etamam_d.setVisible(True)
                            self.d_forward_frame.setVisible(False)
                    
                connection.commit()  
    def t_sabt(self):
        
        self.examname.setText("")
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        global cont,qclist,testnum,questions,cel,datajj,scorec
        cursor.execute("select azmoontype from examten where code=?",(cel,))
        x = cursor.fetchone()
        x=x[0]
        if x == "t":
            qxo = self.mainq.text()
            t1xo = self.test1.text()
            t2xo = self.test2.text()
            t3xo = self.test3.text()
            t4xo = self.test4.text() 
            tcxo = self.ctest.currentText()
            tcxo = tcxo.replace("گزینه" , "")
            
            qclist[cont-1]=tcxo
            
            
            qclist2=str(qclist)
            qclist2=qclist2.replace("'", "")
            qclist2=qclist2.replace("[", "")
            qclist2=qclist2.replace("]", "")
            qclist2=qclist2.replace(" ", "")
            qclist2 = str(qclist2)
            
            cursor.execute("""
            UPDATE examten SET qc=? where code=?                       
            """ ,  (qclist2 ,cel))
            y = 0
            for i in questions:
                y = y+1
                s = i
                s = s.split(",")
                x = s[0:5]
                x = str(x)
                x=x.replace("'", "")
                x=x.replace("[", "")
                x=x.replace("]", "")
                
                cursor.execute(f"""
                UPDATE examten SET q{y}=? where code=?
                """ , (x,cel))
                
                datajjj = qxo +" ,"+ t1xo +" ,"+ t2xo +" ,"+ t3xo +" ,"+ t4xo +" ,"+ tcxo
                questions[cont-1] = datajjj
         

                connection.commit()

            connection.commit()
            
            ctypes.windll.user32.MessageBoxW(0," آزمون با موفقیت ساخته شد ", f"کد آزمون  : {a}", 1)
            cont=0
            self.qnum_label.setText((f"1/{testnum}"))
            time.sleep(2)
            self.pages.setCurrentIndex(3)
            examlist.clear()
            cont=1
            qclist.clear()
            testnum=0
            
            self.t_back_frame.setVisible(False)
            self.t_forward_frame.setVisible(True)
        else:

            nqc = self.nomreh.text()
            jqc = self.javab.text()
            sqc = self.sorat.text()
            scorec[cont-1]=nqc
            y = 0
            for i in questions:
                y = y+1
                s = i
                s = s.split(",")
                x = s[0:3]
                x = str(x)
                x=x.replace("'", "")
                x=x.replace("[", "")
                x=x.replace("]", "")
                
                cursor.execute(f"""
                UPDATE examten SET q{y}=? where code=?
                """ , (x,cel))
                
                datajjjj = sqc +" ,"+ jqc 
                questions[cont-1] = datajjjj
                connection.commit()
            connection.commit()
            scorec = str(scorec)
            scorec=scorec.replace("'", "")
            scorec=scorec.replace("[", "")
            scorec=scorec.replace("]", "")
            scorec=scorec.replace(" ", "")
            cursor.execute(f"""
            UPDATE examten SET score=? where code=?
            """ , ((scorec),cel))  
            connection.commit()  
            
            ctypes.windll.user32.MessageBoxW(0," آزمون با موفقیت ساخته شد ", f"کد آزمون  : {a}", 1)
            cont=0
            self.qnum_label.setText((f"1/{testnum}"))
            time.sleep(2)
            self.pages.setCurrentIndex(3)
            
            examlist.clear()
            cont=1
            qclist.clear()
            testnum=0
            
            self.d_back_frame.setVisible(False)
            self.d_forward_frame.setVisible(True)

                  
    def bakq(self):
        self.etamam_d.setVisible(False)
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        cel = examlist[0]
        
        global cont,qclist,testnum,questions,scorec
        cursor.execute("select azmoontype from examten where code=?",(cel,))
        x = cursor.fetchone()
        x=x[0]
        if 1==1:
            if cont<=testnum:
                if x=="t":

                    self.t_forward_frame.setVisible(True)
                    cel = examlist[0]
                    
                    qxo = self.mainq.text()
                    t1xo = self.test1.text()
                    t2xo = self.test2.text()
                    t3xo = self.test3.text()
                    t4xo = self.test4.text() 
                    tcxo = self.ctest.currentText()
                    tcxo=tcxo.replace("گزینه ","")
                    tcxo=tcxo.replace(" ","")
                    datajj = qxo +" ,"+ t1xo +" ,"+ t2xo +" ,"+ t3xo +" ,"+ t4xo +" ,"+ tcxo
                    
                    
                    questions[cont-1]=datajj
                    
                    cont -=1
                    iiii=questions[cont-1]
                   
                    self.mainq.setText("")
                    self.test1.setText("")
                    self.test2.setText("")
                    self.test3.setText("")
                    self.test4.setText("")
                    
                    if iiii!="":
                        iiii=iiii.split(",")
                        self.mainq.setText(iiii[0])
                        self.test1.setText(iiii[1])
                        self.test2.setText(iiii[2])
                        self.test3.setText(iiii[3])
                        self.test4.setText(iiii[4])
                    qclist[cont-1]=tcxo


                    if cont!=testnum:
                        self.qnum_label.setText(f"{cont}/{testnum}")
                    
                    
                    if cont==1:
                        
                        
                        self.t_back_frame.setVisible(False)
                else:
                    self.d_forward_frame.setVisible(True)
                    cel = examlist[0]
                    
                    nqc = self.nomreh.text()
                    jqc = self.javab.text()
                    sqc = self.sorat.text()
                    datajjjjj =  sqc +" ,"+ jqc
                    
                    questions[cont-1]=datajjjjj
                    scorec[cont-1]=nqc
                    cont -=1
                    iiii=questions[cont-1]
                    oooo=scorec[cont-1]
                     
                    self.nomreh.setText("")
                    self.javab.setText("")
                    self.sorat.setText("")
                    if iiii!="":
                        iiii=iiii.split(",")
                        self.nomreh.setText(oooo)
                        self.sorat.setText(iiii[0])
                        self.javab.setText(iiii[1])
                    

                    if cont!=testnum:
                        self.qnum_label2.setText(f"{cont}/{testnum}")
                    
                    
                    if cont==1:
                        
                        
                        self.d_back_frame.setVisible(False)
                


                    
    def showq(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()


        self.ex_show.setText("")
        self.label_5.setText("")
        global testnum2,testnum3,cel676
        
        cursor.execute("select code from examten where code='%s'" % (self.ex_n.text()))
        test121 = cursor.fetchone()
        connection.commit()
        cel676=""
        
        if test121 is not None:
            cursor.execute(f"select open from examten where code={self.ex_n.text()}")
            start1 = int((cursor.fetchone())[0])
            cursor.execute(f"select close from examten where code={self.ex_n.text()}")
            close1 = int((cursor.fetchone())[0])
            ss = jdatetime.datetime.today()
            ii = ((str(ss))[0:10])
            ii = ii.replace("-" , "")
            tt = ((str(ss))[11:17])
            tt = tt.replace(":" , "")
            neww = ii + tt
            now = int(neww)
            
           
            
            if start1<=now and close1>now : 
                cursor.execute("select forcheck from answer where forcheck='%s'" % ((self.ex_n.text())+loginer[0]))
                cel676 = cursor.fetchone()
                connection.commit()
                
                cursor.execute("select activate from examten where code=?" , ((self.ex_n.text()),))
                active = cursor.fetchone()
                active = active[0]
                
                if cel676 == None and active == "t":

                    ex_n_in=self.ex_n.text()
                    ex_n_in=str(ex_n_in)
                    cursor.execute("select * from examten where code=?",(ex_n_in,))
                    all1 = cursor.fetchall()
                    
                    connection.commit()
                    all1=str(all1)
                    all1=all1.replace("'", "")
                    all1=all1.replace("[", "")
                    all1=all1.replace("]", "")
                    all1=all1.replace("(", "")
                    all1=all1.replace(")", "")
                    all2=all1.split(",")
                    text=f"""طراح آزمون : {all2[1]}
مدت زمان آزمون : {all2[2]}
تعداد سوالات :{all2[5]}
پایه : {all2[3]}
                    """
                    self.ex_show.setText(text)
                    self.label_5.setText(f"آزمون مورد نظر با نام {all2[0]} یافت شد")
                    


                elif active == "f":
                    self.label_5.setText("آزمون فعال نیست")
                else:
                    self.label_5.setText("شما به این ازمون پاسخ دادید")  
            else:
                self.label_5.setText("این آزمون هنوز شروع نشده است یا پایان یافته")  
        else:
            self.label_5.setText("آزمونی با این کد وجود ندارد")  
      
        testnum3=testnum2
        connection.commit()

    def showq2(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        global arzyabi,testnum3,testnum2,cude
        testnum3=testnum2
        if (self.ex_n.text())=="":
            self.ex_show.setText("شما کد را وارد و تایید نکردید !")
        else:
            cursor.execute(f"select open from examten where code={self.ex_n.text()}")
            start1 = int((cursor.fetchone())[0])
            cursor.execute(f"select close from examten where code={self.ex_n.text()}")
            close1 = int((cursor.fetchone())[0])
            ss = jdatetime.datetime.today()
            ii = ((str(ss))[0:10])
            ii = ii.replace("-" , "")
            tt = ((str(ss))[11:17])
            tt = tt.replace(":" , "")
            neww = ii + tt
            now = int(neww)

            cursor.execute(f"select azmoontype from examten where code={self.ex_n.text()}")
            typ = cursor.fetchone()
            typ =typ[0]
            if start1<=now and close1>now : 
                if cel676 is None:
                    if typ == "t":
                        arzyabi="f"
                        
                        ex_n_in=self.ex_n.text()
                        ex_n_in=str(ex_n_in)
                        cude=ex_n_in
                        connection.commit()
                        cursor.execute(("select examdb from examten where code=?"),(ex_n_in,))
                        exname = cursor.fetchone()
                        exname=exname[0]            
                        self.label_e.setText(exname)
                        self.pages.setCurrentIndex(6)
                        cursor.execute("select testnumdb from examten where code=?",(ex_n_in,))
                        testnum2 = cursor.fetchone()
                        connection.commit()
                        testnum2=testnum2[0]
                        testnum2=int(testnum2)
                        co=testnum2
                        for iiii in range(40-testnum2):
                            co=co+1
                            eval("self.ft_"+(str(co))+".setVisible(False)")
                        for iiii in range(40):
                            eval("self.fd_"+(str(iiii+1))+".setVisible(False)")
                        for cont2 in range(0,testnum2):
                            cont3=cont2+1
                            cursor.execute((f"select q{cont3} from examten where code=?"),(ex_n_in,))
                            
                            XD = cursor.fetchone()
                            connection.commit()
                            XD = XD[0]


                            XD = XD.split(",")
                            XE=cont2+1
                            
                            XF=" "+"سوال"+f"{XE}"+")"+" "
                            eval("self.q_"+str(cont3)+".setText(XF+XD[0])")
                            eval("self.t1_"+str(cont3)+".setText(XD[1])")
                            eval("self.t2_"+str(cont3)+".setText(XD[2])")
                            eval("self.t3_"+str(cont3)+".setText(XD[3])")
                            eval("self.t4_"+str(cont3)+".setText(XD[4])")
                        global ti,th,examcode
                        cursor.execute("select time1 from examten where code=?", (ex_n_in,))
                        ti=cursor.fetchone()
                        connection.commit()
                        ti=ti[0]
                        cursor.execute("select close from examten where code=?", (ex_n_in,))
                        close1=cursor.fetchone()
                        close1=str(close1[0])
                        connection.commit()
                        now = datetime.now()
                        now1 = now.strftime("%Y %m %d %H %M")
                        now1 = now1.split(" ")
                        a = datetime((int(now1[0])),(int(now1[1])),(int(now1[2])),(int(now1[3])),(int(now1[4])), 00)
                        b = datetime((int(close1[0:4])), (int(close1[4:6])), (int(close1[6:8])), (int(close1[8:10])), (int(close1[10:12])), 00)
                        c=b-a
                        minutes = int(c.total_seconds() / 60)
                        
                        examcode=ex_n_in
                        if (minutes*60)>ti:
                            ti=int(ti)
                        else:
                            ti=minutes*60
                        th = Thread(target=self.timer_1)
                        th.start()
                    elif typ == "d":
                        arzyabi="f"
                        
                        ex_n_in=self.ex_n.text()
                        ex_n_in=str(ex_n_in)
                        cude=ex_n_in
                        connection.commit()
                        cursor.execute(("select examdb from examten where code=?"),(ex_n_in,))
                        exname = cursor.fetchone()
                        exname=exname[0]            
                        self.label_e.setText(exname)
                        self.pages.setCurrentIndex(6)
                        cursor.execute("select testnumdb from examten where code=?",(ex_n_in,))
                        testnum2 = cursor.fetchone()
                        connection.commit()
                        testnum2=testnum2[0]
                        testnum2=int(testnum2)
                        co=testnum2
                        
                        for iiii in range(40-testnum2):
                            co=co+1
                            eval("self.fd_"+(str(co))+".setVisible(False)")
                        for iiii in range(40):
                            eval("self.ft_"+(str(iiii+1))+".setVisible(False)")
                        for cont2 in range(0,testnum2):
                            cont3=cont2+1
                            cursor.execute((f"select q{cont3} from examten where code=?"),(ex_n_in,))
                            XD = cursor.fetchone()
                            connection.commit()
                            XD = XD[0]
                            cursor.execute((f"select score from examten where code=?"),(ex_n_in,))
                            rr = cursor.fetchone()
                            rr = rr[0]
                            rr=rr.split(",")
                            rr=rr[cont2]
                            
                            XD = XD.split(",")
                            XE=cont2+1
                            XF=" "+"سوال"+f"{XE}"+")"+" "
                            eval("self.qt_"+str(cont3)+".setText(XF+XD[0]+' ( '+rr+' نمره )')")
                        
                        cursor.execute("select time1 from examten where code=?", (ex_n_in,))
                        ti=cursor.fetchone()
                        connection.commit()
                        ti=ti[0]
                        cursor.execute("select close from examten where code=?", (ex_n_in,))
                        close1=cursor.fetchone()
                        close1=str(close1[0])
                        connection.commit()
                        now = datetime.now()
                        now1 = now.strftime("%Y %m %d %H %M")
                        now1 = now1.split(" ")
                        a = datetime((int(now1[0])),(int(now1[1])),(int(now1[2])),(int(now1[3])),(int(now1[4])), 00)
                        b = datetime((int(close1[0:4])), (int(close1[4:6])), (int(close1[6:8])), (int(close1[8:10])), (int(close1[10:12])), 00)
                        c=b-a
                        minutes = int(c.total_seconds() / 60)
                        
                        examcode=ex_n_in
                        if (minutes*60)>ti:
                            ti=int(ti)
                        else:
                            ti=minutes*60
                        th = Thread(target=self.timer_1)
                        th.start()
                        

                else:
                    print(cel676)

        connection.commit()

    def timer_1(self):
        global examissubmited 
        examissubmited=False
        time_sec=ti
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat ="زمان باقی مانده : "+ """{:02d}:{:02d}
""".format(mins, secs)
            self.showtime.setText(str(timeformat))
            time.sleep(1)
            time_sec -= 1
            if examissubmited==True:
                break
        if examissubmited!=True:
            self.subq()



    def subq(self):
        global examissubmited 
        examissubmited=True
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        global arzyabi,testnum3,testnum2
        if arzyabi=="f":
            cursor.execute((f"select azmoontype from examten where code=?"),(cude,))
            lili= cursor.fetchone()
            lili=lili[0]
            
            if lili=="t":
                qqq=[]
                
                testnum3=testnum2
                for i in range(0,int(testnum3)):
                    if eval("self.t1_"+str(i+1)+".isChecked()") is True:
                        qqq.append("1")
                    elif eval("self.t2_"+str(i+1)+".isChecked()") is True:
                        qqq.append("2")
                    elif eval("self.t3_"+str(i+1)+".isChecked()") is True:
                        qqq.append("3")
                    elif eval("self.t4_"+str(i+1)+".isChecked()") is True:
                        qqq.append("4")
                    else:
                        qqq.append("n")
                qqqx=str(qqq)
                scorestu=0
                
                cursor.execute(("select qc from examten where code=?"),(examcode,))
                testc_ans = cursor.fetchone()
                connection.commit()
                testc_ans = testc_ans[0]
                c_ans=testc_ans.split(",")
                
                for i in range(0,testnum3):
                    if qqq[i]==c_ans[i]:
                        scorestu+=1
                scorestu=(scorestu*20)/testnum3
                qqqx = qqqx.replace("'", "")
                qqqx = qqqx.replace("[", "")
                qqqx = qqqx.replace("]", "")
                qqqx = qqqx.replace(" ", "")
                dato12 = ((str(examcode)+loginer[0]),examcode , (loginer[0]),qqqx,scorestu)
                cursor.execute(("insert into answer VALUES (?,?,?,?,?)"),(dato12))
                connection.commit()
                for i in range(0,int(testnum3)):
                    eval("self.q_"+str(i+1)+".setText('')")
                    eval("self.t1_"+str(i+1)+".setChecked(False)")
                    eval("self.t2_"+str(i+1)+".setChecked(False)")
                    eval("self.t3_"+str(i+1)+".setChecked(False)")
                    eval("self.t4_"+str(i+1)+".setChecked(False)")
                    eval("self.t1_"+str(i+1)+".setText('')")
                    eval("self.t2_"+str(i+1)+".setText('')")
                    eval("self.t3_"+str(i+1)+".setText('')")
                    eval("self.t4_"+str(i+1)+".setText('')")
                self.ex_n.setText('')
                self.ex_show.setText('')
                self.showtime.setText('00:00')
                cursor.execute(("select scoretf from examten where code=?"),(examcode,))
                scoretf = cursor.fetchone()
                connection.commit()
                

                if scoretf[0]=="t":
                    ctypes.windll.user32.MessageBoxW(0,(f"نمره ی شما : {scorestu} از 20"), ("پاسخ شما با موفقیت ثبت شد"), 1)
                if scoretf[0]=="f":
                    ctypes.windll.user32.MessageBoxW(0,("موفق باشید"), ("پاسخ شما با موفقیت ثبت شد"), 1)
                for iiii in range(40):
                    eval("self.fd_"+(str(iiii+1))+".setVisible(True)")
                    eval("self.ft_"+(str(iiii+1))+".setVisible(True)")
                self.pages.setCurrentIndex(2)
                testnum2=0
                testnum3=0

            
            if lili=="d":
                qqq=[]
                
                testnum3=testnum2
                for i in range(0,int(testnum3)):
                    ioi=eval("self.qa_"+str(i+1)+".text()")
                    qqq.append(ioi)
                qqqx=str(qqq)
                scorestu=0
                
                qqqx = qqqx.replace("'", "")
                qqqx = qqqx.replace("[", "")
                qqqx = qqqx.replace("]", "")
                dato12 = ((str(examcode)+loginer[0]),examcode , (loginer[0]),qqqx,)
                cursor.execute(("insert into answer(forcheck,exam_cc,stu_cc,ans_cc) VALUES (?,?,?,?)"),(dato12))
                connection.commit()
                for i in range(0,int(testnum3)):
                    eval("self.qt_"+str(i+1)+".setText('')")
                    eval("self.qa_"+str(i+1)+".setText('')")
                self.ex_n.setText('')
                self.ex_show.setText('')
                self.showtime.setText('00:00')
                ctypes.windll.user32.MessageBoxW(0,("موفق باشید"), ("پاسخ شما با موفقیت ثبت شد"), 1)
                for iiii in range(40):
                    eval("self.fd_"+(str(iiii+1))+".setVisible(True)")
                    eval("self.ft_"+(str(iiii+1))+".setVisible(True)")
                self.pages.setCurrentIndex(2)
                testnum2=0
                testnum3=0

            
        else:
            qqq=[]
            
            
            for i in range(0,int(testnum3)):
                if eval("self.t1_"+str(i+1)+".isChecked()") is True:
                    qqq.append("1")
                elif eval("self.t2_"+str(i+1)+".isChecked()") is True:
                    qqq.append("2")
                elif eval("self.t3_"+str(i+1)+".isChecked()") is True:
                    qqq.append("3")
                elif eval("self.t4_"+str(i+1)+".isChecked()") is True:
                    qqq.append("4")
                else:
                    qqq.append("n")
            qqqx=str(qqq)
            scorestu=0
            
            cursor.execute(("select qc from examten where code=?"),(examcode,))
            testc_ans = cursor.fetchone()
            connection.commit()
            testc_ans = testc_ans[0]
            c_ans=testc_ans.split(",")
            
            for i in range(0,testnum3):
                if qqq[i]==c_ans[i]:
                    scorestu+=1
            scorestu=(scorestu*20)/testnum3
            qqqx = qqqx.replace("'", "")
            qqqx = qqqx.replace("[", "")
            qqqx = qqqx.replace("]", "")
            qqqx = qqqx.replace(" ", "")
            for i in range(0,int(testnum3)):
                eval("self.q_"+str(i+1)+".setText('')")
                eval("self.t1_"+str(i+1)+".setChecked(False)")
                eval("self.t2_"+str(i+1)+".setChecked(False)")
                eval("self.t3_"+str(i+1)+".setChecked(False)")
                eval("self.t4_"+str(i+1)+".setChecked(False)")
                eval("self.t1_"+str(i+1)+".setText('')")
                eval("self.t2_"+str(i+1)+".setText('')")
                eval("self.t3_"+str(i+1)+".setText('')")
                eval("self.t4_"+str(i+1)+".setText('')")
            self.showtime.setText('00:00')
            ctypes.windll.user32.MessageBoxW(0,(f"""نمره ی شما : {scorestu} از 20
                                                نتیجه به صورت فایل پی-دی-اف ذخیره شد"""), ("پاسخ شما با موفقیت ثبت شد"), 1)
            self.pages.setCurrentIndex(2)
            testnum2=0
            testnum3=0
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('eunjin', '', application_path+'\\DejaVuSansCondensed.ttf', uni=True)
            pdf.set_font('eunjin', '', 20)
            pdf.write(8, u'exam maker')
            pdf.ln(20)
            f="exam code : "+examcode+""""
student : """
            f=f+loginer[0]+"""

"""
            
            for i in range(len(qqq)):
                f=f+f"test{i+1} : "+f"Right answer : {c_ans[i]}"+"   "+f"Your answer : {qqq[i]}" +"""
"""
            
 
            pdf.add_font('Arial', '', 'DejaVuSansCondensed.ttf', uni=True) 
            pdf.set_font("Arial", size = 15)
            f=f.splitlines()
            for x in f:
            	pdf.cell(10, 6, txt = x, ln = 1, align = 'a')
            time1=(str(datetime.now()))
            time1=time1.replace(" ","--")
            time1=time1.replace(":",";")

            pdf.output(f"خود_ارزیابی{time1}.pdf")
            for iiii in range(40):
                eval("self.fd_"+(str(iiii+1))+".setVisible(True)")
                eval("self.ft_"+(str(iiii+1))+".setVisible(True)")
        connection.commit()
    def subq2(self):
        global examissubmited 
        examissubmited=True
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        global arzyabi,testnum3,testnum2
        if arzyabi=="f":
            qqq=[]
            
            testnum3=testnum2
            for i in range(0,int(testnum3)):
                ioi=eval("self.qa"+str(i+1)+".text()")
                qqq.append(ioi)
            qqqx=str(qqq)
            scorestu=0
            
            qqqx = qqqx.replace("'", "")
            qqqx = qqqx.replace("[", "")
            qqqx = qqqx.replace("]", "")
            dato12 = ((str(examcode)+loginer[0]),examcode , (loginer[0]),qqqx,)
            cursor.execute(("insert into answer(forcheck,exam_cc,stu_cc,ans_cc) VALUES (?,?,?,?)"),(dato12))
            connection.commit()
            for i in range(0,int(testnum3)):
                eval("self.qa"+str(i+1)+".setText('')")
                eval("self.qd"+str(i+1)+".setText('')")
            self.ex_n.setText('')
            self.ex_show.setText('')
            self.showtime_2.setText('00:00')
            ctypes.windll.user32.MessageBoxW(0,("موفق باشید"), ("پاسخ شما با موفقیت ثبت شد"), 1)
            self.pages.setCurrentIndex(2)
            testnum2=0
            testnum3=0

        
    def see_exames(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        self.comboexam.clear()
        cursor.execute(("select * from examten where teacherun=?"),(loginer[0],))
        oko = cursor.fetchall()
        oko = oko[::-1]
        for i in range(len(oko)):
            self.comboexam.addItem((oko[i])[0]+"   "+str((oko[i])[10]))
    def see_scores(self):
        try:
            connection = sqlite3.connect("main.db")
            cursor = connection.cursor()
            cursor.execute(("select * from examten where teacherun=?"),(loginer[0],))
            exams = cursor.fetchall()
            exams = exams[::-1]
            self.tableexam.clear()
            self.tableexam.setHorizontalHeaderLabels(["دانش آموز", "نمره", "پاسخ ها"])
            c_exam=self.comboexam.currentIndex()
            c_exam=int((exams[c_exam])[10])
            cursor.execute(("select * from answer where exam_cc=?"),(c_exam,))
            oko= cursor.fetchall()
            oko = oko[::-1]
            pkl=0
            cursor.execute("select stu_cc from answer where exam_cc=?",(c_exam,))
            ono = cursor.fetchall()
            ono = ono[::-1]
            self.tableexam.setRowCount(len(ono))
            for row in oko:
                self.tableexam.setItem(pkl , 0, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableexam.setItem(pkl , 1, QtWidgets.QTableWidgetItem((str(row[4])+"از 20")))
                gio=(str(row[3]).replace("n", "بدون پاسخ"))
                gio2=gio.split(",")
                gio3=[]
                cursor.execute("select testnumdb from examten where code=?",(c_exam,))
                testnum3 = cursor.fetchone()
                testnum3=testnum3[0]
                testnum3=int(testnum3)
                for i in range(0,testnum3):
                    
                    if gio2[i]=="1" or "2" or "3" or "4":
                        i2=i+1
                        hii=("گزینه "+gio2[i])
                        gio3.append(f"سوال{i2}: "+hii)
                    else:
                        i2=i+1
                        gio3.append(f"سوال{i2}: "+gio2[i])
                gio3 = str(gio3)
                gio3 = gio3.replace("'", "")
                gio3 = gio3.replace("[", "")
                gio3 = gio3.replace("]", "")
                gio3 = gio3.replace(",", " | ")
                self.tableexam.setItem(pkl , 2,QtWidgets.QTableWidgetItem(str(gio3)))
                pkl+=1  
            connection.commit()
        except:
            pass
        
    def search_it(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        self.listx.clear()
        tedad_alan = self.testnum_btn_2.currentText()
        darsaye_m = self.darsaye_mor.currentText()
        n_azmoon = self.nowe_azmon_2.currentText()
        d_azmoon = self.doshvari_2.currentText()
        grade=self.grade_2.currentText()

        removesimi=0
        if tedad_alan != "همه":
            tedad_alan1=" and testnumdb=?"
            tedad_alan2=tedad_alan
        else:
            tedad_alan1=""
            tedad_alan2=""
            removesimi +=1
            
        if grade != "همه":
            grade1=" and grades=?"
            grade2=grade
        else:
            grade1=""
            grade2=""
            removesimi +=1
            
        if darsaye_m != "همه":
            darsaye_m1=" and lesdb=?"
            darsaye_m2=darsaye_m
        else:
            darsaye_m1=""
            darsaye_m2=""
            removesimi +=1
            
            
        if d_azmoon != "همه":
            d_azmoon1=" and dif=?"
            d_azmoon2=d_azmoon
            
        else:
            d_azmoon1=""
            d_azmoon2=""
            removesimi +=1
            
            
        if n_azmoon != "همه":
            n_azmoon1=" and type=?"
            n_azmoon2=n_azmoon
        else:
            n_azmoon1=""
            n_azmoon2=""
            removesimi +=1
            

        data=("t" + "," + tedad_alan2 + "," + darsaye_m2 + "," + d_azmoon2 + "," + n_azmoon2+","+grade2)
        data=data.replace(",,,,,", ",")
        data=data.replace(",,,,", ",")
        data=data.replace(",,,", ",")
        data=data.replace(",,", ",")
        if data[-1]==",":
            data = data.rstrip(data[-1])
            
        global li
        
        data=data.split(",")
        data=tuple(data)
        
        now = datetime.now()
        now1 = now.strftime("%Y %m %d %H %M")
        now1=now1.replace(" ","")
        cursor.execute(f"select * from examten where close<{now1} and azmoontype='t' and activate='t' and arztf=?{tedad_alan1}{darsaye_m1}{d_azmoon1}{n_azmoon1}{grade1}",data)
        hasel = cursor.fetchall()
        li=[]
        if len(hasel)!=0:
            for i in range(len(hasel)):
                xn=str(((hasel[i])[0]))
                size=" "*(35-(len(xn)))
                xn=xn+(size)
                self.listx.addItem("  نام ازمون : "+xn+"     "+str(((hasel[i])[3]))+"  |  "+str(((hasel[i])[4]))+" | سواله"+str(((hasel[i])[5]))+"  |  "+str(((hasel[i])[6]))+"  |  "+str(((hasel[i])[7])))
                li.append(str(((hasel[i])[10])))
        else:
            print("mio")
        connection.commit()
            
    def listxdef(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()

        global examcode,testnum3,testnum2,arzyabi
        x=self.listx.currentRow()
        examcode=li[x]
        examcode=str(examcode)
        cursor.execute(("select examdb from examten where code=?"),(examcode,))
        exname = cursor.fetchone()
        exname=exname[0]     
        self.label_e.setText(exname)
        self.pages.setCurrentIndex(6)
        cursor.execute("select testnumdb from examten where code=?",(examcode,))
        testnum2 = cursor.fetchone()
        connection.commit()
        testnum2=testnum2[0]
        testnum2=int(testnum2)
        testnum3=testnum2
        co=testnum2
        for iiii in range(40-testnum2):
            co=co+1
            eval("self.ft_"+(str(co))+".setVisible(False)")
        for iiii in range(40):
            eval("self.fd_"+(str(iiii+1))+".setVisible(False)")
        for cont2 in range(0,testnum2):
            cont3=cont2+1
            cursor.execute((f"select q{cont3} from examten where code=?"),(examcode,))
            XD = cursor.fetchone()
            connection.commit()
            XD = XD[0]
            XD = str(XD)

            XD = XD.split(",")
            eval("self.q_"+str(cont3)+".setText(XD[0])")
            eval("self.t1_"+str(cont3)+".setText(XD[1])")
            eval("self.t2_"+str(cont3)+".setText(XD[2])")
            eval("self.t3_"+str(cont3)+".setText(XD[3])")
            eval("self.t4_"+str(cont3)+".setText(XD[4])")
        self.showtime.setText("")
        arzyabi="t"
        connection.commit()
    def listexams(self):
        list11.clear()
        self.listexam.clear()

        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        t1=self.time1.text()
        t2=self.time2.text()
        t1=(t1.replace("/",""))
        yy=int(t1[0:4])
        mm=int(t1[4:6])
        dd=int(t1[6:8])
        x=jdatetime.datetime(yy, mm, dd, 16, 53, 26, 558957)
        t1=(x - timedelta(days=1))
        t1=((str(t1))[0:10])
        t1=int(t1.replace("-",""))
        t2=(t2.replace("/",""))
        yy=int(t2[0:4])
        mm=int(t2[4:6])
        dd=int(t2[6:8])
        x=jdatetime.datetime(yy, mm, dd, 16, 53, 26, 558957)
        t2=(x + timedelta(days=1))
        t2=((str(t2))[0:10])
        t2=int(t2.replace("-",""))
        cursor.execute(f"select * from examten where teacherun=? and datetime>{t1} and datetime<{t2}",(loginer[0],))
        XXX = cursor.fetchall() 
        for i in range(len(XXX)):
            self.listexam.addItem(((XXX[i])[0])+"   "+str((XXX[i])[10]))
            list11.append((XXX[i])[10])
        
        
    def remex(self):
        if len(list11)!=0:
            connection = sqlite3.connect("main.db")
            cursor = connection.cursor()
            x=(self.listexam.currentRow())
            x=int(x)
            xx=list11[x]
            cursor.execute(("delete from examten where code=?"),(xx,))
            cursor.execute(("delete from answer where exam_cc=?"),(xx,))
            connection.commit()
            self.listexams()
        
    def acti(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        click = self.listexam.currentItem().text()
        click = click.split("   ")
        cc = click[1]
        cursor.execute("select activate from examten where code=?" , (cc,))
        cs = cursor.fetchone()
        cs = cs[0]
        if cs == "t":
            self.pushButton.setText(" غیر فعال کردن")
            connection.commit()
        elif cs == "f":
            self.pushButton.setText("فعال کردن")
            connection.commit()
        else: 
            pass
    def xl(self):
        
        try:  
            if len(list11)!=0:
                connection = sqlite3.connect("main.db")
                cursor = connection.cursor()
                xl_ex=(self.listexam.currentItem().text())
                xl_ex=xl_ex.split("   ")
                xl_ex=xl_ex[1]
                cursor.execute("select * from answer where exam_cc=?",(xl_ex,))
                XXX = cursor.fetchall() 
                now = datetime.now()
                dt_string = now.strftime("%d-%m-%Y_%H;%M;%S")
                workbook = xlsxwriter.Workbook(f'exam_{xl_ex}({dt_string}).xlsx')
                worksheet = workbook.add_worksheet()
                expenses = []
                for i in range(len(XXX))  :
                    x=[((XXX[i])[2]),((XXX[i])[4]),((XXX[i])[3])]
                    expenses.append(x)
                expenses=tuple(expenses)
                row = 0
                col = 0
                for i in range(len(expenses)):
                    worksheet.write(row, col,     ((expenses[i])[0]))
                    worksheet.write(row, col + 1, ((expenses[i])[1]))
                    worksheet.write(row, col + 2, ((expenses[i])[2]))
                    row += 1
                workbook.close()
                connection.commit()
        except:
            pass

    def checkact(self):
        try:
            connection = sqlite3.connect("main.db")
            cursor = connection.cursor()
            click = self.listexam.currentItem().text()
            click = click.split("   ")
            cc = click[1]
            cursor.execute("select activate from examten where code=?" , (cc,))
            cs = cursor.fetchone()
            cs = cs[0]
            if cs == "t":
                self.pushButton.setText(" فعال کردن")
                cursor.execute("update examten set activate='f' where code=?", (cc,))
                connection.commit()
            elif cs == "f":
                self.pushButton.setText("غیر فعال کردن")
                cursor.execute("update examten set activate='t' where code=?", (cc,))
                connection.commit()
            else: 
                pass
        except:
            pass
    def keyPressEvent(self, event):
        try:
            if self.pages.currentIndex() == 0:
                if event.key() == 16777220:
                    self.log_in.click()
                else:
                    pass
            if self.pages.currentIndex() == 1:
                if event.key() == 16777220:
                    self.sign_in.click()
                else:
                    pass
            if self.pages.currentIndex() == 2:
                if self.stu.currentIndex() == 1:
                    if event.key() == 16777220:
                        self.ex_btn.click()
                    else:
                        pass
                elif self.stu.currentIndex() == 2:
                    if event.key() == 16777220:
                        self.search_btn.click()
                    else:
                        pass
            if self.pages.currentIndex() == 3:
                if self.stu.currentIndex() == 1:
                    if event.key() == 16777220:
                        self.teacher.click()
                    else:
                        pass
                elif self.stu.currentIndex() == 2:
                    if event.key() == 16777220:
                        self.ok.click()
                    else:
                        pass
                elif self.stu.currentIndex() == 3:
                    if event.key() == 16777220:
                        self.searchforex.click()
                    else:
                        pass
        except:
            pass
    def changetos(self):
        self.pages.setCurrentIndex(1)

    def changetol(self):
        self.pages.setCurrentIndex(0)

    def exito(self):
        self.pages.setCurrentIndex(0)
        loginer.clear()
        self.l_password.setText("")
        self.l_username.setText("")
        self.s_fname.setText("")
        self.s_username.setText("")
        self.s_password.setText("")
        self.s_password2.setText("")
        self.ch_tea.setChecked(False)
        self.ch_stu.setChecked(False)
    def showthestu(self):
        global llll
        llll=[]
        self.pages.setCurrentIndex(9)
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        x=(self.listexam.currentRow())
        x=int(x)
        xx=list11[x]
        self.label_15.setText(str(xx))
        cursor.execute("select examdb from examten where code=?",(xx,))
        p = cursor.fetchone()
        self.exex.setText(p[0])
        cursor.execute(("select * from answer where exam_cc=?"),(xx,))
        ans=cursor.fetchall()
        for i in range((len(ans))):
            cursor.execute(("select fname from query where username=?"),(((ans[i])[2]),))
            n=cursor.fetchone()
            n=n[0]
            if (ans[i])[4]=="":
                o="بدون نمره"
            else:
                o=(ans[i])[4]

            self.listWidget_2.addItem(f"{n} : {o}")
            llll.append([((ans[i])[1]),((ans[i])[2])])
        connection.commit()
        self.listexams()
        connection.commit()
    def updateandshow(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        o=self.listWidget_2.currentRow()

        x=(self.listWidget_2.currentRow())
        x=int(x)
        xx=(llll[x])[0]
        cursor.execute("select azmoontype from examten where code=?",(xx,))
        xxx = cursor.fetchone()
        xxx=xxx[0]




        
        global student,examcodw
        if xxx == "t":
            self.pages.setCurrentIndex(10)
            examcodw = (llll[o])[0]
            student = (llll[o])[1]
            cursor.execute((f"select fname from query where username=?"),(student,))
            self.namestu.setText((cursor.fetchone())[0])
            cursor.execute((f"select examdb from examten where code=?"),(examcodw,))
            self.nameexam.setText((cursor.fetchone())[0])
            cursor.execute((f"select sco_cc from answer where stu_cc=? and exam_cc=?"),(student,examcodw,))
            self.lineEdit.setText(f"{(cursor.fetchone())[0]}/20")
            cursor.execute((f"select testnumdb from examten where code=?"),(examcodw,))
            h = cursor.fetchone()
            h=h[0]
            co=h
            for iiii in range(40-h):
                co=co+1
                eval("self.dd_"+(str(co))+".setVisible(False)")
            for cont2 in range(0,h):
                        cont3=cont2+1
                        cursor.execute((f"select q{cont3} from examten where code=?"),(examcodw,))
                        KD = cursor.fetchone()
                        connection.commit()
                        KD = KD[0]

                        KD = KD.split(",")
                        eval("self.st_"+str(cont3)+".setText(KD[0])")
            ooo=[examcodw,student]
            cursor.execute((f"select ans_cc from answer where exam_cc=? and stu_cc=?"),(ooo))
            ress = cursor.fetchone()
            ress = ress[0]
            ress = ress.split(",")
            for mm in range(len(ress)):
                u = mm+1
                eval("self.sa_"+str(u)+".setText(ress[mm])")
        elif xxx == "d":
            self.pages.setCurrentIndex(11)
            examcodw = (llll[o])[0]
            student = (llll[o])[1]
            cursor.execute((f"select fname from query where username=?"),(student,))
            self.namestu_2.setText((cursor.fetchone())[0])
            cursor.execute((f"select examdb from examten where code=?"),(examcodw,))
            self.nameexam_2.setText((cursor.fetchone())[0])
            cursor.execute((f"select sco_cc from answer where stu_cc=? and exam_cc=?"),(student,examcodw,))
            self.labol.setText(f"{(cursor.fetchone())[0]}/20")
            cursor.execute((f"select testnumdb from examten where code=?"),(examcodw,))
            h = cursor.fetchone()
            h=h[0]
            co=h
            for iiii in range(40-h):
                co=co+1
                eval("self.yy_"+(str(co))+".setVisible(False)")
            for cont2 in range(0,h):
                        cursor.execute((f"select score from examten where code=?"),(examcodw,))
                        rr = cursor.fetchone()
                        rr = rr[0]
                        rr=rr.split(",")
                        rr=rr[cont2]
                        cont3=cont2+1
                        cursor.execute((f"select q{cont3} from examten where code=?"),(examcodw,))
                        KD = cursor.fetchone()
                        connection.commit()
                        KD = KD[0]

                        KD = KD.split(",")
                        eval("self.yt_"+str(cont3)+".setText(KD[0]+' ( '+rr+' نمره )')")
            ooo=[examcodw,student]
            cursor.execute((f"select ans_cc from answer where exam_cc=? and stu_cc=?"),(ooo))
            ress = cursor.fetchone()
            ress = ress[0]
            ress = ress.split(",")
            for mm in range(len(ress)):
                u = mm+1
                eval("self.ya_"+str(u)+".setText(ress[mm])")
        else:
            print("N")

    def updatescore(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        x = self.lineEdit.text()
        if x == "":
            
            ctypes.windll.user32.MessageBoxW(0,"چیزی وارد نشده است !", "خطا", 1)
        else:
            t = x.split("/")
            z = t[0]
            y = t[1]
            if z!="" and y!="":
                y = float(y)
                z = float(z)
                if z == y or z<=y:
                    result = float(z*20)
                    res = float(result/y)
                    
                    xxx = examcodw
                    yy = student
                    ooo=[res,xxx,yy]
                    cursor.execute((f"update answer set sco_cc=? where exam_cc=? and stu_cc=?"),(ooo))
                    connection.commit()
                    self.pages.setCurrentIndex(9)
                    for iiii in range(40):
                        eval("self.dd_"+(str(iiii+1))+".setVisible(True)")
                else:
                   
                    ctypes.windll.user32.MessageBoxW(0,"عدد وارد شده بزرگ تر از 20 است !", "خطا", 1)
                    
    def tnomreh(self):
        connection = sqlite3.connect("main.db")
        cursor = connection.cursor()
        cursor.execute("select testnumdb from examten where code=?",(examcodw,))
        tstnum = cursor.fetchone()
        tstnum = tstnum [0]
        res = 0
        
        for i in range(tstnum):
            
            opo=eval("self.ys_"+str(i+1)+".text()")
            if opo != "":
                res=res+float(opo)
               
            else:
                print("input was 'Nothing'")
        for i in range(40):
            eval("self.ys_"+str(i+1)+".setText('')")
        if res > 20:
            res = 20
        xxx = examcodw
        yy = student
        ooo=[res,xxx,yy]
        cursor.execute((f"update answer set sco_cc=? where exam_cc=? and stu_cc=?"),(ooo))
        connection.commit()
        self.pages.setCurrentIndex(9)
        for iiii in range(40):
            eval("self.dd_"+(str(iiii+1))+".setVisible(True)")
        self.pages.setCurrentIndex(9)
            
    def reload(self):
        res=0
        for i in range(40):
            
            opo=eval("self.ys_"+str(i+1)+".text()")
            if opo != "":
                res=res+float(opo)
                
            else:
                print("input was 'Nothing'")
        if res > 20:
            res = 20
        self.labol.setText(str(res)+"/20")
    def back1(self):
        self.pages.setCurrentIndex(3)
        self.listWidget_2.clear()


app = QApplication(sys.argv)
calculator_app = mainapp()
calculator_app.show()
sys.exit(app.exec_())