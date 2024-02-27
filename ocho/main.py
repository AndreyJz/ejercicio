import modulos.agplayer as ap
import modulos.menu as m
import modulos.partidosnovatos as p
import modulos.seguimiento as s
import modulos.resultados as r

Torneo={
    'Novato':{},
    'Intermedio':{},
    'Avanzado':{}
}
Partidos={}

if __name__ == '__main__' :
    isAppRuning = True
    while isAppRuning:
        op=m.Menu()
        if(op == 1):
            isAddPlayer = True
            while isAddPlayer:
                ap.os.system('cls')
                ap.addPlayer(Torneo)
                isAddPlayer = bool(input('Desea seguir agregando jugadores? S(si) o Enter(no)'))
        elif(op == 2):
            isAddGame = True
            while isAddGame:
                p.os.system('cls')
                p.AddGame(Torneo,Partidos)
                isAddGame = bool(input('Desea seguir agregando partidos? S(si) o Enter(no)'))
        elif(op == 3):
            isLookE = True
            while isLookE:
                s.os.system('cls')
                s.segPlayer(Torneo)
                isLookE = bool(input('Desea seguir mirando las estadisticas de este jugador? S(si) o Enter(no)'))
        elif(op == 4):
            isLookRes = True
            while isLookRes:
                r.os.system('cls')
                r.Results(Torneo)
                isLookRes = bool(input('Desea seguir mirando los ganadores del torneo? S(si) o Enter(no)'))
        elif(op == 5):
            isAppRuning=False
        