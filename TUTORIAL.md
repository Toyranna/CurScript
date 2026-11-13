# Writing CurScript:

### Moving in different directions:
Write the first letter of the direction and then the amount of pixels in that direction you want to move.
For example, if I wanted to draw a square, my code would be:

```
L100
D100
R100
U100
```
### Going to exact positions:
Write the axis and then the value.
For example, moving to the top left of the screen

```
X0
Y0
```
### Waiting
To make the program wait, you can use "W" followed by the amount of seconds you want to wait before performing the next action.
For example, adding onto the square from earlier:
```
L100
W0.2
D100
W0.3
R100
W0.4
U100
```
### Clicking
To make the mouse click, you can use "C" followed by either L (left), R (right), or M (middle)
For example, making the mouse left click, right click, and middle click:
```
CL
CR
CM
```
### Scrolling
You can scroll up and down using "S" followed by the number of lines you want to scroll (positive is up; negative is down)
for example, scrolling up by 20 lines, waiting, and then scrolling down by 30 lines
```
S20
W0.5
S-30
```
### Making movement fluid
To make the mouse smoothly glide instead of teleporting, you can use "T" followed by the glide time.
For example, I want the mouse to slowly glide to the left over 5 seconds:
```
T5
L100
```

### Sending messages
If your program includes mouse clicks, it might be a good idea to warn the users beforehand. You can do this by writing "M" followed by your message.
For example, warning the user 10 seconds before a click.
```
MWARNING: This script includes clicks!!!
W10
CL
```
### Conclusion
Those are all the commands currently present in CurScript. Keep an eye on this repository in case I add new ones!
Hopefully you now understand how to write CurScript. If you need an example of it's use, CurScript comes with a default script in the projects folder.
