def get_client_count(clients):
    if clients.empty:
        return 0
    return len(clients)

def get_average_age(clients):
    if clients.empty:
        return 0
    return clients['age'].mean()

def get_city_with_most_clients(clients):
    if clients.empty:
        return None
    return (
        clients['city']
        .value_counts()
        .idxmax()
    )

def get_oldest_client(clients):
    if clients.empty:
        return None

    index = clients['age'].idxmax()
    return clients.loc[index]

def get_youngest_client(clients):
    if clients.empty:
        return None

    index = clients['age'].idxmin()
    return clients.loc[index]
