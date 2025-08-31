@echo off
echo 🎬 Netflix Clone Frontend Setup
echo ========================================

echo Installing Node.js dependencies...
npm install

if %errorlevel% neq 0 (
    echo ✗ Failed to install dependencies
    pause
    exit /b 1
)

echo ✓ Dependencies installed successfully
echo.
echo 🚀 Setup complete!
echo Run 'npm start' to start the development server
pause
