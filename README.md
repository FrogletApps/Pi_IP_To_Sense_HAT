# Pi IP To Sense HAT

I wanted to be able to see the IP of my Pi (which is often running headless on my desk).  Therefore I wrote the original code (ipToSenseHat.py) to simply write the IP address onto the screen of the Sense HAT, however I only tended to remember this would happen after the first digit had gone.  Rather than doing something sensible like slowing the digits down (how boring would that be), I decided to create a variant (ipToSenseHATBinary.py) which instead shows the IP in Binary Coded Decimal, it's pretty quick to read, plus I don't have to have seen the screen was on straight away!  (Plus it also looks really cool!)

The BCD numbers are displayed in green, points are shown as 4 dots of blue, and unused space at the end is shown in red.
