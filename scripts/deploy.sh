#!/bin/bash
set -e

SERVER_USER="vityuntu"
SERVER_HOST="192.168.1.111"
SERVER_PATH="~/homeserver/home-device-bridge"
REBUILD=false

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

while [[ $# -gt 0 ]]; do
    case $1 in
        --rebuild)
            REBUILD=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo -e "${GREEN}=== Home Device Bridge Deploy ===${NC}\n"

if [ ! -f "docker-compose.yml" ]; then
    echo -e "${RED}Error: docker-compose.yml not found. Run this script from project root.${NC}"
    exit 1
fi

echo -e "${GREEN}Step 1: Syncing code to server...${NC}"
rsync -avz --delete \
    --exclude '.git/' \
    --exclude '.venv/' \
    --exclude '__pycache__/' \
    --exclude '.env' \
    . ${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/

echo -e "\n${GREEN}Step 2: Deploying on server...${NC}"

if [ "$REBUILD" = true ]; then
    echo -e "${YELLOW}Rebuilding containers...${NC}"
    ssh ${SERVER_USER}@${SERVER_HOST} << 'ENDSSH'
        cd ~/homeserver/home-device-bridge
        docker compose down
        docker compose build --no-cache
        docker compose up -d
        docker compose ps
ENDSSH
else
    ssh ${SERVER_USER}@${SERVER_HOST} << 'ENDSSH'
        cd ~/homeserver/home-device-bridge
        docker compose down
        docker compose up -d
        docker compose ps
ENDSSH
fi

echo -e "\n${GREEN}=== Deploy Complete ===${NC}"
