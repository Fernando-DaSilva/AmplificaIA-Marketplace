"""
run.py - Script de Execução do Servidor FastAPI
Uso: python run.py
"""

import uvicorn

if __name__ == "__main__":
    print("==========================================================")
    print(" AmplificaIA Marketplace White-Label (FastAPI + HTMX)")
    print(" Servidor rodando em: http://127.0.0.1:8050")
    print("==========================================================")
    uvicorn.run("main:app", host="0.0.0.0", port=8050, reload=True)
