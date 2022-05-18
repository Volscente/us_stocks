# Dockerfile for us_stocks_image

# Base image
FROM alpine:latest

# Update & Upgrade
RUN apk update && apk upgrade --available

# Install Git
RUN apk add git

# Commands
CMD ["echo", "container started"]