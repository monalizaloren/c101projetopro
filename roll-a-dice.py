import random 
  
# Use uma variável para armazenar a resposta para continuar jogando o dado
response = "y"
   
while response == "y": 
      
    # Gere um número aleatório 
    # entre 1 e 6 (incluindo 
    # os números 1 e 6) 
    no = random.randint(1,6) 

    # condições para verificar o valor numérico  
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 
          
    # Peça para o usuário informar uma resposta      
    response=input("Pressione y para jogar novamente e n para sair:") 
    print("\n") 