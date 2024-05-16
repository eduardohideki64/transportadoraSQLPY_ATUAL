import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="transportadora base"  
    )
except Exception as e:
    print(f'Erro ao conectar ao banco de dados: {e}')

def resposta_menu(menu):
    try:
        cursor = connection.cursor()

        if menu == 1:  # cadastrar pedido
            nome_produto = str(input("Digite o nome do produto: "))
            valor_sub = str(input("Digite o valor subtotal do produto: "))
            horario_pe = str(input("Digite o horário que a compra foi afetuada: "))
            status_pa = str(input("Digite qual foi a forma de pagamento: "))
            sql = "INSERT INTO pedido (nome_produto, subtotal, hora_pedido, pagamento) VALUES (%s, %s, %s, %s );"


            cursor.execute(sql, (nome_produto, valor_sub, horario_pe, status_pa))
            connection.commit()
            print("Pedido cadastrado no sistema.")


        elif menu == 2: # cadastrar transportadora
        
            endereco_entrega = str(input("Digite o endereço de entrega: "))
            modo_envio = str(input("Digite a forma escolhida de envio: "))
            transportadora = str(input("Digite qual é a transportadora responsavel: "))
            cod_rastreio = str(input("Digite o código de rastreio do seu produto: "))
            sql = "INSERT INTO transportadora (endereco_entrega, modo_envio, transportadora, cod_rastreio ) VALUES (%s, %s, %s, %s);"


            cursor.execute(sql, ( endereco_entrega,  modo_envio, transportadora, cod_rastreio))
            connection.commit()
            print("Envio Transportadora cadastrado no sistema.")


        elif menu == 3: # cadastrar entrega
            id_entrega = str(input("ID da entrega/envio "))
            status_envio = str(input("Digite o status do envio: "))
            transportadora = str(input("Digite qual é a transportadora responsavel: "))
            sql = "INSERT INTO entrega (id_entrega, status_envio, transportadora) VALUES (%s, %s, %s);"


            cursor.execute(sql, (id_entrega, status_envio, transportadora))
            connection.commit()
            print("Entrega cadastrada no sistema.")

        elif menu == 4: #listar pedido
                    cursor = connection.cursor()
                    cursor.execute("SELECT * FROM pedido")
                    print("Pedidos:")
                    for pedido in cursor:
                        print(pedido)  # Isso imprimirá cada linha como uma tupla
                        cursor.close()
                        connection.close()
                    
        
        elif menu == 5: #listar transportadora
                    cursor = connection.cursor()
                    cursor.execute("SELECT * FROM transportadora")
                    print("Transporte:")
                    for transporte in cursor:
                        print(transporte)  # Isso imprimirá cada linha como uma tupla
                        cursor.close()
                        connection.close()
                
        elif menu == 5: #listar entrega
                    cursor = connection.cursor()
                    cursor.execute("SELECT * FROM entrega")
                    print("Entregas:")
                    for entrega in cursor:
                        print(entrega)  # Isso imprimirá cada linha como uma tupla
                        cursor.close()
                        connection.close()

               
        elif menu == 6: #deletar entrega pelo id
                identrega = int(input("Digite o ID da entrega que quer deletar: "))
                sql = "DELETE FROM entrega WHERE id_entrega = %s;"


                cursor.execute(sql, (identrega,))
                connection.commit()
                print("Entrega deletada com sucesso!")

                    
        elif menu == 7: #deletar transporte por cod_rastreio
                transporte = int(input("Digite o cod_rastreio do transporte que quer deletar: "))
                sql = "DELETE FROM transportadora WHERE cod_rastreio = %s;"


                cursor.execute(sql, (transporte,))
                connection.commit()
                print("Transporte deletado com sucesso!")

                    
        elif menu == 8: #deletar pedido por id
                idpedido = int(input("Digite o cod_rastreio do pedido que quer deletar: "))
                sql = "DELETE FROM pedido WHERE cod_rastreio = %s;"


                cursor.execute(sql, (idpedido,))
                connection.commit()
                print("Pedido deletado com sucesso!")

        
        elif menu == 9: #UPDATE no banco de dados
                new_envio = str(input("Digite novo status de envio que deseja alterar: "))
                customer_id = int(input("Digite o id de qual cliente deseja alterar: "))
                sql = "UPDATE entrega SET status_envio = %s WHERE id_entrega = %s;"
                cursor = connection.cursor()
                cursor.execute(sql, ( new_envio, customer_id))
                connection.commit()
                print("Status alterado.")
        
        

    
        else:
            print("Opção inválida")
    except Exception as e:
        print(f'Erro ao executar operação: {e}')
    finally:
        cursor.close()

def main():
    menu = int(input("Digite a operação: "))
    resposta_menu(menu)
    connection.close()

    
    # Esta linha verifica se o script está sendo executado como o programa principal. Em Python, o atributo __name__ de um módulo é uma variável especial que contém o nome do módulo.
    #Se o módulo estiver sendo executado como o programa principal, o valor de __name__ será "__main__".
    #no caso, o módulo é a myssql.connector
if __name__ == "__main__":
    main()


    #feliz porque esse código deu certoooooo(apenas o item 1 até momento). Vou fazer mais comentários









