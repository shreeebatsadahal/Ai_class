import time
start_time=time.time()
for i in range (0,10):
    print(i)
print(time.time()-start_time)
#time complexity gives relation of input and time   

###o(1)--constant, o(n)--linear, o(n^2)--quadratic, o(log n)--logarithmic, o(n log n)--linearithmic
#think it as time in y and input in x axis
#o(1)>o(log2n)>o(n)>o(n^2)