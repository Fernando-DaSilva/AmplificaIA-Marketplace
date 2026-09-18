"""
cart.py - Gerenciamento de Carrinho de Compras e Processamento de Pedidos (Simulado)
"""

import uuid
from typing import Dict, List, Any, Optional
from database import get_product

# Armazenamento em memória de carrinhos por sessão
CARTS: Dict[str, Dict[str, int]] = {}
ORDERS: Dict[str, Dict[str, Any]] = {}

def get_cart(session_id: str) -> Dict[str, Any]:
    if session_id not in CARTS:
        CARTS[session_id] = {}
    
    raw_cart = CARTS[session_id]
    items = []
    total = 0.0
    
    for pid, qty in raw_cart.items():
        product = get_product(pid)
        if product:
            subtotal = product["price"] * qty
            total += subtotal
            items.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal
            })
            
    return {
        "cart_items": items,
        "item_count": sum(raw_cart.values()),
        "total": total
    }

def add_to_cart(session_id: str, product_id: str) -> Dict[str, Any]:
    if session_id not in CARTS:
        CARTS[session_id] = {}
    
    CARTS[session_id][product_id] = CARTS[session_id].get(product_id, 0) + 1
    return get_cart(session_id)

def remove_from_cart(session_id: str, product_id: str) -> Dict[str, Any]:
    if session_id in CARTS and product_id in CARTS[session_id]:
        del CARTS[session_id][product_id]
    return get_cart(session_id)

def update_quantity(session_id: str, product_id: str, quantity: int) -> Dict[str, Any]:
    if session_id in CARTS:
        if quantity <= 0:
            remove_from_cart(session_id, product_id)
        else:
            CARTS[session_id][product_id] = quantity
    return get_cart(session_id)

def clear_cart(session_id: str):
    if session_id in CARTS:
        CARTS[session_id] = {}

def create_order(session_id: str, customer_info: dict, payment_method: str) -> Dict[str, Any]:
    cart = get_cart(session_id)
    if not cart["cart_items"]:
        raise ValueError("Carrinho está vazio.")
        
    order_id = f"ORD-{uuid.uuid4().hex[:8].upper()}"
    
    # Coletar todos os arquivos dos produtos para a entrega
    purchased_files = []
    for item in cart["cart_items"]:
        prod = item["product"]
        for file_info in prod.get("included_files", []):
            purchased_files.append({
                "product_id": prod["id"],
                "product_title": prod["title"],
                "product_type": prod["type"],
                "file_name": file_info["name"],
                "file_type": file_info["type"],
                "file_size": file_info["size"],
                "download_url": f"/download/{order_id}/{file_info['name']}"
            })
            
    order_data = {
        "order_id": order_id,
        "customer": customer_info,
        "payment_method": payment_method,
        "cart_items": cart["cart_items"],
        "total": cart["total"],
        "purchased_files": purchased_files,
        "status": "PAID",
        "created_at": "18/09/2026 13:35",
        "pix_code": "00020126580014BR.GOV.BCB.PIX0136123e4567-e89b-12d3-a456-4266141740005204000053039865405147.005802BR5925AmplificaIA Marketplace6009SAO PAULO62070503***6304E2CA"
    }
    
    ORDERS[order_id] = order_data
    clear_cart(session_id)
    return order_data

def get_order(order_id: str) -> Optional[Dict[str, Any]]:
    return ORDERS.get(order_id)
