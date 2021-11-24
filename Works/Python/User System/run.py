import register,login
while True:
    print("""
          1.Qeydiyyatdan keç
          2.Sisteme daxil ol
          3.Proqramdan cix
          """)
    
    
    emr=input('Seciminizi qeyd edin: ')
    
    if emr=='1':
        register.registerUser()
    elif emr=='2':
        login.userLogin(1)
    else:
        break