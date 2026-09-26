class Category:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ledger = []

    def deposit(self, amount: int, description = ""):
        self.ledger.append({
            "amount": amount,
            "description": description})

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
          "amount": -amount,
          "description": description
        })
        return True
    
    def get_balance(self):
        balance = 0
        for n in self.ledger:
            balance += n["amount"]
        return balance
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
         return True
        else:
         return False
    
    def transfer(self,amount, category):
        if self.check_funds(amount):
           self.withdraw(amount, f"Transfer to {category.nombre}")
           category.deposit(amount, f"Transfer from {self.nombre}")
           return True
        return False
            
    def __str__(self):
        centrado = self.nombre.center(30, "*") + "\n"

        for n in self.ledger:
            centrado += n["description"][:23].ljust(23)
            centrado += f"{n['amount']:7.2f}" + "\n"

        total = f"Total: {self.get_balance():.2f}"
        return centrado + total
    
def create_spend_chart(categorias):

    gastos = []

    for n in categorias:
        gasto = 0

        for m in n.ledger:
            if m["amount"] < 0:
                gasto += abs(m["amount"])

        gastos.append(gasto)

    total_gastos = sum(gastos)

    porcentajes = []

    for gasto in gastos:
        porcentaje = (gasto / total_gastos) * 100
        redondear = (porcentaje // 10) * 10
        porcentajes.append(redondear)

    graficos = "Percentage spent by category\n"

    for nivel in range(100, -1, -10):
        linea = str(nivel).rjust(3) + "|"

        for porcentaje in porcentajes:
          linea += " o " if porcentaje >= nivel else "   "

        graficos += linea + " \n"

    linea_horizontal = "    " + ("-" * (len(categorias) * 3 + 1))
    graficos += linea_horizontal + "\n"

    longitudes = []

    for categoria in categorias:
        longitudes.append(len(categoria.nombre))

    longitud_maxima = max(longitudes)

    for i in range(longitud_maxima):
        fila_nombres = []

        for categoria in categorias:
            if i < len(categoria.nombre):
                fila_nombres.append(categoria.nombre[i])
            else:
                fila_nombres.append(" ")

        linea_nombres = "  ".join(fila_nombres) + "  "
        graficos += "     " + linea_nombres + "\n"

    return graficos.rstrip("\n")

    
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))