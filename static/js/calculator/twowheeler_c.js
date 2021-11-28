function CalculateCom(){
    var sumInsured = $('#bikeSum').val();
    var yom = $('#oldbike :selected').val();
    var voluntary_excess = $('#veBike :selected').val();
    var ncd_years = $('#noclaimebike :selected').val();
    var electric_discount = $('#towingBike :selected').val();
    var direct_discount = $('#DirectDiscountBike :selected').val();
    var valBikeC = $("#CbikeCC :selected").val();
    var rsd =  $('#rsdbike :selected').val();
    
    var total = 0
    var cost= 0
    var yom_cost = 0
    var vc_cost = 0
    var ndc_cost = 0
    var ed_cost = 0
    var dd_cost = 0
    var rsd_cost = 0
    // Set sum_insured_percentage
   
 

    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(valBikeC == 'Less than 150 CC'){
            cost = 1500
        }
        else if(valBikeC== '150 to 250 CC'){
            cost = 1700
        }
        else if(valBikeC == 'Above 250 CC'){
            cost = 1900
        }
        else{
            cost = 0
        }
        console.log('Third Party Premium', cost)
        var new_sum_insured = 1.50/100*sumInsured
        console.log("Basic Premium" , new_sum_insured)
        // Futher new for com
    }
    else{
        if(valBikeC == 'Less than 150 CC'){
           cost = 1250
        }
        else if(valBikeC== '150 to 250 CC'){
            cost = 1500
        }
        else if(valBikeC == 'Above 250 CC'){
            cost = 1500
        }
        else{
            cost = 0
        }
        console.log('Third Party Premium', cost)
        var new_sum_insured = 1/100*sumInsured
        console.log("Basic Premium" , new_sum_insured)
    }
    // set yom percentage
    if(yom== 'Less than 5 year'){
        yom_cost = 0

    }else if(yom == '5 to 10 years'){
        yom_cost = 15/100 * new_sum_insured
        console.log('Yom cost', yom_cost)
        
    }else if(yom == 'Above 10 years'){
       yom_cost = 25/100 * new_sum_insured
    
    }
    else{
        yom_cost = 0 
    }
    console.log('Yom cost', yom_cost)
    total = new_sum_insured+yom_cost
    console.log('With year of manufacurting charge',  total)
    
    // set voluntary Excess
    if(voluntary_excess== '0'){
         vc_cost = 0
    }else if(voluntary_excess== '500'){
         vc_cost = 10/100*total
    }else if(voluntary_excess== '1000'){
         vc_cost = 15/100*total
    }else if(voluntary_excess== '2000'){
         vc_cost = 20/100*total
    }else{
         vc_cost = 0
    }
    
    console.log('voluntary Excess', vc_cost)
    total = total-vc_cost
    console.log('With year of manufacurting charge',  total)

    // set NCD YEARS
    if(ncd_years == '0 year @0%'){
        ndc_cost = 0
    }else if(ncd_years == '1 year @15%'){
        ndc_cost = 15/100 *total
    }else if(ncd_years == '2 years @25%'){
        ndc_cost = 25/100 *total
    }else if(ncd_years == '3years or above @35%'){
        ndc_cost = 35/100 *total
    }else{
        ndc_cost = 0
    }
    console.log('No claim Discount', vc_cost)
    total = total-ndc_cost
    console.log('Total with NCD',  total)

    // set electric discount
    if(electric_discount== 'Yes'){
        ed_cost = 25/100*total
    }else{
        ed_cost = 0
    }
    console.log('Electric Discount', ed_cost)
    total = total-ed_cost
    console.log('Total with Electric Discount',  total)
    // Setting direct discount 
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(direct_discount == 'Yes'){
            dd_cost = 10/100*total
            console.log('direct discount from the top', dd_cost)
        }
        else{
            dd_cost = 0
        }
    }
    else{
        dd_cost = 0
    }
    console.log('Direct Discount', dd_cost)
    total = total-dd_cost
    console.log('Total with Direct Discount',  total)
    // setting RSD Risk
    if(rsd == 'Yes'){
        rsd_cost = 250
        rsd_cost_sum = 0.15/100*new_sum_insured
    }else{
        rsd_cost = 0
        rsd_cost_sum = 0
    }
    console.log('RSD Cost', rsd_cost+rsd_cost_sum)
    total = total+rsd_cost+rsd_cost_sum
    console.log('Third Party Premium', cost)
    total = total + cost
    net_premium = total
    console.log("Total Cost is", total)
    vat = 13/100 * total
    console.log('VAT', vat)
    if(sumInsured <= 100000){
        stamp = 20
    }else{
        stamp = 30
    }
    total =total+vat+stamp
    //  init_percentage =  yom_cost+
    document.getElementById('basicp').innerHTML ="Rs." + parseInt(new_sum_insured)
    document.getElementById('yom').innerHTML ="Rs." + parseInt(yom_cost)
    document.getElementById('ve').innerHTML ="Rs." + parseInt(vc_cost)
    document.getElementById('ncd').innerHTML ="Rs." + parseInt(ndc_cost)
    document.getElementById('ed').innerHTML ="Rs." + parseInt(ed_cost)
    document.getElementById('direct_d').innerHTML ="Rs." + parseInt(dd_cost)
    document.getElementById('tp_p').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('rsd').innerHTML ="Rs." +parseInt(rsd_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)

}
  