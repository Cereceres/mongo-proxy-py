# Test

```bash
python -m unittest discover -v -s test -p "*_test.py"
```

# Install 

```bash
pip install -r requirements.txt  
```

# API

## GET /collection/ip
it is mapped to query= string_query || {_id: id}
## PUT /collection/id
it is mapped to query= string_query || {_id: id}, the update is obtained from body request
## POST /collection/ip
the data is obtained from body request
## DELETE /collection/ip
it is mapped to query= string_query || {_id: id}



