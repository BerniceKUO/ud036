from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc2269010eb6bd26cfdb8287c814a5e26"
# Your Auth Token from twilio.com/console
auth_token  = "546867c36e83a01973994c16d7b83b1b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8860958860175", 
    from_="+12138553080",
    body="發中文的訊息試試 感恩今天是美好的一天!")

print(message.sid)


#pip install --target=c:\python\lib twilio
#把套件安裝到指定位置
