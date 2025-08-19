def greet(time):
    if time >= 5 and time <= 11:
        return "good morning"
    elif time >= 12 and time <= 17:
        return "good afternoon"
    else:
        return "evening"
    

print(greet(5))