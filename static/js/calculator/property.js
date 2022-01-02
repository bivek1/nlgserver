function calculateHome(){
    clas = $('#type :selected').val()
    sumInsured = $('#sumInsured').val()
    discount = $("#discount :selected").val();
    rsd = $("#rsd :selected").val();
    var total = 0
    var stamp = 20
    var vat = 0
    var cost = 0
    var minimum_cost = 0
    var discount_cost = 0
    var rsd_cost = 0

    if (sumInsured <= 10000000){
        cost = 0.04/100 * parseInt(sumInsured)
        if(clas == 'other'){
            cost = 1.5/100 * cost
        }

    }else if (sumInsured <= 20000000){
        cost = 0.1/100 * parseInt(sumInsured)
        if(clas == 'other'){
            cost = 1.5/100 * cost
        }  
    }else{
        alert("Home Insurance is only valid for Residential Building below 2 corer")
    }
    if(discount == 'Yes'){
        discount_cost = 10/100 * cost
    }
    else{
        discount_cost = 0
    }
    
    total = cost - discount_cost
    if(clas == 'first'){
        if(total<500){
            minimum_cost = 500-total
        }
        else{
            minimum_cost = 0
        }
    }
    
    if(rsd == 'Yes'){
        if (sumInsured <= 10000000){
            rsd_cost = 0.010/100 * parseInt(sumInsured)
            if(clas == 'other'){
                rsd_cost = 1.5/100 * cost
            }
    
        }else if (sumInsured <= 20000000){
            rsd_cost = 0.050/100 * parseInt(sumInsured)
            if(clas == 'other'){
                rsd_cost = 1.5/100 * cost
            }
        }
    }
    else{
        rsd_cost= 0
    }
    total = total+rsd_cost
    net_premium = total
    vat = 13/100*total
    total = total+vat+stamp
    
    document.getElementById('basicp').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('discount_c').innerHTML ="Rs." + parseInt(discount_cost)
    document.getElementById('minimum_c').innerHTML ="Rs." + parseInt(minimum_cost)
    document.getElementById('rsd_c').innerHTML ="Rs." + parseInt(rsd_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)
}