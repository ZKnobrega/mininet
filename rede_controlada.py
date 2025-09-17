#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import RemoteController  # Importante: Usaremos um controlador remoto
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def criar_rede_sdn():
    """Cria uma rede simples conectada a um controlador SDN externo."""

    # Usamos RemoteController para conectar ao Ryu que estará rodando na mesma máquina
    # O IP 127.0.0.1 significa "esta própria máquina"
    net = Mininet(controller=RemoteController('c0', ip='127.0.0.1', port=6633))

    info('*** Adicionando hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    info('*** Adicionando switch\n')
    s1 = net.addSwitch('s1')

    info('*** Criando links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Iniciando a rede\n')
    net.start()

    info('*** A rede está pronta. Execute a CLI.\n')
    CLI(net)

    info('*** Parando a rede\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    criar_rede_sdn()
