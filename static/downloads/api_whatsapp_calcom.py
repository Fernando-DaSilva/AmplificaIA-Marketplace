"""
AmplificaIA API Connector: WhatsApp + Cal.com / Google Calendar
Serviço microservice em Python/FastAPI para sincronizar agendamentos de clínicas e consultórios.
"""

import requests
from typing import Dict, Any

class WhatsAppCalendarSyncAPI:
    def __init__(self, api_key: str, whatsapp_instance: str):
        self.api_key = api_key
        self.whatsapp_instance = whatsapp_instance

    def enviar_confirmacao_agendamento(self, telefone: str, nome: str, data_hora: str, procedimento: str) -> Dict[str, Any]:
        mensagem = (
            f"Olá *{nome}*! 👋\n\n"
            f"Seu agendamento para *{procedimento}* foi confirmado com sucesso!\n"
            f"📅 Data/Hora: *{data_hora}*\n\n"
            f"Caso precise remarcar, responda a esta mensagem com 'REMARCAR'."
        )
        payload = {
            "phone": telefone,
            "message": mensagem
        }
        print(f"[API WhatsApp] Simulando envio para {telefone}: {mensagem[:40]}...")
        return {"status": "success", "message_id": "msg_9981247", "recipient": telefone}

if __name__ == "__main__":
    api = WhatsAppCalendarSyncAPI(api_key="demo_key_amplifica_ia", whatsapp_instance="inst_001")
    api.enviar_confirmacao_agendamento("5511999998888", "Dra. Ana Silva", "25/09 às 14:00", "Consulta Avaliação")
