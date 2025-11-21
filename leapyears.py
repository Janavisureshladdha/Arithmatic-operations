years =2003
def leap_year(years):
    if(years%4==0 or years%100==0 and 400%2!=0) :
         print("IS A LEAP YEARS ")
    else :
         print("IS NOT A LEAP YEARS ")
         return years
b = leap_year(years)
print(b)