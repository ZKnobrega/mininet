from pox.core import core
import pox.web.webcore as webcore
from pox.lib.util import dpid_to_str

# Obtém o logger para registrar informações, o que é uma boa prática
log = core.getLogger()

class NetworkViewHandler(webcore.BaseHandler):
    def _handle_GET(self):
        self.response.content_type = 'text/html'

        # Começa a construir o corpo do HTML
        body = """
        <html>
          <head>
            <title>Visualizacao da Rede SDN</title>
            <style>
              body { font-family: sans-serif; }
              h1 { color: #333; }
              h2 { color: #555; border-bottom: 1px solid #ccc; }
              ul { list-style-type: none; padding-left: 20px; }
              li { background: #f4f4f4; margin: 5px; padding: 8px; border-radius: 5px; }
              .dpid { color: #0056b3; font-weight: bold; }
              .port { color: #28a745; }
            </style>
          </head>
          <body>
            <h1>Estado da Rede (Visao do Controlador POX)</h1>
        """

        # Acessa o núcleo do OpenFlow para obter a lista de conexões (switches)
        connections = core.openflow.connections

        if not connections:
            body += "<p>Nenhum switch conectado no momento.</p>"
        else:
            body += f"<p>Detectado(s) {len(connections)} switch(es).</p>"
            # Itera sobre cada switch conectado
            for connection in connections.values():
                dpid_str = dpid_to_str(connection.dpid)
                body += f"<h2>Switch <span class='dpid'>{dpid_str}</span></h2>"

                if not connection.features or not connection.features.ports:
                    body += "<p>Nao foi possivel obter as portas do switch.</p>"
                else:
                    body += "<ul>"
                    # Itera sobre as portas de cada switch
                    for port in connection.features.ports:
                        body += f"<li>Porta <span class='port'>#{port.port_no}</span>: {port.name.decode()}</li>"
                    body += "</ul>"

        body += """
          </body>
        </html>
        """
        self.response.write(body)

def launch():
    # Renomeamos o manipulador e a URL para serem mais descritivos
    core.WebServer.set_handler("/network_view", NetworkViewHandler)
    log.info("Painel da Rede registrado em /network_view")
