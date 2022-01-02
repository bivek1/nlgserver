function calculateHome(){

    sumInsured = $('#sumInsured').val()
    var total = 0
    var vat = 0
    var cost = 0
    var rsd_cost = 0
    if (sumInsured > 100000){
        var stamp = 30
    }else{
        var stamp = 20
    }
    if (sumInsured <= 2000000 ){
        rsd_cost = 0.10/1000
        cost = rsd_cost * sumInsured
    }else{
        rsd_cost = 0.25/1000
        cost = rsd_cost * sumInsured
    }

    net_premium = total
   
    total = total+vat+stamp
    
    document.getElementById('basicp').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('rsd_c').innerHTML ="Rs." + parseInt(rsd_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)
}