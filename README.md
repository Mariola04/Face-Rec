# Face Rec code using Simple Face Rec library and opencv

This was a project I made on my spare time with the purpose of redoing it on my Arduino Board and linking it with a web server. But as of now it only has the python code for it 

The program is pretty simple, once you execute it it opens a seperate window with your camera, after the program detects a face a red square will appear and it will following you as long as it can see you.

If you are not in the image database your tag will be "Unknown" and if you are it will have your name

## Libraries

First you need all the libraries necessary to run the project

On Ubuntu or in the command prompt go ahead and type the following lines of code:

```
sudo apt install python3-pip
```

Then:
```
pip3 install opencv-python
```

And finally:
```
pip3 install face_recognition
```

## Execution

To run the program you simply need to be in the respective directory and run:

```
python3 main.py
```

To exit the window press "Esc" 

### New Face
If you want to add a new face simply press "n", the window will freeze and on the terminal a new prompt will appear that asks you to write the person name, after typing the name click enter and the window will unfreeze.

And a screenshot of the "Unknown" rectangle in the moment you pressed "n" will be added to "/images" and the person is now added to the database
