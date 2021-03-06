''' ----------------------------------------------------------------------
SSLCAUDIT - a tool for automating security audit of SSL clients
Released under terms of GPLv3, see COPYING.TXT
Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
---------------------------------------------------------------------- '''

from src.ClientAuditor.ClientConnectionAuditEvent import ClientConnectionAuditResult
from src.ClientAuditor.ClientConnectionAuditor import  ClientConnectionAuditor

class DummyClientConnectionAuditor(ClientConnectionAuditor):
    '''
    This dummy profile does nothing, but returns DummyClientConnectionResult.
    '''

    def __init__(self, dummy_result):
        ClientConnectionAuditor.__init__(self, dummy_result)
        self.dummy_result = dummy_result

    def handle(self, conn):
        return ClientConnectionAuditResult(self, conn.get_client_id(), self.dummy_result)
