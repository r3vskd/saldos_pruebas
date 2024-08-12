from colorama import Fore, Style, init

init(autoreset=True)

def display_banner():
    print(Fore.CYAN + '''
 ██████╗ █████╗ ▄▄███▄▄·██╗  ██╗     █████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██║  ██║    ██╔══██╗██╔══██╗██╔══██╗
██║     ███████║███████╗███████║    ███████║██████╔╝██████╔╝
██║     ██╔══██║╚════██║██╔══██║    ██╔══██║██╔═══╝ ██╔═══╝ 
╚██████╗██║  ██║███████║██║  ██║    ██║  ██║██║     ██║     
 ╚═════╝╚═╝  ╚═╝╚═▀▀▀══╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝                                                                
          ''' + Style.RESET_ALL)

class asignar_valores:
    def __init__(self, titular, cuenta, saldo): # creeando los atributos
         self.titular = titular
         self.cuenta = cuenta
         self.saldo = saldo # asignar el saldo especifico a cada cuenta
             
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"{cantidad} pesos depositados a {self.titular} (El saldo actual de la cuenta {self.cuenta} es: {self.saldo})")
        
    def retirar(self, cantidad):
        if cantidad <= self.saldo: # si la cantidad que se va a operar es menor o igual a la que tiene la cuenta, se procede con la operacion
            self.saldo -= cantidad
            print(f"{cantidad} fue retirada de la cuenta de: {self.titular} (Correspondiente al numero de cuenta: {self.cuenta} el saldo actual es: {self.saldo})")
        else:
            print(f"Saldo insuficiente en la cuenta de {self.titular} con el numero de cuenta {self.cuenta} para hacer un retiro.") # de cualquier ota forma se muestra que no hay saldo suficienteen la cuenta
        
    def mostrar(self):
        return f"La cuenta {self.cuenta} con el nombre {self.titular}, tiene un saldo actual de: {self.saldo}"
    
class cuenta_digital:
    display_banner()
    
    def __init__(self):
        self.cuenta_jo = asignar_valores("Jose", "0001", 100) # titular, cuenta y saldo (seteando los atributosa self)
        self.cuenta_mi = asignar_valores("Miguel", "0002", 120)
        self.cuenta_ke = asignar_valores("Kevin", "0003", 80)
        
    def preguntar(self):
        for _ in range(3):
            cuenta = input("Ingresa el numero de cuenta, ya sea 0001, 0002 o 0003): ").strip()
            operacion = input("Deseas depositar o retirar? (ingresa depositar o retirar): ").strip().lower()
            cantidad = int(input("Ingresa la cantidad: "))
            
            # Arregle un bug en el que no me reconocia la variable "cuenta_select"
            cuenta_select = None
            
            # sleccionando el objeto basandose en la cuenta seleccionada por el ususario
            if cuenta == self.cuenta_jo.cuenta:
                cuenta_select = self.cuenta_jo
                
            elif cuenta == self.cuenta_ke.cuenta:
                cuenta_select = self.cuenta_ke
            
            elif cuenta == self.cuenta_mi.cuenta:
                cuenta_select = self.cuenta_mi
                
            else:
                print("Numero de cuenta invalido, Por favor intente de nuevo.")
                continue
            
            if cuenta_select:
                if operacion == "depositar":
                    cuenta_select.depositar(cantidad)
                elif operacion == "retirar":
                    cuenta_select.retirar(cantidad)
                else:
                    print("Operacion invalida, por favor, escribe 'depositar' o 'retirar' ")
            
            else:
                print("Numero de cuenta no valido para esta operacion")
                
# Instanciando el objeto para los saldos de las cuentas, nombres y numeros de cuenta                
instancia = cuenta_digital()

# Instanciando el objeto para pedir datos de entrada
instancia.preguntar()

# Mostrando los saldos actualizados de todos las cuentas
print(instancia.cuenta_jo.mostrar())
print(instancia.cuenta_ke.mostrar())
print(instancia.cuenta_mi.mostrar())      
