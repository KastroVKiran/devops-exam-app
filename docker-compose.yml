version: '3.8'

services:
  flask:
    build: ./backend
    container_name: flask_app
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
      - MYSQL_HOST=mysql
      - MYSQL_USER=root
      - MYSQL_PASSWORD=rootpass
      - MYSQL_DATABASE=devops_exam
    depends_on:
      mysql:
        condition: service_healthy
    volumes:
      - ./backend:/app
      - ./frontend:/app/templates

  mysql:
    image: mysql:5.7
    container_name: mysql_db
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: devops_exam
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-uroot", "-prootpass"]
      interval: 5s
      timeout: 10s
      retries: 10

volumes:
  mysql_data:
    driver: local
