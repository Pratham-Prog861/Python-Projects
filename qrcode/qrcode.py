import qrcode
from IPython.display import display, Image

# Get UPI ID from user input
upi_id = input("Enter your UPI ID: ")

recipient_name = "Recipient Name"  
amount = int(input("Enter the amount to pay : "))
currency = "INR"  
transaction_note = "Payment for services"


# phonepe_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&tn={transaction_note}'
# paytm_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&tn={transaction_note}'
google_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}&tn={transaction_note}'


# phonepe_qr = qrcode.make(phonepe_url)
# paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#You can use this to save the file in your laptop

#phonepe_qr.save('phonepe_qr.png')
#paytm_qr.save('paytm_qr.png')
#google_pay_qr.save('googlepay_qr.png')

#This is to display the qrcode but you write code in google colab this might not work 

# phonepe_qr.show() 
# paytm_qr.show()
# google_pay_qr.show()


#This work in google colab

# display(phonepe_qr)
# display(paytm_qr)
display(google_pay_qr)