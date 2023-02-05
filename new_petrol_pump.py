import new_fuel_rate as fr  
import datetime
import random
import sys
from text_to_speech import speak
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email_send_passwd                     # mail & passward created file import


try :
    name = " Welcome To HP Petrol Pump "
    speak(" Welcome To HP Petrol Pump ")
    print(name.center(50,"-"))
    fuel_types = ("*** Avileble Fuel Types ***")
    print(fuel_types)
    print("1] Petrol ")
    print("2] Diesel")
    print('3] CNG')
    print("4] Exit")
    print('-'*40)

    while(True):

        speak("Enter Valied Number like 1 2 3 if you want fuel else enter 4 for exit")
        choice = int(input("Enter your fuel type [1/2/3/4] - "))
    
        if choice == 1:
            speak("you select petrol")
            speak("Enter amount")
            amount = float(input("Enter your amount - Rs "))
            fuel_type = "Petrol"
            quantity = amount/fr.petrol_rate()
            print('-'*40)
            # round function is removes more than 2 decimal 
            speak(f"You Got {round(quantity,2)} liters {fuel_type} of RS.{amount}")
            print(f"You Got {round(quantity,2)} liters {fuel_type} of RS.{amount}")
            break

        elif choice == 2:
            speak("you select diesel")
            speak("Enter amount")
            amount = float(input("Enter your amount - Rs "))
            fuel_type = "Diesel"
            quantity = amount/fr.disel_rate()
            print('-'*40)
            speak(f"You Got {round(quantity,2)} liters {fuel_type} of RS.{amount}")
            print(f"You Got {round(quantity,2)} liters {fuel_type} of RS.{amount}")
            break

        elif choice == 3:
            speak("you select CNG")
            speak("Enter amount")
            amount = float(input("Enter your amount - Rs "))
            fuel_type = "CNG"
            quantity = amount/fr.cng_rate()
            print('-'*40)
            speak(f"You Got {round(quantity,2)} Kg {fuel_type} of RS.{amount}")
            print(f"You Got {round(quantity,2)} Kg {fuel_type} of RS.{amount}")
            break

        elif choice == 4:
            print("*** Thanks for Visit Our Petrol Pump ***")
            speak("Thanks for visit our Petrol Pump")
        sys.exit()

    print('-'*40)
    
    # Printing Current Date & Time - 
    date_time = datetime.datetime.now()

    # Create Random Bill No -
    bill_no = random.randint(999999,9999999)
    
       
    # Create Bill PDF -
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=15) 
    pdf.text(30,25,txt = f"HP Petrol Pump")
    pdf.text(30,30,txt = f"Date & Time - {date_time}")
    pdf.text(30,35,f"Bill no - {bill_no}")
    pdf.text(30,40,txt = f"You Got - {round(quantity,2)} Liters {fuel_type}")
    pdf.text(30,45,txt = f"Amount is - {amount}")
    pdf.text(30,50,txt = "Thank You... Visit Again !!!")
    a = f"HP_Fuel_Bill {bill_no}.pdf"
    pdf.output(a)
    
    
    # Send Created Bill PDF In Gmail -

    fromaddr = email_send_passwd.mail
    pwd =  email_send_passwd.password
    receiver_mail = input("Enter your Email id = ")
    toaddr = receiver_mail
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr
    msg['Subject'] = "Regarding fuel bill"
    body = "This is an email with a PDF attachment."
    msg.attach(MIMEText(body,'plain'))
    attachment = open(f"C:/Users/hp/Desktop/python/python_cw/{a}", "rb")

    # Instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p)   
    p.add_header('Content-Disposition', "attachment; filename= %s" % a)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr,pwd) 
    text = msg.as_string()
    s.sendmail(fromaddr, receiver_mail , text)
    s.quit()
    

    print('-'*40)
    print("Your Bill Send on Your Email... Thank You... Visit Again.")
    speak("Your Bill Send on Your Email... Thank You... Visit Again.")

except BaseException as ex:
    print(f"Error Occured = {ex}")

finally:
    print("finally")

