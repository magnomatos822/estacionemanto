from django.contrib import admin
from core.models import(    
                            Marca, 
                            Mensalista, 
                            Movimento, 
                            Parametro, 
                            Pessoa,
                            Veiculo,
                            MovMensalista,   
                                )


class MovimentoRotativoAdmin(admin.ModelAdmin):
    list_display =(
        'veiculo',
        'proprietario',
        'chekin', 
        'checkout',
        'valor_hora',
        'pagamento',
        'total_horas',
        'total',
    )

class MensalistaAdim(admin.ModelAdmin):
    list_display =(
        'veiculo',
        'inicio',
        'valor_mes',
        'pago',
    )


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista',
        'dt_pgto',
        'total',
    )


# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(Movimento, MovimentoRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdim)
admin.site.register(MovMensalista, MovMensalistaAdmin)
