.PHONY: default build test lint run clean docker-build docker-up

# Default help text
default:
	@echo "GÖKBÖRÜ SOTM - Development Makefile"
	@echo "Available commands:"
	@echo "  make lint          - Run flake8 code linter"
	@echo "  make test          - Run pytest suite"
	@echo "  make docker-build  - Build the containerized development environment"
	@echo "  make docker-up     - Spin up the ROS 2 container"
	@echo "  make clean         - Deep clean python cache files"

# Quality Checks
lint:
	flake8 scripts/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 scripts/ tests/ --count --max-complexity=10 --max-line-length=127 --statistics

test:
	pytest tests/ -v

# Docker Commands
docker-build:
	docker build -t gokboru-sotm:humble-v1 .

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

# Utilities
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	@echo "[*] Clean up complete."
