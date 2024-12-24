# Use the official NGINX image from the Docker Hub
FROM nginx:latest

# Copy the custom NGINX configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start NGINX in the foreground (required by Docker containers)
CMD ["nginx", "-g", "daemon off;"]

