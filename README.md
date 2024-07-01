# text-tone-analyzer
Analyze the tone of a text message

## Setup Instructions

### Backend

1. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the backend server:
    ```bash
    python app.py
    ```

Additionally, you can also do this to start the app:

```bash
cd ..
cd front
pnpm start-backend
```

### Frontend

1. Navigate to the `front` directory:
    ```bash
    cd front
    ```

2. Install the required packages using pnpm:
    ```bash
    pnpm install
    ```

3. Run the frontend development server:
    ```bash
    pnpm dev
    ```

Alternatively, you can run `build.bat` to install needed items.

### Running the Project

1. Ensure the backend server is running (see Backend section).
2. Ensure the frontend server is running (see Frontend section).
3. Open your browser and navigate to `http://localhost:5173` to use the application.