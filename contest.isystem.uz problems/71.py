months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
n = int(input())
print(months[n] if (n > 0 and n < 13) else 'none')
