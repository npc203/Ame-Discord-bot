import datetime
print(datetime.datetime.now())

with open('guilds.txt','a') as f:
    f.write(str(datetime.datetime.now())+'guild_name,'+'command')
