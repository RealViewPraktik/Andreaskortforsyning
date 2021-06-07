import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob



#print(glob.glob(f"data/cutimage/100/*.jpg"))

def mail_sender(orderID, mail):   
    print('This is where i would sent a mail if i was allowed. MY ORDER AND EMAIL IS: ', orderID, mail)
   # fromaddr = "systemintigration2020mail@gmail.com"
   # password = "CSQtF2kLw0c9"
   # toaddr = mail
   # msg=MIMEMultipart()
   # msg['FROM'] = fromaddr
   # msg['TO'] = toaddr
   # msg['Subject'] = 'Lokations order! WEEEEh'
   # body = 'Dette er din bestilling på en lokation gennem realviews nye maskinerri'
   # msg.attach(MIMEText(body, 'plain'))
    
   # images = glob.glob(f"/data/cutimage/{orderID}/*.jpg")
   # imagecount = 1
   # for image in images:
   #     filename = imagecount
   #     attachment = open(image, 'rb')
   #     p = MIMEBase('application', 'octet-stream')
   #     p.set_payload((attachment).read())
   #     encoders.encode_base64(p)
   #     p.add_header('Content-Disposition', "Attachment; filename= %s" % filename) 
   #     msg.attach(p)
   #     imagecount +=1

   # s = smtplib.SMTP('smtp.gmail.com', 587)
   # s.starttls()
   # s.login(fromaddr, password)
   # text = msg.as_string()
   # s.sendmail(fromaddr, toaddr, text)
   # s.quit


