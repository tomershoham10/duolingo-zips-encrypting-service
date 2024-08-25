# ./redis/Dockerfile
FROM redis:latest

# Install procps which includes sysctl
RUN apt-get update && apt-get install -y procps

# Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose the Redis port
EXPOSE 6379

# Set the entrypoint to the script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
