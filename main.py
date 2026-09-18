"""
main.py - Servidor FastAPI para o AmplificaIA Marketplace White-Label
Integra HTMX, Jinja2 Templates e entrega de produtos digitais pós-compra.
"""

import os
import uuid
from typing import Optional
from fastapi import FastAPI, Request, Form, Response, Cookie, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import (
    TENANTS, PRODUCT_TYPES, CATEGORIES,
    get_tenant, list_products, get_product
)
from cart import (
    get_cart, add_to_cart, remove_from_cart,
    create_order, get_order
)

app = FastAPI(
    title="AmplificaIA Marketplace White-Label",
    description="Prototipo funcional de e-commerce para produtos e automações de IA.",
    version="1.0.0"
)

# Montar diretório de arquivos estáticos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configurar motor de templates Jinja2
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def get_session_id(request: Request, response: Response) -> str:
    session_id = request.cookies.get("session_id")
    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie("session_id", session_id, httponly=True, max_age=86400*7)
    return session_id


# ==========================================
# ROTAS PRINCIPAIS DE NAVEGAÇÃO
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def index_page(
    request: Request, 
    response: Response,
    tenant: str = "amplifica_ia",
    category: str = "all",
    ptype: str = "all",
    search: Optional[str] = None
):
    session_id = get_session_id(request, response)
    tenant_obj = get_tenant(tenant)
    cart = get_cart(session_id)
    products = list_products(category=category, ptype=ptype, search=search)
    
    context = {
        "request": request,
        "tenant": tenant_obj,
        "categories": CATEGORIES,
        "product_types": PRODUCT_TYPES,
        "products": products,
        "current_category": category,
        "current_ptype": ptype,
        "search": search,
        "cart": cart
    }
    
    res = templates.TemplateResponse("index.html", context)
    if not request.cookies.get("session_id"):
        res.set_cookie("session_id", session_id, httponly=True, max_age=86400*7)
    return res


# Rota parcial HTMX para filtragem e busca dinâmica
@app.get("/products", response_class=HTMLResponse)
async def filter_products_partial(
    request: Request,
    category: str = "all",
    ptype: str = "all",
    search: Optional[str] = None
):
    products = list_products(category=category, ptype=ptype, search=search)
    context = {
        "request": request,
        "products": products,
        "product_types": PRODUCT_TYPES
    }
    return templates.TemplateResponse("components/product_card_list.html", context)


# Rota para exibir o Modal de Detalhes do Produto (HTMX)
@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail_modal(request: Request, product_id: str, tenant: str = "amplifica_ia"):
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
        
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "product": product,
        "tenant": tenant_obj,
        "product_types": PRODUCT_TYPES
    }
    return templates.TemplateResponse("product_detail.html", context)


# ==========================================
# ROTAS DE CARRINHO DE COMPRAS (HTMX)
# ==========================================

@app.get("/cart", response_class=HTMLResponse)
async def view_cart_drawer(request: Request, response: Response, tenant: str = "amplifica_ia"):
    session_id = get_session_id(request, response)
    cart = get_cart(session_id)
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "cart": cart,
        "tenant": tenant_obj
    }
    return templates.TemplateResponse("components/cart_drawer.html", context)


@app.post("/cart/add/{product_id}", response_class=HTMLResponse)
async def add_to_cart_action(request: Request, response: Response, product_id: str, tenant: str = "amplifica_ia"):
    session_id = get_session_id(request, response)
    cart = add_to_cart(session_id, product_id)
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "cart": cart,
        "tenant": tenant_obj
    }
    return templates.TemplateResponse("components/cart_drawer.html", context)


@app.post("/cart/remove/{product_id}", response_class=HTMLResponse)
async def remove_from_cart_action(request: Request, response: Response, product_id: str, tenant: str = "amplifica_ia"):
    session_id = get_session_id(request, response)
    cart = remove_from_cart(session_id, product_id)
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "cart": cart,
        "tenant": tenant_obj
    }
    return templates.TemplateResponse("components/cart_drawer.html", context)


# ==========================================
# ROTAS DE CHECKOUT & CONFIRMAÇÃO
# ==========================================

@app.get("/checkout", response_class=HTMLResponse)
async def checkout_page(request: Request, response: Response, tenant: str = "amplifica_ia"):
    session_id = get_session_id(request, response)
    cart = get_cart(session_id)
    if not cart["cart_items"]:
        # Se carrinho estiver vazio, redirecionar para homepage
        return Response(status_code=302, headers={"Location": f"/?tenant={tenant}"})
        
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "cart": cart,
        "tenant": tenant_obj
    }
    return templates.TemplateResponse("checkout.html", context)


@app.post("/checkout/process", response_class=HTMLResponse)
async def process_checkout(
    request: Request,
    response: Response,
    name: str = Form(...),
    email: str = Form(...),
    document: str = Form(...),
    company: Optional[str] = Form(None),
    payment_method: str = Form("pix"),
    tenant: str = Form("amplifica_ia")
):
    session_id = get_session_id(request, response)
    customer_info = {
        "name": name,
        "email": email,
        "document": document,
        "company": company or "N/A"
    }
    
    try:
        order = create_order(session_id, customer_info, payment_method)
    except ValueError as e:
        return Response(status_code=302, headers={"Location": f"/?tenant={tenant}"})
        
    tenant_obj = get_tenant(tenant)
    context = {
        "request": request,
        "order": order,
        "tenant": tenant_obj,
        "cart": get_cart(session_id)
    }
    return templates.TemplateResponse("order_success.html", context)


# ==========================================
# ROTA DE DOWNLOAD DOS ARQUIVOS COMPRADOS
# ==========================================

@app.get("/download/{order_id}/{file_name}")
async def download_file(order_id: str, file_name: str):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado ou expirado.")
        
    # Verificar se o arquivo faz parte do pedido
    valid_file = False
    for pf in order.get("purchased_files", []):
        if pf["file_name"] == file_name:
            valid_file = True
            break
            
    if not valid_file:
        raise HTTPException(status_code=403, detail="Acesso não autorizado a este arquivo.")
        
    file_path = os.path.join(BASE_DIR, "static", "downloads", file_name)
    if not os.path.exists(file_path):
        # Fallback para criar o arquivo dinamicamente se for uma amostra
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{{\n  \"asset\": \"{file_name}\",\n  \"status\": \"downloaded\",\n  \"order_id\": \"{order_id}\"\n}}")
            
    return FileResponse(
        path=file_path,
        filename=file_name,
        media_type="application/octet-stream"
    )
