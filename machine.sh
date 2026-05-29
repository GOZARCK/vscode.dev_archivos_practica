echo "=== INFO DE TU CODESPACE ===" && \
echo "Cores: $(nproc)" && \
echo "RAM: $(free -h | grep Mem | awk '{print $2}')" && \
echo "Disco: $(df -h / | awk 'NR==2 {print $2}')" && \
echo "SO: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)" && \
echo "=================================="