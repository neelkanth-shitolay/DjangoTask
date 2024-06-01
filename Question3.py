#Step 3
Update packages: sudo apt update && sudo apt upgrade -y
Install Python, pip, virtualenv: sudo apt install python3-pip python3-venv -y
Install Nginx: sudo apt install nginx -y
Install PostgreSQL (optional, if you are using PostgreSQL): sudo apt install postgresql postgresql-contrib -y


#Step 4
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#Step 5 - Configure Gunicorn

#Install Gunicorn
pip install gunicorn  
sudo nano /etc/systemd/system/gunicorn.service  

#Create a Systemd file for Gunicorn 
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=your-username
Group=www-data
WorkingDirectory=/home/your-username/your-project
ExecStart=/home/your-username/your-project/venv/bin/gunicorn --workers 3 --bind unix:/home/your-username/your-project/yourproject.sock yourproject.wsgi:application

[Install]
WantedBy=multi-user.target  

#Start and Enable GUnicorn
sudo systemctl start gunicorn
sudo systemctl enable gunicorn  

#Step 6 - Configure Nginx

#Create Nginx server block 
sudo nano /etc/nginx/sites-available/yourproject

server {
    listen 80;
    server_name your_server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/your-username/your-project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/your-username/your-project/yourproject.sock;
    }
}  

#Enable file using symlink  
sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx



