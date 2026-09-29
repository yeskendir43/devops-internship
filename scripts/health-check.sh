#!/bin/bash

echo "================================"
echo " DevOps Internship Health Check "
echo "================================"

echo
echo "[HOST]"
hostname

echo
echo "[UPTIME]"
uptime -p

echo
echo "[MEMORY]"
free -h | head -2

echo
echo "[DISK]"
df -h /

echo
echo "[DOCKER SERVICES]"
docker compose ps

echo
echo "[NGINX]"
systemctl is-active nginx

echo
echo "[APPLICATION]"
curl -s http://localhost:5000/health

echo
echo
echo "Health check completed."
