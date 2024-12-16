responses = [200,300,403,500]
print(responses[0])
responses.append("456")
responses.append("678")
responses.append("123")
for i in responses:
    print(i)

responses.remove(300)
print(responses)

print(responses.count(200))