# FenderFinder (ML)

Ever wondered what would be the price of a car that you found interesting, but don't know its details? Just click a picture and we will find the nearest dealers for the car with the right price!

## Before you start, Install the following

1. latest version of npm
2. NodeJS
3. Python3

## Frontend

1. (First time cloning the repo only) navigate into the `frontend` folder and type `npm install`
2. To run the frontend locally, navigate into the `frontend` folder and type `npm start`, you will see real time update in the page!
3. `Ctrl + C` to stop running the site
   Frontend is now live at https://polar-reef-47694.herokuapp.com

## Backend

To deploy to localhost:

- shortcut on visual studio code: `Ctrl +Alt + N` starts running code, `Ctrl + Alt + M` stops, links shown in terminal
- start up a virtual environment in the `backend` directory
- type the following lines into the command line in the `backend` directory

*Note, you may have to use Cntrl-C once on the backend terminal window to have it send the first request after the request was made*
`set FLASK_APP=main.py`
`$env:FLASK_APP = "main.py"`
`flask run`

- backend is now deployed to google cloud at https://fenderfinder.wl.r.appspot.com/
 
## Machine Learning 

- A resNet50 model that is trained to classify the image of the car based on its the model
- notebook containing training code is in the ML folder
- run the code on your training set as required and download the model to upload it in the backend
