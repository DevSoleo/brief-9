print("ok

target = -5
num = 3

target =- num  # Noncompliant; target = -3. Is that really what's meant?
target =+ num # Noncompliant; target = 3
      
jwt.decode(token, verify = False)  # Noncompliant
jwt.decode(token, key, options={"verify_signature": False})  # Noncompliant
