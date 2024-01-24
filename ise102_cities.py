cities = {
  'Giresun': ['Trabzon', 'Gumushane','Erzurum'],
  'Trabzon': ['Giresun','Gumushane', 'Bayburt', 'Rize'],
  'Gumushane': ['Giresun', 'Trabzon', 'Bayburt','Erzincan'],
  'Erzincan': ['Giresun', 'Gumushane','Bayburt','Erzurum','Bingol','Tunceli'],
  'Tuncelı': ['Erzincan','Bingol'],
  'Bayburt': ['Gumushane','Trabzon','Rize','Erzurum','Erzincan'],
  'Bingol': ['Tunceli', 'Erzincan','Erzurum','Mus'],
  'Rize' : ['Trabzon','Bayburt','Erzurum','Artvin'],
  'Erzurum' : ['Rize','Artvin','Ardahan', 'Kars','Agri','Mus','Bingol','Erzincan','Bayburt'],
  'Mus' : ['Bingol','Erzurum','Agri'],
  'Artvin' : ['Rize','Erzurum','Ardahan'],
  'Ardahan' : ['Artvin', 'Erzurun','Kars'],
  'Kars' : ['Ardahan','Erzurum','Agri','Igdir'],
  'Agri' : ['Kars', 'Erzurum','Mus','Igdir'],
  'Igdir' : ['Kars','Agri']
  }

def hops(cities, start, end, visited):
    if start == end:
        return 0
    smallest = float('inf')     # infinity
    visited.append(start)
    for a_city in cities[start]:
        if a_city not in visited:
            city_hop = hops(cities, a_city, end, visited)
            smallest = min(smallest, city_hop + 1)
    return smallest

vizi= []
print(hops(cities,'Giresun','Agri',vizi))