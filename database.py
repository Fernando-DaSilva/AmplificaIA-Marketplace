"""
database.py - Banco de Dados de Exemplo para o AmplificaIA Marketplace White-Label
Contém configurações de Tenants (marcas white-label), categorias de negócios, tipos de IA e catálogo de produtos.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel

class Tenant(BaseModel):
    id: str
    name: str
    tagline: str
    logo_text: str
    accent_color: str
    banner_title: str
    banner_subtitle: str

TENANTS: Dict[str, Tenant] = {
    "amplifica_ia": Tenant(
        id="amplifica_ia",
        name="AmplificaIA Marketplace",
        tagline="Sua Vitrine Oficial de Soluções e Automações de Inteligência Artificial",
        logo_text="AmplificaIA",
        accent_color="indigo",
        banner_title="Marketplace de Automações & Ativos de IA",
        banner_subtitle="Prompts, Skills, Servidores MCP, Agentes AI e APIs prontos para impulsionar seus clientes e seu negócio."
    ),
    "lawtech_ai": Tenant(
        id="lawtech_ai",
        name="LegalTech AI Store",
        tagline="Inteligência Artificial de Alta Performance para Advocacia e Jurídico",
        logo_text="LegalTech AI",
        accent_color="amber",
        banner_title="Soluções de IA para escritórios Jurídicos",
        banner_subtitle="Maximize a produtividade na elaboração de peças, análise contratual e triagem de processos."
    ),
    "beauty_hub": Tenant(
        id="beauty_hub",
        name="Beauty & Barber AI Store",
        tagline="Tecnologia de Automação para Barbearias e Salões de Beleza",
        logo_text="BeautyAI",
        accent_color="pink",
        banner_title="Agendamentos & Upsell Automatizados",
        banner_subtitle="Agentes de IA e fluxos WhatsApp para lotar a agenda da sua barbearia ou salão."
    ),
    "accountant_ia": Tenant(
        id="accountant_ia",
        name="Contábil IA Hub",
        tagline="Aceleração Fiscal e Contábil powered by AI",
        logo_text="ContábilIA",
        accent_color="emerald",
        banner_title="Automação Inteligente para Contadores",
        banner_subtitle="Auditoria de balancetes, triagem de notas e apuração de tributos em segundos."
    )
}

PRODUCT_TYPES = {
    "Prompt": {"label": "Prompt", "color": "bg-blue-500/10 text-blue-400 border-blue-500/30", "icon": "fa-terminal"},
    "Skill": {"label": "Skill", "color": "bg-purple-500/10 text-purple-400 border-purple-500/30", "icon": "fa-wand-magic-sparkles"},
    "MCP": {"label": "MCP Server", "color": "bg-emerald-500/10 text-emerald-400 border-emerald-500/30", "icon": "fa-plug-zap"},
    "Agente AI": {"label": "Agente AI", "color": "bg-amber-500/10 text-amber-400 border-amber-500/30", "icon": "fa-robot"},
    "API": {"label": "API Connector", "color": "bg-cyan-500/10 text-cyan-400 border-cyan-500/30", "icon": "fa-network-wired"}
}

CATEGORIES = [
    {"id": "all", "name": "Todas as Soluções", "icon": "fa-border-all"},
    {"id": "Advogados", "name": "Advogados & Jurídico", "icon": "fa-scale-balanced"},
    {"id": "Barbearias e Salões", "name": "Barbearias & Salões", "icon": "fa-scissors"},
    {"id": "Contadores", "name": "Contadores & Fiscal", "icon": "fa-calculator"},
    {"id": "Dentistas", "name": "Dentistas & Odonto", "icon": "fa-tooth"},
    {"id": "Vendas e Comercial", "name": "Vendas & Comercial", "icon": "fa-chart-line"},
    {"id": "Imobiliárias", "name": "Imobiliárias & Corretores", "icon": "fa-building"},
    {"id": "Médicos e Clínicas", "name": "Médicos & Clínicas", "icon": "fa-user-nurse"},
    {"id": "E-commerce", "name": "E-commerce & Varejo", "icon": "fa-cart-shopping"}
]

PRODUCTS = [
    {
        "id": "prod-009",
        "title": "Agente SDR de Vendas AI: Qualificação BANT & Agendamento de Reuniões",
        "type": "Agente AI",
        "category": "Vendas e Comercial",
        "image_url": "https://images.unsplash.com/photo-1556745757-8d76bdb6984b?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Agente autônomo SDR para filtrar leads por perfil (orçamento, prazo e necessidade) e agendar reuniões direto na agenda dos vendedores.",
        "detailed_desc": "Solução autônoma completa de pré-vendas (SDR). Atende leads inbound no WhatsApp e Webchat em menos de 10 segundos, qualifica o prospect através da metodologia BANT (Budget, Authority, Need, Timeline), tira dúvidas comerciais frequentes e realiza o agendamento de reuniões diretamente no Calendly/Google Calendar dos vendedores (Closers).",
        "solutions_executed": [
            "Atendimento imediato em <10s eliminando a perda de leads por demora no contato.",
            "Qualificação rigorosa BANT antes de transferir o lead para o vendedor humano.",
            "Agendamento automático de reuniões com distribuição Round-Robin entre o time de vendas.",
            "Criação automática de oportunidade no CRM (HubSpot / Pipedrive) e notificação no Slack."
        ],
        "included_files": [
            {"name": "agente_sdr_vendas.json", "size": "28 KB", "type": "JSON Workflow Spec", "path": "/static/downloads/agente_sdr_vendas.json"},
            {"name": "manual_sdr_ia.pdf", "size": "1.8 MB", "type": "PDF Documentation", "path": "/static/downloads/agente_sdr_vendas.json"}
        ],
        "price": 329.00,
        "featured": True,
        "rating": 5.0,
        "sales_count": 489,
        "requirements": "n8n / Flowise ou Servidor Python, Conector Calendly + API WhatsApp."
    },
    {
        "id": "prod-001",
        "title": "Prompt Master: Triagem Jurídica & Esboço de Petição Inicial",
        "type": "Prompt",
        "category": "Advogados",
        "image_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Prompt estruturado para ler depoimentos de clientes e gerar minutagem jurídica completa com enquadramento no CPC e CLT.",
        "detailed_desc": "Pacote profissional contendo prompts mestres em formato JSON e Markdown testados para GPT-4o e Claude 3.5 Sonnet. Transforma relatos informais via áudio ou texto de clientes em um primeiro rascunho de petição com tópicos dos fatos, direito e pedidos de tutela.",
        "solutions_executed": [
            "Redução do tempo de redação de iniciais de 4 horas para 15 minutos.",
            "Detecção automática de prazos prescricionais e requisitos legais obrigatórios.",
            "Formatação pronta para importação direta no PJe, e-SAJ e PROJUDI.",
            "Inclusão de variáveis personalizáveis por área jurídica (Trabalhista, Família, Cível e Tributário)."
        ],
        "included_files": [
            {"name": "prompt_advogados_peticao.json", "size": "14 KB", "type": "JSON Prompt Spec", "path": "/static/downloads/prompt_advogados_peticao.json"},
            {"name": "guia_uso_prompts_juridicos.pdf", "size": "1.2 MB", "type": "PDF Documentation", "path": "/static/downloads/prompt_advogados_peticao.json"}
        ],
        "price": 147.00,
        "featured": True,
        "rating": 4.9,
        "sales_count": 342,
        "requirements": "Funciona em qualquer assistente de IA (ChatGPT, Claude, Antigravity, Copilot)."
    },
    {
        "id": "prod-002",
        "title": "MCP Server: Agendamento Automático via WhatsApp para Barbearias",
        "type": "MCP",
        "category": "Barbearias e Salões",
        "image_url": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Servidor MCP pronto para conectar assistentes de IA diretamente com agendas do WhatsApp e sistemas de barbearia.",
        "detailed_desc": "Conector nativo do protocolo MCP (Model Context Protocol). Permite que qualquer agente autônomo consulte disponibilidade de horários por barbeiro, realize reservas, remarcações e envie lembretes automáticos 2 horas antes do atendimento.",
        "solutions_executed": [
            "Atendimento 24/7 de agendamento sem intervenção humana no WhatsApp.",
            "Eliminação de faltas (no-show) em até 65% com lembretes inteligentes.",
            "Sincronização bidirecional com Google Calendar e Trinks/BarberApp.",
            "Oferecimento de serviços adicionais (Barba, Hidratação, Barboterapia) no momento do atendimento."
        ],
        "included_files": [
            {"name": "mcp_barbearia_agendamento.json", "size": "8 KB", "type": "MCP Spec", "path": "/static/downloads/mcp_barbearia_agendamento.json"},
            {"name": "servidor_mcp_barbearia.zip", "size": "4.5 MB", "type": "ZIP Source Code", "path": "/static/downloads/mcp_barbearia_agendamento.json"}
        ],
        "price": 297.00,
        "featured": True,
        "rating": 5.0,
        "sales_count": 189,
        "requirements": "Node.js 18+ ou Python 3.10+, Token de WhatsApp API (Evolution, Z-API ou Oficial)."
    },
    {
        "id": "prod-003",
        "title": "Skill IA: Análise Fiscal, DRE e Auditoria de Balancetes",
        "type": "Skill",
        "category": "Contadores",
        "image_url": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Skill de análise avançada para agentes de IA inspecionarem balancetes, alíquotas do Simples Nacional e prevenirem autuações.",
        "detailed_desc": "Habilidade especializada desenvolvida para integrar em assistentes contábeis. Processa extratos de balancetes mensais, identifica erros em lançamentos contábeis, sugere o melhor anexo fiscal do Simples e gera relatórios executivos para envio ao cliente final.",
        "solutions_executed": [
            "Varredura automática de divergências de lançamentos em segundos.",
            "Cálculo automatizado do Fator R para empresas enquadradas no Simples Nacional.",
            "Geração de parecer técnico visual em Markdown/PDF com destaques de alerta.",
            "Histórico comparativo de evolução de despesas e lucratividade."
        ],
        "included_files": [
            {"name": "skill_contador_fiscal.md", "size": "18 KB", "type": "Skill Markdown", "path": "/static/downloads/skill_contador_fiscal.md"},
            {"name": "modelos_balancete_exemplo.csv", "size": "45 KB", "type": "CSV Sample Data", "path": "/static/downloads/skill_contador_fiscal.md"}
        ],
        "price": 249.00,
        "featured": True,
        "rating": 4.8,
        "sales_count": 215,
        "requirements": "Compatível com Antigravity SDK, Claude Code, OpenAI Assistants API e LangChain."
    },
    {
        "id": "prod-004",
        "title": "Agente AI: Triagem Odontológica & Anamnese Pré-Consulta",
        "type": "Agente AI",
        "category": "Dentistas",
        "image_url": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Agente inteligente autônomo para clínicas dentárias realizar anamnese prévia e agendamento de consultas pelo WhatsApp.",
        "detailed_desc": "Fluxo autônomo completo com lógica de conversação humanizada para clínicas odontológicas. O agente qualifica o sintoma (dor aguda, canal, aparelho ortodôntico, estética), preenche a ficha de anamnese antes do paciente chegar e avisa o dentista responsável.",
        "solutions_executed": [
            "Coleta automatizada de histórico de saúde e alergias medicamentosas.",
            "Encaminhamento prioritário imediato para casos de dor aguda/urgência.",
            "Lembrete automático pré e pós-procedimento com instruções de cuidados (ex: pós-siso).",
            "Integração com calendários e sistemas de gestão médica/odontológica."
        ],
        "included_files": [
            {"name": "agente_dentista_triagem.json", "size": "32 KB", "type": "JSON Workflow Spec", "path": "/static/downloads/agente_dentista_triagem.json"},
            {"name": "pacote_agente_n8n_flowise.zip", "size": "2.8 MB", "type": "ZIP Package", "path": "/static/downloads/agente_dentista_triagem.json"}
        ],
        "price": 389.00,
        "featured": True,
        "rating": 4.9,
        "sales_count": 156,
        "requirements": "Instância n8n / Flowise ou Servidor Python + Webhook WhatsApp."
    },
    {
        "id": "prod-005",
        "title": "API Connector: Sincronizador WhatsApp + Cal.com para Clínicas",
        "type": "API",
        "category": "Médicos e Clínicas",
        "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80",
        "short_desc": "API de alta performance para orquestrar lembretes de consultas médicas e confirmações instantâneas via WhatsApp.",
        "detailed_desc": "Microserviço em Python/FastAPI pronto para deploy. Conecta seu sistema de gestão médica (ou Google Calendar / Cal.com) à API do WhatsApp. Permite confirmações com botão 'Sim/Não' e atualização em tempo real na agenda do médico.",
        "solutions_executed": [
            "Confirmação automática de presença com 24h e 2h de antecedência.",
            "Liberação instantânea da vaga na agenda se o paciente cancelar.",
            "Envio automatizado do link de localização e mapa do consultório.",
            "Suporte a múltiplas filiais e médicos no mesmo servidor."
        ],
        "included_files": [
            {"name": "api_whatsapp_calcom.py", "size": "12 KB", "type": "Python API Script", "path": "/static/downloads/api_whatsapp_calcom.py"},
            {"name": "docker-compose.yml", "size": "2 KB", "type": "Docker Config", "path": "/static/downloads/api_whatsapp_calcom.py"}
        ],
        "price": 199.00,
        "featured": False,
        "rating": 4.7,
        "sales_count": 98,
        "requirements": "Python 3.10+ ou Docker, Chave API Cal.com / WhatsApp API."
    },
    {
        "id": "prod-006",
        "title": "Prompt Master: Avaliador de Imóveis & Gerador de Anúncios de Alto Padrão",
        "type": "Prompt",
        "category": "Imobiliárias",
        "image_url": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Prompts para corretores criarem descrições persuasivas de imóveis para portais e qualificar leads pelo perfil financeiro.",
        "detailed_desc": "Conjunto avançado de prompts de copywriting imobiliário e inteligência comercial. Analisa características do imóvel (metragem, bairro, acabamento) e gera copy otimizada para Instagram, Zap Imóveis, OLX e e-mail marketing.",
        "solutions_executed": [
            "Criação de textos de venda atraentes em menos de 1 minuto por imóvel.",
            "Sugestão de precificação média baseada no m² do bairro informado.",
            "Roteiro de perguntas de qualificação para o corretor identificar se o lead possui financiamento pré-aprovado."
        ],
        "included_files": [
            {"name": "prompt_imobiliaria_lead.json", "size": "16 KB", "type": "JSON Prompt Pack", "path": "/static/downloads/prompt_advogados_peticao.json"}
        ],
        "price": 97.00,
        "featured": False,
        "rating": 4.8,
        "sales_count": 410,
        "requirements": "Qualquer modelo de linguagem (GPT, Claude, Gemini)."
    },
    {
        "id": "prod-007",
        "title": "MCP Server: Protocolo Jurídico de Consulta ao Jusbrasil & PJe",
        "type": "MCP",
        "category": "Advogados",
        "image_url": "https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?auto=format&fit=crop&w=800&q=80",
        "short_desc": "Servidor MCP para agentes de IA realizarem pesquisas de jurisprudência e andamento de processos de forma automática.",
        "detailed_desc": "Conector avançado de MCP para escritórios de advocacia. Conecta seu assistente virtual aos bancos de dados de jurisprudência dos Tribunais (STJ, STF, TJSP, TRT) para trazer precedentes citáveis diretamente na redação da petição.",
        "solutions_executed": [
            "Busca acelerada de acórdãos e súmulas aplicáveis ao caso.",
            "Resumo automático das últimas movimentações processuais do cliente.",
            "Alerta de publicação em diários oficiais diretamente no painel do advogado."
        ],
        "included_files": [
            {"name": "mcp_juridico_jusbrasil.json", "size": "15 KB", "type": "MCP Server Spec", "path": "/static/downloads/mcp_barbearia_agendamento.json"}
        ],
        "price": 349.00,
        "featured": True,
        "rating": 5.0,
        "sales_count": 275,
        "requirements": "Node.js 18+ ou Python, Token de API de Dados Jurídicos."
    }
]

def get_tenant(tenant_id: str) -> Tenant:
    return TENANTS.get(tenant_id, TENANTS["amplifica_ia"])

def list_products(category: Optional[str] = None, ptype: Optional[str] = None, search: Optional[str] = None) -> List[dict]:
    items = PRODUCTS
    if category and category != "all":
        items = [p for p in items if p["category"].lower() == category.lower()]
    if ptype and ptype != "all":
        items = [p for p in items if p["type"].lower() == ptype.lower()]
    if search:
        s = search.lower()
        items = [
            p for p in items 
            if s in p["title"].lower() or s in p["short_desc"].lower() or s in p["category"].lower() or s in p["type"].lower()
        ]
    return items

def get_product(product_id: str) -> Optional[dict]:
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None
