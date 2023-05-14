seconds = 1000008

days = seconds // 86400
print(days)

hours = seconds // 3600
print(hours)

seconds = seconds % 3600
minutes = seconds // 60
print(minutes)

seconds = seconds % 60
print(seconds)
