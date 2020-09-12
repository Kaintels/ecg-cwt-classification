@echo off

echo "Data Download... wait 1 seconds..."
timeout 1
mkdir ".\data"
curl.exe --output ".\data\ECG5000.zip" http://www.timeseriesclassification.com/Downloads/ECG5000.zip

