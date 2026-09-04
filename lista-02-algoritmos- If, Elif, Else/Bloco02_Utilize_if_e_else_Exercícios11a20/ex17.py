# 17) Verificação de senha. Defina uma senha fixa no código ("python123"). Leia a tentativa do usuário e informe se o acesso foi permitido ou negado.

senha = input("Digite sua senha: ")
if senha == 'python123':
    print('Acesso permitido!')
else:
    print('Acesso negado!')
