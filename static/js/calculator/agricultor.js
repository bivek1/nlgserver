function calculateHome(){
    clas = $('#type :selected').val()
    sumInsured = $('#sumInsured').val()
    var total = 0
    var vat = 0
    var cost = 0
    var personal = 0
    if(clas == 'Livestock/Crops/Birds'){
        cost = 5/100 * sumInsured
    }else if(clas=='Fish/Ostrich'){
        cost = 2/100 * sumInsured
    }else{
        cost = 1.25/100 * sumInsured
    }
    console.log(cost)
    var anudan = 75/100 * cost
    console.log('anudan', anudan)
    var personal = 100
    total = cost-anudan+personal
    console.log('total', total)

    if (sumInsured < 100000){
        stamp = 20
    }else{
        stamp = 30
    }

    net_premium = total
    vat = 13/100*total
    total = total+vat+stamp
    
    document.getElementById('basicp').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('anudan').innerHTML ="Rs." + parseInt(anudan)
    document.getElementById('personal_c').innerHTML ="Rs." + parseInt(personal)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)
}