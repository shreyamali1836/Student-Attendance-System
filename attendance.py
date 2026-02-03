from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Attendance System")

        # *******************variable*******************
        self.var_attend_id=StringVar() 
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_department=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()


        img=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\bg4.png")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="HOSTEL ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1500,height=700)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=660)

        img_left=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\banner1.jpg")
        img_left=img_left.resize((755,180))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=755,height=180)

        img_left1=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\banner.jpg")
        img_left1=img_left1.resize((755,180))
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)

        f_lbl=Label(left_frame,image=self.photoimg_left1)
        f_lbl.place(x=0,y=450,width=755,height=180)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=195,width=755,height=250)

        # **********label and entry*************
        # attendance ID
        attendance_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll
        roll_label=Label(left_inside_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # department
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_department,font=("times new roman",13,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance
        attendance_label=Label(left_inside_frame,text="Attendance status:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)

        self.attendance_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",13,"bold"),width=19,state="readonly")
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3,column=1,pady=8)
        

         # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=750,height=100)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,width=24,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,width=24,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",width=24,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)

        Year_data=Button(btn_frame,text="Yearly Data",command=self.open_year,width=24,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Year_data.grid(row=1,column=0)


        Year_label=Label(btn_frame,text="                                               Year:",font=("times new roman",13,"bold"),bg="white")
        Year_label.grid(row=2,column=0,sticky=W)

        Year_entry=ttk.Entry(btn_frame,width=24,font=("times new roman",13,"bold"))
        Year_entry.grid(row=2,column=1,sticky=W)
        

        Month_data=Button(btn_frame,text="Monthly Data",command=self.open_month,width=24,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Month_data.grid(row=1,column=1)

        self.course_combo=ttk.Combobox(btn_frame,font=("times new roman",13,"bold"),width=24,state="readonly")
        self.course_combo["values"]=("Select Month","January","February","March","April","May","June","July","August","September","October","November","December")
        self.course_combo.current(0)
        self.course_combo.grid(row=2,column=2,sticky=W)

        Daily_data=Button(btn_frame,text="Daily Data",command=self.open_daily,width=24,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Daily_data.grid(row=1,column=2)

        

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=790,y=10,width=690,height=660)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=630)

        # ***********scroll bar table***************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID:")
        self.attendanceReportTable.heading("roll",text="Roll no:")
        self.attendanceReportTable.heading("name",text="Name:")
        self.attendanceReportTable.heading("department",text="Department:")
        self.attendanceReportTable.heading("time",text="Time:")
        self.attendanceReportTable.heading("date",text="Date:")
        self.attendanceReportTable.heading("attendance",text="Attendance:")

        self.attendanceReportTable["show"]="headings"
        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def open_year(self):
        os.startfile(f"Record")

    def open_month(self):
        # seyear=self.Year_entry.get()
        selected_month = self.course_combo.get()
        if selected_month != "Select Month":
            os.startfile(f"Record\Year\{selected_month}")
        else:
            messagebox.showwarning("Selection Error", "Please select a valid month.")


    def open_daily(self):
        os.startfile("Record\Year\Month\Daily")

    # *****************fetch data****************
    def fetchdata(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root,)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    
    # ***********export csv************
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO data","No data found to export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root,)
            with open(fin,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data is exported "+os.path.basename(fin)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

    def get_cursor(self,event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_department.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])


            
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_department.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
