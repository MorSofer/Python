A flask-driven restful API for Bucketlist interactions

Technologies used
Python3, Flask and Keras

make sure you have python3, you can downloand from:
https://www.python.org/downloads/

And for the import I used:
pip install keras

pip install flask

pip install request 

(Note I also using Numpy, Pandas, jpblib and JSON)

downloand the titancAPI.py and titanic.h5 from the same folder.
from the folder open powershell or cmd and run the command python titanicAPI.py - this will active the API

I worked with postman desktop to send post request to the API in the server:
127.0.0.1:8080/predict 
with values:
{"pcalss": class(int), "sex": female(0)/male(1) (int), "age": age (float), "fare": fare (float), "family":family_size (int)}

{"pcalss": 3, "sex": 1, "age": 24, "fare": 320, "family":2}
and the API will response by "Surivive: Yes/No" according to the result
