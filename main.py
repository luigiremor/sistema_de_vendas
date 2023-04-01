from cashier import Cashier
from manager import Manager
from cart import Cart
from product import Product
from system import System
from storage import Storage


if __name__ == '__main__':
    system = System()

    # Cria os produtos
    products = [
        Product('Camiseta', 50, 10),
        Product('Calça', 100, 10),
        Product('Meia', 10, 10),
        Product('Sapato', 200, 10),
        Product('Boné', 30, 10),
        Product('Óculos', 100, 10),
        Product('Relógio', 200, 10),
        Product('Bermuda', 50, 10),
        Product('Cueca', 20, 10),
    ]

    # Cria o estoque
    storage = Storage()
    for product in products:
        storage.add_product(product)

    # Cria o carrinho
    cart = Cart()

    system.add_cart(cart)
    system.add_storage(storage)


    is_running = True
    while is_running:
        is_logged = False
        while not is_logged:
            print(30 * '-=')
            print('Bem vindo ao sistema de vendas')
            print('1 - Login')
            print('2 - Cadastrar')
            print('3 - Sair')
            print(30 * '-=')

            option = int(input('Opção: '))
            if option == 1:
                username = input('Usuário: ')
                password = input('Senha: ')
                is_logged = system.login(username, password)
                if is_logged:
                    print('Login realizado com sucesso!')
                else:
                    print('Usuário ou senha inválidos!')
            elif option == 2:
                username = input('Usuário: ')
                password = input('Senha: ')
                is_admin = input('É administrador? (s/n): ')
                is_admin = is_admin.lower() == 's'
                if is_admin:
                    user = Manager(username, password)
                else:
                    user = Cashier(username, password)
                system.add_user(user)
                is_logged = system.login(username, password)
            elif option == 3:
                is_running = False
                break


        while is_logged:
            print(30 * '-=')
            print('1 - Consultar produto')
            print('2 - Adicionar produto')
            print('3 - Remover produto')
            print('4 - Adicionar produto ao carrinho')
            print('5 - Remover produto do carrinho')
            print('6 - Total do carrinho')
            print('7 - Listar carinho')
            print('8 - Sair')
            print(30 * '-=')

            option = int(input('Opção: '))

            if option == 1: # Consultar produto
                name = input('Nome do produto: ')
                product = system.consult_storage_product(name)
                if product:
                    print(product)
                else:
                    print('Produto não encontrado!')
            elif option == 2: # Adicionar produto
                if not system.user._is_admin:
                    print('Usuário não é administrador!')
                    continue
                name = input('Nome do produto: ')
                product = system.consult_storage_product(name)
                if product:
                    print('Produto já existe!')
                    is_update_qtd = input('Deseja adicionar? (s/n)')
                    if is_update_qtd.lower() == 's':
                        qtd = int(input('Quantidade: '))
                        system.insert_storage_product(product, qtd)
                else:
                    price = float(input('Preço: '))
                    qtd = int(input('Quantidade: '))
                    product = Product(name, price, qtd)
                    system.insert_storage_product(product)

            elif option == 3: # Remover produto
                if not system.user._is_admin:
                    print('Usuário não é administrador!')
                    continue
                name = input('Nome do produto: ')
                product = system.consult_storage_product(name)
                if product:
                    qtd = int(input('Deseja remover quantos?: '))
                    system.remove_storage_product(product, qtd)
                else:
                    print('Produto não encontrado!')
                    continue
                
            elif option == 4: # Adicionar produto ao carrinho
                name = input('Nome do produto: ')
                product = system.consult_storage_product(name)
                if product:
                    system.add_product_to_cart(product)
                else:
                    print('Produto não encontrado!')
            elif option == 5: # Remover produto do carrinho
                name = input('Nome do produto: ')
                product = system.consult_storage_product(name)
                if product:
                    system.remove_product_from_cart(product)
                else:
                    print('Produto não encontrado!')
            elif option == 6: # Total do carrinho
                print(f'Total: {system.total_cart()}')

            elif option == 7: # Listar carrinho
                products = system.list_cart()
                print(30 * '-=')
                print('Produtos no carrinho:')
                for product in products:
                    print(product)
                print(30 * '-=')

            elif option == 8: # Sair
                system.logout()
                is_logged = False

            