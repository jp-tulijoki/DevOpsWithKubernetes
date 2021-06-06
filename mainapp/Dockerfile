FROM python
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
EXPOSE 8000
CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]