// Helper script for UI interactions
function copyToClipboard(text, elementId) {
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById(elementId);
        if (btn) {
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400 mr-2"></i> Copiado!';
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500');
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.classList.remove('bg-emerald-600/30', 'border-emerald-500');
            }, 2500);
        }
    }).catch(err => {
        console.error('Erro ao copiar: ', err);
    });
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'fixed bottom-5 right-5 bg-indigo-600 text-white px-5 py-3 rounded-xl shadow-2xl z-50 flex items-center gap-3 border border-indigo-400/30 transition-all transform translate-y-full opacity-0';
    toast.innerHTML = `<i class="fa-solid fa-circle-check text-xl"></i> <span>${message}</span>`;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.remove('translate-y-full', 'opacity-0');
    }, 50);
    
    setTimeout(() => {
        toast.classList.add('translate-y-full', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Escutar eventos HTMX para notificações
document.addEventListener('htmx:afterOnLoad', function(evt) {
    if (evt.detail.target.id === 'cart-drawer-container') {
        const countBadge = document.getElementById('cart-count-badge');
        if (countBadge) {
            countBadge.classList.add('animate-bounce');
            setTimeout(() => countBadge.classList.remove('animate-bounce'), 1000);
        }
    }
});
