### Clone the Repository 
This command downloads your code to another computer:  

```bash
git clone https://github.com/IsaiasDev-commits/generador-contrase-as-python.git
```

---

### **Create a Virtual Environment and Install Dependencies**  
This prevents conflicts with other Python libraries on the system.  

- For Windows:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

- **For Mac/Linux:**  

  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

---

### Run the Server
To start the FastAPI application, use:  

```bash
uvicorn main:app --reload
```

This will launch the server at `http://127.0.0.1:8000/`.

---

### Test the API
Open your browser and visit:  

- **Swagger UI (interactive testing):**  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

- **Generate a password:**  
  [http://127.0.0.1:8000/generate_password](http://127.0.0.1:8000/generate_password)  

