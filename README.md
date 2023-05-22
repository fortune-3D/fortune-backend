# Fortune 3D  
Team: Tyler Huntley, Darran Holmes, Sheldon Pierce, Dominick Martin     
Date: 05/19/2023    
Backend Version: V1.0  
Backend Setup: Tyler Huntley  

- Added a response randomizer.   
- Deployed to Vercel and ensured that the api is working properly and connected to the database.  
- [Fortune Backend](https://fortune-backend.vercel.app/api/v1/fortune/)  

Team: Tyler Huntley, Darran Holmes, Sheldon Pierce, Dominick Martin     
Date: 05/19/2023    
Backend Version: Alpha/Beta  
Backend Setup: Tyler Huntley  

Resources:  
[ChatGPT](https://openai.com/blog/chatgpt) - For coming up with cosmic phrases to reply
[django](https://github.com/django/django)

- Worked on getting the backend api built for our full-stack application.  
- Backend is up and running locally, database is populated with replies 

## SETUP
```
If you are running locally: 

python3 -m venv .venv
python3 .venv/bin/activate

Install all requirements
pip install -r requirements.txt

Bring up Docker
docker compose up
```

## Testing  
Testing for the backend was all done manually as the ElephantSQL database and project setup will not allow for temp user or database items to be created.   
Ensured that database properly adds items from the backend admin & api views.  
