# A small project

# Note--
# 1st welcome statements
# 1 new ragistration
# 2 fee submision
# 3 data submission/ class teacher work
# 4 principal access
# 5 exit


# We start here to write a small project


print("Welcome to WsCube tech :\n")

box = (" 1- New Registration \n 2- Fee submission \n 3- Data submission/ class teacher \n 4- Principal Access \n 5- Exit ")
print(box)
while True:
# for n in range(1, 6):
    print()
    i = int(input("Hi user kindly choose the number 1 to 5, which is mentioned in the above along with the discreption :"))
    print()
    if i == 1:
        print()
        m=int(input("How meny student registration :"))
        for j in range(1,m+1):
            first_name = input("Your first name :")
            last_name = input("Your last name :")
            father_name = input("Your father's  name :")
            mother_name = input("Your mother name :")
            contact = input("Your contact details name :")
            id_number =int(input("Your id number name :"))
            print()
            
            

            # Data save in sql serer
            try:
                import sqlite3
                cann=sqlite3.connect("new.db")
                cur=cann.cursor()
                data="""CREATE TABLE school (first_name varchar(255),last_name varchar(255),father_name varchar(255),mother_name varchar,contact varchar(255),
                id int PRIMARY KEY,fee_amount int,class_teacher varchar,hindi int,english int,ecocomics int,politicial int,
                sociology int,percentage float)"""
                cann.execute(data)
                cann.commit()
            except:
                pass

            # insert data in the table

            import sqlite3
            cann=sqlite3.connect("new.db")
            cur=cann.cursor()
            data="INSERT INTO school VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            t1=(first_name,last_name,father_name,mother_name,contact,id_number,0,0,0,0,0,0,0,0)
            cur.execute(data,t1)
            cann.commit()
            cann.close()

            print("Your first step is successfully processed :")
            print()
            print(box)
            print()
        
    elif i == 2:
        print()
        # Use update query and update the fee as well
        Id_match = int(input("Enter your id which you have submitted on the registration time :"))
        print()
        print()

        amount =int(input("Fee :"))
        print()
        print()

        # Update query

        try:
            import sqlite3
            conn=sqlite3.connect("new.db")
            cur=conn.cursor()
            t2=(amount,Id_match)
            data1=("UPDATE school SET fee_amount=? where id=?")
            cur.execute(data1,t2)
            print(amount)
            conn.commit()

        except:
            print("Kindly entre the correct id  ")


        print(box)

    elif i == 3:
        print("Student score :")
        print()
        class_teacher = input("class teached id :")
        Roll_number = input("Entre student id_number :")
        print("subject marks :")
        print()
        hindi = int(input("Hindi marks :"))
        english = int(input("English marks :"))
        ecocomics = int(input("Economics marks :"))
        politicial = int(input("Politicial science marks :"))
        sociology = int(input("Sociology marks :"))
        percentage = (hindi+english+ecocomics+politicial+sociology)/5
        print()
        print("Your total parcentage is :", percentage)
        print()
        print(box)
        print()

        # Update students Marks

        import sqlite3
        conn=sqlite3.connect("new.db")
        cur=conn.cursor()
        t3=(class_teacher,Roll_number)
        t4=(hindi,Roll_number)
        t5=(english,Roll_number)
        t6=(ecocomics,Roll_number)
        t7=(politicial,Roll_number)
        t8=(sociology,Roll_number)
        t9=(percentage,Roll_number)

        data3=("UPDATE school SET class_teacher=? where id=?")
        data4=("UPDATE school SET hindi=? where id=?")
        data5=("UPDATE school SET english=? where id=?")
        data6=("UPDATE school SET ecocomics=? where id=?")
        data7=("UPDATE school SET politicial=? where id=?")
        data8=("UPDATE school SET sociology=? where id=?")
        data9=("UPDATE school SET percentage=? where id=?")

        cur.execute(data3,t3)
        cur.execute(data4,t4)
        cur.execute(data5,t5)
        cur.execute(data6,t6)
        cur.execute(data7,t7)
        cur.execute(data8,t8)
        cur.execute(data9,t9)
        conn.commit()
        conn.close()

    elif i == 4:

        print("Principle access :")
        # Show all data to principal  
        # Select Query

        import sqlite3
        conn=sqlite3.connect("new.db")
        cur=conn.cursor()
        data10=("SELECT * FROM school")
        new=cur.execute(data10)
        for i in new:
            print(i)
        conn.close()

        print(box)
        print()

    elif i == 5:
        break

    else:
        print("Thanks for using this :")
        break
