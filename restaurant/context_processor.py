def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        #carro = request.session.get("carro", {})
    #for item in carro.values():
     #       total += float(item["precio"]) * item["cantidad"]
    #return {"importe_total_carro": total}
     for key, value in request.session["carro"].items():
        total=total+(float(value["precio"]))
    else:  
       total= "debes hacer login"  

    return  {"importe_total_carro": total}