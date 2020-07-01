import smtplib as s
# simple mail transfer protocol

#object creation
obj= s.SMTP("smtp.gmail.com", 587)

#connection security
obj.starttls() #tls= transport layer security

#login
obj.login("kumardigamberjha@gmail.com", "digamberjha@1099")

#create message

Subject= "This is a subject"
body= "This is a body for testing this program"

message= f"Subject:{Subject}\n\n {body}"

#sending mail
obj.sendmail("kumardigamberjha@gmail.com", "digamber1011@gmail.com", message)
print("Message sent successfully")
obj.quit()