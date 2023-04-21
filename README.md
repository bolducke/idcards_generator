# ID Card Generator

![image](https://user-images.githubusercontent.com/26026137/233532015-bd9e0607-3aa1-4786-99a0-5040b3a5d350.png)


## Motivation

For FoieGraph 2022, we needed to create IDCards for every member that were attending the event. Unfortunately, I didn't find any script to accomplish this task. I decided to provide my script so that anyone can inspire themself to waste as little time as possible. In the template `template/page.htm`, I fined-tune the margin that would be easier to cut through and to keep the content intact while printing (Most printer have a *dead zone* where the content is not properly draw).

## How does it works?

The formatting of every card is handle using `html` and `css`. The script in python is used to generate the documents holding the ID.

To begin, you need a template for your ID Card (Adobe Illustrator, By hands, etc...). Then, based on this template, you mark slots where you want to insert information. Finally, the filled cards are inserted into a document. You only need to print the document. (Most browsers let you print the `html` document using `ctl-p`.)

## Credit

The design of the template was done by Mariia Myronova. 
