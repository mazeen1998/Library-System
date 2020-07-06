from tkinter import *
from tkinter import messagebox
from datetime import date,timedelta,datetime
import sqlite3
#c=sqlite3.connect('Library.db')
#print('db created')
#c.execute('''CREATE TABLE student (ID int primary key not null,
#name text not null,pending real)''' )
#c.execute('''CREATE TABLE books(bID int primary key not null,
#	bname text not null,price real)''')
#c.execute('''CREATE TABLE sbooks(ID int primary key not null,
#bID int not null,Idate char not null,
#Rdate char not null,fine real)'''

#print('Database tb created')
#c.commit()
#c.close()
def cb1():
	w1=Tk()
	w1.title('Books list')
	w1.geometry('450x300')
	c=sqlite3.connect('Library.db')
	books=c.execute('select * from books')
	# c.execute(SELECT * from books)
	# print(books)
	r=1
	l1=Label(w1,text='The available books are given below',bg='yellow',font=('Ariel Bold',20)).grid(ipadx=1.5)
	for i in books:
		bk= 'Book ID :'+ str(i[0]) +'\t' +'Book Name :'+ str(i[1]) + '\n'
		print(bk)
		l1=Label(w1,text=bk).grid(row=r,column=0)
		r+=1
	c.close()

def entry():
	c=sqlite3.connect('Library.db')
	m=c.cursor()
	s=m.execute('select bID from sbooks')
	r=s.fetchall()
	s1=m.execute('select * from books where bID ='+e1.get())
	r2=s1.fetchall()
	r1=int(e1.get()),
	r3=r2[0][1]
	print(r3)
	if r1 in r:
			# global ID
			# ID=date.today()
			# RD=date.now()+timedelta(30).datetime.isoformat()
			l2=Label(w2,text="Sorry, The book " + r2[0][1] +" is already barrowed").grid()
			l2=Label(w2,text=r2[0][1],bg='yellow',font=(20)).grid(ipadx=10)
			# l2=Label(w2,text='This book is barrowed on %s and should be returned by %s'%(ID,RD),font=(16)).grid()
			# books.remove(e1.get())
			# b1.config(w2,status=DISABLED) 
	elif int(e1.get())==r2[0][0]:
		l2=Label(w2,text='The book %s is available to barrow'%(r2[0][1])).grid()
		l2=Label(w2,text='The book should be returned within 30 days of isuue').grid()
	else:
		messagebox.showinfo('Message','No such book is available')
	e1.delete(0,END)
	c.close()

def entry3():
	try:
		global e4
		c=sqlite3.connect('Library.db')
		c.execute('''INSERT INTO books
			values(:bid ,:bname ,:p)''',
			{
			'bid':e3.get(),
			'bname':e4.get(),
			'p':e6.get()
			})
		print('Data inserted')
		c.commit()
		c.close()
		AD=date.today().isoformat()
		l2=Label(w4,text="Hello! " + e4.get()+" is added").grid(columnspan=2)
		l2=Label(w4,text=e4.get(),bg='yellow',font=(20)).grid(ipadx=10,columnspan=2)
		l2=Label(w4,text='The book %s is added to the library on %s'%(e4.get(),AD),font=(16)).grid(columnspan=2)
		e3.delete(0,END)
		e4.delete(0,END)
		e6.delete(0,END)
	except:
		messagebox.showinfo('Message','Book already available')
		e3.delete(0,END)
		e4.delete(0,END)
		e6.delete(0,END)
	
def entry4():
	global e3
	global e4
	try:
		c=sqlite3.connect('Library.db')
		books=c.execute('DELETE from books where bID ='+ e3.get())
		l=Label(w4,text='%s is deleted'%(e4.get())).grid(columnspan=2)
		c.commit()
		c.close()
	except:
		messagebox.showinfo('Message',"Such a book doesn't exist")
def entry5():
	try:
		c=sqlite3.connect('Library.db')
		c.execute('''INSERT INTO student(ID,name)
			values(:sid ,:sname)''',
			{
			'sid':e7.get(),
			'sname':e8.get(),
			})
		print('Data inserted')
		c.commit()
		c.close()
		l2=Label(w6,text=e8.get(),bg='yellow',font=(20)).grid(ipadx=10,columnspan=2)
		l2=Label(w6,text='The student %s is now registered to the library'%(e8.get()),font=(16)).grid(columnspan=2)
		e7.delete(0,END)
		e8.delete(0,END)
	except:
		messagebox.showinfo('Message','Student already registered')
		e7.delete(0,END)
		e8.delete(0,END)
def entry6():
	global e5
	global e7
	try:
		c=sqlite3.connect('Library.db')
		books=c.execute('DELETE from sbooks where bID ='+ e5.get())
		l=Label(w5,text='%s is successfully returned'%(e7.get())).grid(columnspan=2)
		print('success')
		c.commit()
		c.close()
	except:
		messagebox.showinfo('Message',"Such a Book hasen't been lended")
def entry7():
	global e10
	global e9
	global w3
	global e11
	c=sqlite3.connect('Library.db')
	s=c.execute('select bID from books')
	r1=s.fetchall()
	s1=c.execute('select ID from student')
	r2=s1.fetchall()
	s2=c.execute('select ID from sbooks where ID='+e10.get())
	r3=s2.fetchall()
	r4=len(r3)
	b1=int(e9.get()),
	b2=int(e10.get()),
	# print(r1)
	# print(r2)
	print(r3)
	print(r4)
	# print(b1)
	# print(b2)
	if b1 in r1 and b2 in r2 and r4<2: 
		# c.execute('begin')
		try:
			Id=date.today()
			Rd=date.today()+timedelta(30)
			c.execute('''insert into sbooks (ID,bID,Idate,Rdate)
				values(:a,:b,:c,:d)''',
				{
				'a':e10.get(),
				'b':e9.get(),
				'c':Id,
				'd':Rd,
				})
			c.commit()
			l=Label(w3,text='''The book %s has been barrowed on %s and should be returned
				by %s'''%(e11.get(),Id,Rd)).grid(columnspan=2)
			print('Data Inserted')
		except:
		# 	print('Data not inserted')
			l=Label(w3,text='Book already barrowed').grid(columnspan=2)
		# 	c.execute('rollback')
	if r4>3:
		l1=Label(w3,text='The user %s has already barrowed 3 books'%e10.get()).grid(columnspan=2)
	if b1 not in r1 and b2 in r2:
		messagebox.showinfo('Message','Invalid Book ID')
	if b1 not in r1 and b2 not in r2:
		messagebox.showinfo('Message','Invalid Student ID \\ Book ID')
	c.close()
def entry8():
	global w4
	global e3
	c=sqlite3.connect('Library.db')
	c1=c.cursor()
	sbook=c1.execute('select * from sbooks where bID ='+e3.get())
	r3=sbook.fetchall()
	for i in r3:
		s='Student ID : '+ str(i[0]) +'|| Issue Date : '+ str(i[2])+'|| Return Date : '+ str(i[3])+'\n'
		# print(s)
		l=Label(w4,text=s).grid(pady=1,columnspan=2)
	c.close()
def entry9():
	global e7
	global w6
	try:
		c=sqlite3.connect('Library.db')
		c1=c.cursor()
		sID=c1.execute('delete * from student where ID ='+e7.get())
		c1.commit()
		c.close()
	except:
		messagebox.showinfo('Message','Incorrect Student ID')
def entry10():
	global e7
	global w6
	c=sqlite3.connect('Library.db')
	c1=c.cursor()
	sID=c1.execute('select * from sbooks where ID ='+e7.get())
	r=sID.fetchall()
	for i in r:
		s='Book ID ID : '+ str(i[1]) +'|| Issue Date : '+ str(i[2])+'|| Return Date : '+ str(i[3])+'\n'
		# print(s)
		l=Label(w6,text=s).grid(pady=1)
	c.close()


def cb2():
	global w2
	# global l2
	global e1
	w2=Toplevel()
	w2.title('Search Books')
	w2.geometry('700x300')
	l2=Label(w2,text="Enter the book ID",font=(16)).grid()
	e1=Entry(w2,width=20)
	e1.grid(row=2,column=0)
	e1.insert(0,'Type here')
	global b1	
	b1=Button(w2,text='Search',relief=GROOVE,command=entry)
	b1.grid()
	# w2.bind(b1,entry())
def cb3():
	global w3
	global e10
	global e9
	global e11
	w3=Toplevel()
	w3.geometry('700x300')
	w3.title('Lend Book')
	l3=Label(w3,text="Enter the details",font=(16)).grid()
	e10=Entry(w3,width=20)
	e10.grid(row=2,column=1)
	l4=Label(w3,text="Book ID").grid(row=1,column=0)
	l4=Label(w3,text="Student ID").grid(row=2,column=0)
	l4=Label(w3,text="Book Name").grid(row=3,column=0)
	e9=Entry(w3,width=20)
	e9.grid(row=1,column=1)
	e11=Entry(w3,width=20)
	e11.grid(row=3,column=1)
	b3=Button(w3,text='Lend Book',relief=GROOVE,command=entry7)
	b3.grid(row=4,columnspan=2)	
	
def cb4():
	global w4
	global e3
	global e4
	global e6
	w4=Toplevel()
	w4.geometry('700x300')
	w4.title('Manage Book')
	l4=Label(w4,text="Book Details",font=(16)).grid(row=0,column=0,columnspan=2)
	l4=Label(w4,text="Book ID").grid(row=1,column=0)
	l4=Label(w4,text="Book Name").grid(row=2,column=0)
	l4=Label(w4,text="Book Price").grid(row=3,column=0)
	e3=Entry(w4,width=20)
	e3.grid(row=1,column=1)
	# e3.insert(0,'Type here')
	e4=Entry(w4,width=20)
	e4.grid(row=2,column=1)
	e6=Entry(w4,width=20)
	e6.grid(row=3,column=1)
	global b3	
	b3=Button(w4,text='Add',relief=GROOVE,command=entry3)
	b3.grid(row=4,columnspan=2)
	l4=Label(w4,text="Just enter Book ID for deleting/checking a book").grid(row=5,columnspan=2)
	b3=Button(w4,text='Delete',relief=GROOVE,command=entry4)
	b3.grid(row=6,columnspan=2)
	b3=Button(w4,text='Check',relief=GROOVE,command=entry8)
	b3.grid(row=7,columnspan=2)
def cb5():
	global e5
	global w5
	global e7
	w5=Toplevel()
	w5.geometry('700x300')
	w5.title('Return Book')
	l4=Label(w5,text="Book Details",font=(16)).grid(row=0,column=0,columnspan=2)
	l4=Label(w5,text="Book ID").grid(row=1,column=0)
	l4=Label(w5,text="Book Name").grid(row=2,column=0)
	e5=Entry(w5,width=20)
	e5.grid(row=1,column=1)
	e7=Entry(w5,width=20)
	e7.grid(row=2,column=1)
	b3=Button(w5,text='Return Book',relief=GROOVE,command=entry6)
	b3.grid(row=3,columnspan=2)	
	
def cb6():
	global e8
	global e7
	global w6
	w6=Toplevel()
	w6.geometry('700x300')
	w6.title('Manage Student')
	l4=Label(w6,text="Student Details",font=(16)).grid(row=0,column=0,columnspan=2)
	l4=Label(w6,text="Student ID").grid(row=1,column=0)
	l4=Label(w6,text="Student Name").grid(row=2,column=0)
	e7=Entry(w6,width=20)
	e7.grid(row=1,column=1)
	# e3.insert(0,'Type here')
	e8=Entry(w6,width=20)
	e8.grid(row=2,column=1)	
	b3=Button(w6,text='Add',relief=GROOVE,command=entry5)
	b3.grid(columnspan=2)
	l4=Label(w6,text='Student ID is enough for deleting/checking').grid(row=4,columnspan=2)
	b3=Button(w6,text='Delete',relief=GROOVE,command=entry9)
	b3.grid(columnspan=2)
	b3=Button(w6,text='Check',relief=GROOVE,command=entry10)
	b3.grid(columnspan=2)



m=Tk()
m.title('Library Login')
m.geometry('400x250')
def slogin():
	c=sqlite3.connect('Library.db')
	c1=c.cursor()
	# c.row_factory=sqlite3.Row
	sID=c1.execute('select * from student where ID ='+e1.get())
	# print(sID.fetchall())
	r=sID.fetchall()
	# print(r)
	sname=c1.execute('select ID from student')
	r1=sname.fetchall()
	r2=int(e1.get()),
	# print(r1)
	# print(r2)
	# print(type(r[0][0]))
	# print(type(r[0][1]))
	# print(type(e1.get()))
	# print(type(e2.get()))
	# print(sname.fetchall())
	# print(e1.get())
	# print(e2.get())
	if r2 in r1 and int(e1.get())==r[0][0] and e2.get()==r[0][1]:
			sbook=c1.execute('select * from sbooks where ID ='+e1.get())
			r3=sbook.fetchall()
			m1=Toplevel()
			m1.title('Library')
			m1.geometry('700x300')
			l=Label(m1,text='Library Menu',font=('Ariel Bold',30),bg='yellow').pack(fill=X)
			b=Button(m1,text='Display All Books',fg='green',bg='beige',command=cb1,width=20,height=2).pack(padx=10,pady=2)
			b=Button(m1,text='Book Availablity',fg='blue',bg='white',command=cb2,width=20,height=2).pack(padx=10,pady=2)
			# b=[Button(m1,text='Return book',fg='navyblue',bg='beige',command=cb3,width=20,height=2).pack(padx=10,pady=2)
			b=Button(m1,text='Logout',fg='red',bg='#ffffff',relief=GROOVE,command=m1.destroy).pack(padx=12,pady=10)
			for i in r3:
				# p=datetime.strptime(i[3],'%Y-%m-%d')
				# print(p)
				# q=p-date.today()
				s='Book ID : '+ str(i[1]) +'|| Issue Date : '+ str(i[2])+'|| Return Date : '+ str(i[3])+'\n'
				print(s)
				l=Label(m1,text=s).pack(pady=1)
			e1.delete(0,END)
			e2.delete(0,END)	
	elif r2 not in r1:
		messagebox.showinfo('Message','Invaid UserID')
	else:
		messagebox.showinfo('Message','Invalid Username')
	c.close() 
def mlogin():
	if e3.get()=='12345' and e4.get()=='12345':
		w=Toplevel()
		w.title('Library Management System')
		w.geometry('1000x500')
		l=Label(w,text='Library Menu',font=('Ariel Bold',30),bg='yellow').pack(fill=X)
		b=Button(w,text='Display all books',fg='green',bg='beige',command=cb1,width=20,height=2).pack(padx=10,pady=2)
		b=Button(w,text='Lend book',fg='blue',bg='white',command=cb3,width=20,height=2).pack(padx=10,pady=2)
		b=Button(w,text='Manage student',fg='blue',bg='#000000',command=cb6,width=20,height=2).pack(padx=10,pady=2)
		b=Button(w,text='Manage book',fg='black',bg='white',command=cb4,width=20,height=2).pack(padx=10,pady=2)
		b=Button(w,text='Return book',command=cb5,width=20,height=2).pack(padx=10,pady=2)
		b=Button(w,text='Logout',fg='red',bg='#ffffff',relief=GROOVE,command=w.destroy).pack(padx=12,pady=10)
		e3.delete(0,END)
		e4.delete(0,END)		
	else:
		messagebox.showinfo('Message','Invalid credentials')

l1=Label(m,text='Student Login',font=('Ariel Bold',16),bg='yellow').grid(row=0,column=0,padx=2,ipadx=10,pady=2,columnspan=2)
l1=Label(m,text='Management Login',font=('Ariel Bold',16),bg='yellow').grid(row=0,column=2,padx=20,ipadx=20,pady=2,columnspan=2)
m.config(bg='yellow')
e1=Entry(m,width=20)
e1.grid(row=2,column=0,pady=5)
l1=Label(m,text='Student ID').grid(row=1,column=0,padx=40,pady=5)
e2=Entry(m,width=20)
e2.grid(row=4,column=0,pady=5)
l1=Label(m,text='Student Name').grid(row=3,column=0,padx=40,pady=5)
e3=Entry(m,width=20)
e3.grid(row=2,column=2,padx=40,pady=5)
l1=Label(m,text='Management ID').grid(row=1,column=2,padx=40,pady=5)
e4=Entry(m,width=20,show='*')
e4.grid(row=4,column=2,padx=40,pady=5)
l1=Label(m,text='Management Password').grid(row=3,column=2,padx=40,pady=5)
b1=Button(m,text='Login',command=slogin,bg='blue').grid(row=5,column=0,pady=5)
b1=Button(m,text='Login',command=mlogin,bg='blue').grid(row=5,column=2,padx=40,pady=5)

##Placing buttons
# c=Checkbutton(w,text='select').pack(side='left')
# b.grid(column=2,row=2)
mainloop()