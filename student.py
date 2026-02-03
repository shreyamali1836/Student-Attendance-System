from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")


        # ===============variables=====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # bg img
        img=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\bg3.jpg")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="HOSTEL ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1500,height=700)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=660)

        img_left=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\reg1.png")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=755,height=130)

        # current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=5,y=135,width=740,height=140)

        
        # course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","Diploma","Degree")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)

        # department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Electrical","Electronics","DDGM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=1,pady=10)

        # year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=1,pady=10,sticky=W)

        # semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","first semester","second semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=1,pady=10,sticky=W)

        # Class student information
        Class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",13,"bold"))
        Class_student_frame.place(x=5,y=280,width=740,height=350)

        
        # student ID
        studentID_label=Label(Class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student Name
        studentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # batch
        class_div_label=Label(Class_student_frame,text="Hostel Name:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        batch_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=19,state="readonly")
        batch_combo["values"]=("Select Hostel","Krushna","Koyana","Warna","kaveri","Godavari","Chandrabhaga","Indrayani")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # roll no
        rollno_label=Label(Class_student_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # gender
        gender_label=Label(Class_student_frame,text="Room Number:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=19,state="readonly")
        gender_combo["values"]=("Select Room Number","G1","G2","G3","G4","G5","G6","F1","F2","F3","F4","F5","F6","F7","F8","S1","S2","S3","S4","S5","S6","S7","S8","T1","T2","T3","T4","T5","T6","T7","T8")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # DOB
        DOB_label=Label(Class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone no
        Phone_label=Label(Class_student_frame,text="Phone no:",font=("times new roman",13,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        Address_label=Label(Class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teachername
        teacher_label=Label(Class_student_frame,text="Warden name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="yes")
        radiobtn1.grid(row=7,column=0)

        # radio button2
        radiobtn2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No a photo sample",value="No")
        radiobtn2.grid(row=7,column=1)

        # button frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=725,height=50)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=270,width=725,height=50)

        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        




        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=790,y=10,width=690,height=660)

        img_right=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\banner1.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #  ================table frame========================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=140,width=680,height=485)


        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)     
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Hostel")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Room No")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Warden name")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ------------------function declaration-------------------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="shreya@1836",database="shreya")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                                ))      
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

    # --------------fetch data----------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="shreya@1836",database="shreya")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


# *********************get cursor************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # **********update function**********
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="shreya@1836",database="shreya")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,batch=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where stdid=%s",(
                                                                                                                                self.var_dep.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_semester.get(),
                                                                                                                                self.var_std_name.get(),
                                                                                                                                self.var_div.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get(),
                                                                                                                                self.var_std_id.get()
                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated!!!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ***************Delete function*******************
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required!!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="shreya@1836",database="shreya")
                    my_cursor=conn.cursor()
                    sql="delete from student where stdid=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)        
            except Exception as es:                
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # *****************reset********************
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_name.set(""),
        self.var_div.set("Select Batch"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        self.var_std_id.set("")

    # ***************generate dataset & take a sample********************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="shreya@1836",database="shreya")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,batch=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where stdid=%s",(
                                                                                                                                self.var_dep.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_semester.get(),
                                                                                                                                self.var_std_name.get(),
                                                                                                                                self.var_div.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get(),
                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ****************load predefined data on face frontal from opencv*********
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully")
            except Exception as es:                
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)








if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()