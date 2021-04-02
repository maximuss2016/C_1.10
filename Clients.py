from  classes import Visitors, Clients

client1 = Visitors("Иван", "Иваново", "турист")

client2 = Visitors("Иван", "Иваново", "турист")
client3 = Clients("Сергей", "Питер", "наставник")
client4 = Clients("Алексей", "Москва", "начальник")
client5 = Clients("Пётр", "Самара", "наставник")
client6 = Visitors("Саша", "Воронеж", "наставник")

clients = (client1,client2,client3,client4,client5,client6)

for client in clients:
    if isinstance(client, Clients) and client.get_status():
        client.get_list()

