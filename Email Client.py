__author__ = 'Timothy Lam'
###Simple Email Client###

#Imports
import smtplib

#Base
sent = "true"
ss = "true"
repeats = 1

while sent == "true":
    #Your EmailL#
    m_email = input("Please input the Senders Email:\n")
    m_server = input("Please input the mail server (For Example: 'mail.host.com'):\n")

    #Recipients EmailL#
    r_emails = input("Please enter a list of comma seperated emails:\n")
    r_emails = r_emails.replace(" ", "").split(",")


    #Message#
    subject = input("Input your message subject:\n")
    subject = "Subject: " + subject
    main_body = input("Input the main message:\n")

    MESSAGE = subject + "\n \n" + main_body
    while ss == "true" or repeats == "5":
        #Sending the Email#
        try:
            smtpObj = smtplib.SMTP(m_server)
            smtpObj.sendmail(m_email, r_emails, MESSAGE)
            print ("Mail Sent Successfully!")
            ss = "false"
        except:
            print ("Sending Failed!")
            repeats = repeats + 1

    if input("Send another Email?\n") == "yes":
         sent = "true"
         ss = "true"
         repeats = 1
    else:
        sent = "false"