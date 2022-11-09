sec = int(input())

hours = sec//3600
minutes = (sec - hours*3600)//60
all_secs = sec - hours*3600 - minutes*60

print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(all_secs).zfill(2)}")