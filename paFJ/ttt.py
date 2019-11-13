# import random
#
# USER_AGENT_LIST = [
#         'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
# ]
# print(random.choice(USER_AGENT_LIST))

name = 'https://www.anjuke.com/sy-city.html'
print(name.split(".", 1))
print(name.split(".", 1)[0])
print(name.split(".", 1)[0][8:])
