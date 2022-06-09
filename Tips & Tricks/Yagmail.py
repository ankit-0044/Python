import yagmail

sender = "senprod34xx.gn@gmail.com"
receiver = "ankitsinghshakya.as@gmail.com"

subject = "Testing yagmail"

sender_pass = input("please enter your passwd:")

yag = yagmail.SMTP(user=sender,password=sender_pass)

content = ["Successfuly send the email.",
			"C:\\Users\\Ankit Singh\\Desktop\\Programs\\Python\\Lena_Copy.jpg"]

yag.send(to=receiver,subject=subject,contents=content)
