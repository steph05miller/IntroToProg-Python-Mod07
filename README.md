# IntroToProg-Python-Mod07
## Code Header
As with every code we much start with the header of the code. In the header we included the title of the script, description of what the code is for, name of the developer, date of the code creation, and a change log for any future changes to the code. 

![image](https://user-images.githubusercontent.com/118407339/204572111-720874e2-13c9-4260-9fcd-8fea9cedf6c0.png)
 
## Error Handling
For the error handling demonstration, I decided to focus on specific except clauses. In the try clause I have input a simple equation y = 100/int(x). I decided to turn x into an int in the equation instead of the variable definition for the purpose of the error handling exceptions. 
 
 ![image](https://user-images.githubusercontent.com/118407339/204572217-3d509fa3-d804-469f-9662-38ddc1b1e403.png)
 
The first except block is defined as NameError. This except block will not be triggered with the current way the code is written because I have not defined the x variable. We see the following when the code is run:

![image](https://user-images.githubusercontent.com/118407339/204572255-e85fcff6-1d57-4fd8-9831-b4f182042d0f.png)
 
This is since the x variable can’t be used when we do not set it to a specific value. In this code when the Name Error is triggered, as is the case based on the way we set up the code. The statement will print telling the user that the X variable must be defined. The next statement will then print telling the user what the python defined error is. The code used to display when this error is triggered can be seen below:

![image](https://user-images.githubusercontent.com/118407339/204572321-cb92d78c-482c-4d94-a863-18449c083723.png)
 
The last except clause in this code is the generalized exception clause that will catch any errors the might be missed. However, with the way the code is currently written the code will always stop at the first error and never make it to the second block in the code. 

![image](https://user-images.githubusercontent.com/118407339/204572377-ce923c69-5511-4cc2-a307-cf9e086385f9.png)
 
## Pickling
The first step when using the pickling is to import pickle. This will allow us to use binary. 

![image](https://user-images.githubusercontent.com/118407339/204572409-8c44144f-b7a9-4122-b525-47d3f347ea26.png)
 
To set up the code I first ask the user to input a task and its priority. I then save the user input to a list that can be referenced later. This will give us some data to work with in the rest of the code.

![image](https://user-images.githubusercontent.com/118407339/204572463-8ab1b978-13e8-4ceb-bb0f-6377d23592e2.png)
 
In the next section of code, I open the file I want to save the code to. In this section we need to save the code as .dat so that it will save as binary. We will then open the code in ab which will allow us to append data in binary. In the next part we need to dump the data from the list into the file. Lastly, we will close the file. 

![image](https://user-images.githubusercontent.com/118407339/204572510-327d654d-4ad5-4276-a2e2-bc6e0094970c.png)
 
In the next part of the code, I open the file again, this time I open in rb. This will open the binary data in read mode. Next, I need to use pickle load to open the file. We need to do pickle load so the data will be read back in non-binary. Then the file is closed again. 
 
 ![image](https://user-images.githubusercontent.com/118407339/204572569-c20e3568-ec96-43e6-bfda-2ee59b0a380b.png)
 
The last step in the code is to print the file data so we can see what is contained in the file. 
 
![image](https://user-images.githubusercontent.com/118407339/204572615-0c7566ad-c0cf-4471-ae3f-741da00f24e1.png)
