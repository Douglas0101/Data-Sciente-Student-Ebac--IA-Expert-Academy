usuario = 'andre.perez'
senha = 'andre123'

usuario_cadastro = 'andre.perez'
senha_cadastro = 'andre123'

usuario_igual  = usuario == usuario_cadastro
senha_igual = senha == senha_cadastro

print(usuario_igual)
print(senha_igual)

conceder_acesso = usuario_igual & senha_igual
print(conceder_acesso)

