# ID Card Generator

![image](https://user-images.githubusercontent.com/26026137/233532015-bd9e0607-3aa1-4786-99a0-5040b3a5d350.png)


## Motivation

For FoieGraph 2022, we needed to create IDCards for every member that were attending the event. Unfortunately, I didn't find any script to accomplish this task. I decided to provide my script so that anyone can inspire themself to waste as little time as possible. In the template `template/page.htm`, I fined-tune the margin that would be easier to cut through and to keep the content intact while printing (Most printers have a *dead zone* where the content is not properly drawn).

## How does it work?

The formatting of every card is handled using `html` and `css`. The script in Python is used to generate the documents holding the ID.

1. You create an `html` template for your ID Card. (Adobe Illustrator, etc).
2. You need to specify an id on the field where you need to insert information.
3. You run the script. (You only need to alter directly the 3-4 variables)
4. You print the document with your browser. (Often `ctl-p`)

## Credit

The design of the template was done by Mariia Myronova. 
