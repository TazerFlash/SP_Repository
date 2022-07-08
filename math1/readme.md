This challenge introduces us to one of the basic mathematical concepts used in key encryption, i.e Greatest Common Divisor (GCD)
or Highet Common Factor (HCF). 

There are various algorithms that can be used in setting the GCD up. I have chosen the Euclidean approach, as mentioned in the 
challenge notes itself.

It works under the following logic:
If we subtract a smaller number from a larger (we reduce a larger number), GCD doesn’t change. So if we keep subtracting 
repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find remainder 0. 

The python code implementation for the same is attached in this directory unde the name: "math1.py"
