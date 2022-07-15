In this challenge, there was a hex string provided, which was the flag itself. But to get to the flag, we need to obtain the ASCII equivalent of the same. 
Since the challenge drops us a hint about converting the hex string to bytes, we use the bytes.fromhex() function from the python libraries to do the same.
Next, the function to conver the bytes to ASCII equivalents is used i.e. variable_name.decode("ASCII"). After this is done, the flag can be printed and retrieved. 

The equivalent python code to do the above exists under the name "Encode2.py"
