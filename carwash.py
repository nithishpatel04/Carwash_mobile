import mysql.connector as c

con = c.connect(host='db4free.net',
                database='carwash',
                user='nithish123',
                passwd='carwash1')

cursor = con.cursor()
while True:
    choice = input('1. New User Registration\n2. LOGIN as USER\n3. LOGIN as ADMIN\n4. Exit\nChoose Your Action:')

    if choice == '1':
        name = input('\nEnter Your Name: ')
        mail = input("Enter Your mail: ")
        password = 1
        pass2 = 0
        while password != pass2:
            password = input("Enter a password: ")
            pass2 = input('Re-enter your password: ')
            if password != pass2:
                print('\nYou Failed to retype password\n')
        query = f"insert into login_details(name,email,password) values('{name}','{mail}','{password}')"
        cursor.execute(query)
        con.commit()
        print("\nAccount Created Successfully ❤️😊\n")
        print("*" * 110)

    elif choice == '4':
        print("\nThanks 4 Visiting ❤️❤\n️")
        print('*' * 110)
        break

    elif choice == '2':
        check = 0
        carwash = 0
        while not (check):
            mail = input('\nEnter your E-Mail: ')
            password = input("Enter Your Password: ")
            query = f"select login_details.id from login_details  where login_details.email = '{mail}' and login_details.password = '{password}' and login_details.type = 'user' "
            cursor.execute(query)
            check = cursor.fetchone()
            if check:
                print('successfully logged in 😎😎\n')
                break
            else:
                print("\nE-Mail and Password Doesn't Match ---- Please Try Again\n")
                continue

        while True:
            print("*" * 110)
            print(' ' * 30, 'WELCOME BOOK YOUR CARWASH\n')
            pincode = int(input('Enter pincode to search availabe CARWASH centers in your area: '))
            query = f"select av.carwash_id ,av.center_name , av.address, av.state, av.pincode, av.slots_available  from location as av where pincode = '{pincode}'"
            cursor.execute(query)
            carwash = cursor.fetchall()

            if carwash:
                print('Here are the Service Centers Near You :\n')
                for i in carwash:
                    print(
                        f" Carwash ID : {i[0]}\nSERVICE CENTER Name : {i[1]}\nLocation : {i[2]}\nState : {i[3]}\nPincode : {i[4]}\nTotal Slots : {i[5]}\n")

                rev = int(
                    input('\n-->Enter 1 to Book A SloT\n-->Enter 2 to search another location:\n-->Enter 3 to Logout'))
                if rev == 3:
                    print("*" * 110)
                    break

                elif rev == 2:
                    continue
                elif rev == 1:
                    service_center = [100]

                    while service_center[0] > 10:
                        service_id = int(input('\nEnter center ID from above available Centers: '))
                        testquery = f"select count(*) from login_details  where login_details.carwash_id = {service_id} and login_details.booking_date = curdate()"
                        cursor.execute(testquery)
                        service_center = cursor.fetchone()
                        con.commit()
                        if service_center[0] < 5:
                            query = f"update login_details as ld set ld.carwash_id =  {service_id}, ld.booking_date = curdate() where ld.email = '{mail}' "
                            cursor.execute(query)
                            con.commit()
                            br = input("Slot Successsfully Booked Press Enter to Logout\n")
                            print("_" * 100)
                            if br == '':
                                break

                            else:
                                print('No Slots Available in this Center select another Center ID: ')
                                continue
                    break

            else:
                print("\nSORRY NO NEARBY CARWASH  LOCATIONS FOUND\nTRy ANOTHER PINCODE")
                continue
    elif choice == '3':
        check = 0
        while not (check):
            mail = input('\nEnter your E-Mail: ')
            password = input("Enter Your Password: ")
            query = f"select ld.id from login_details as ld where ld.email = '{mail}' and ld.password = '{password}' and ld.type = 'admin' "
            cursor.execute(query)
            check = cursor.fetchone()
            if check:
                print('successfully logged in 😎😎')
                break
            else:
                print("\nE-Mail and Password Doesn't Match ---- Please Try Again\n")
                continue

        while True:
            print("______________________________________________________")
            admin_case = int(input(
                '\n-->Enter 1 to add Service Centers:\n-->Enter 2 to Get Total slots Details:\n-->Enter 3 to delete Service Centers:\n-->Enter 4 to Logout : '))
            if admin_case == 4:
                print("\nLogging out....\n")
                print("*" * 110)
                break

            elif admin_case == 2:
                slots = 0
                query = "select vl.center_name, vl.slots_available from location  as vl "
                cursor.execute(query)
                dose = cursor.fetchall()

                for i in dose:
                    print(f"\nSERVICE CENTER Name: {i[0]}\nAvailable Dose: {i[1]}")
                br = input("\n-->Enter 1 to logout\n-->Enter any key to continue: ")
                if br == '1':
                    break
                else:
                    continue

            elif admin_case == 3:
                querys = "select av.carwash_id, av.center_name  from location as av  "
                cursor.execute(querys)
                s = cursor.fetchall()

                for i in s:
                    print(f"\nCARWASH ID: {i[0]}\nCENTER Name: {i[1]}")
                    print('----------------------------------------------')
                id = int(input("Enter ID of the Carwash Centers U want To Delete: "))
                queryd = f"delete from location  where carwash_id = '{id}' "
                cursor.execute(queryd)
                con.commit()
                print("Selected Service Centers Location Successfully Deleted 😊")
                print('\n----------------------------------------------')

                br = input("-->Enter 1 to logout\nEnter any key to continue: ")
                if br == '1':
                    break
                else:
                    continue

            elif admin_case == 1:
                center_name = input("\nEnter Service Center Name: ")
                state = input("Enter State: ")
                add = input("Enter address: ")
                pin = input("Enter Pincode: ")
                dos = input("Enter Slots Available: ")
                query = f"insert into location(center_name,state,address,pincode,slots_available) values('{name}','{state}','{add}','{pin}',{dos})"

                cursor.execute(query)
                print("\nNew Center Added Successfully....\n")
                br = input("-->Enter 1 to logout\nEnter any key to continue: ")
                print("\n")
                if br == '1':
                    break
                else:
                    continue
            continue

    else:
        print('\nPlease Choose Valid Action --> Heading HOMPAGE\n')
        print("*" * 110)
        continue
