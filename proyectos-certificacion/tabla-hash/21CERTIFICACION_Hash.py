class HashTable:
    def __init__(self):
        self.collection = {}

    def hash (self,cadena: str) -> int:
        obtener_total = 0

        for n in cadena:
            obtener = ord(n)
            obtener_total = obtener_total + obtener 
        return obtener_total

    def add (self, clave: str, valor: str) -> None:
        hash_clave = self.hash(clave)

        if hash_clave not in self.collection:
            self.collection[hash_clave] = {}

        self.collection[hash_clave][clave] = valor


    def remove (self,clave: str) -> None:
        remove_clave = self.hash(clave)

        if remove_clave in self.collection:
         if clave in self.collection[remove_clave]:
          del self.collection[remove_clave][clave]

    def lookup (self, clave: str):
        lookup_clave = self.hash(clave)
        
        if lookup_clave not in self.collection:
            return None

        if clave not in self.collection[lookup_clave]:
            return None
        
        return self.collection[lookup_clave][clave]


    

tabla = HashTable()
print(tabla.add("golf", "sport"))

print(tabla.hash("golf"))
tabla.add("fcc", "coding")
tabla.add("cfc", "chemical")

print(tabla.collection)
print(tabla.lookup("golf"))
tabla.remove("golf")
print(tabla.collection)

tabla.remove("fcc")
print(tabla.collection)

print(tabla.lookup("fcc"))
print(tabla.lookup("cfc"))