function CalculateCarCom(){
    var sumInsured = $('#bikeSum').val();
    var yom = $('#oldbike :selected').val();
    var voluntary_excess = $('#veBike :selected').val();
    var ncd_years = $('#noclaimebike :selected').val();
    var electric_discount = $('#towingBike :selected').val();
    var direct_discount = $('#DirectDiscountBike :selected').val();
    var valBikeC = $("#cccCar :selected").val();
    var rsd =  $('#rsdbike :selected').val();
    var seat = $('#seatC').val()
    var helperC = $('#helperCC').val()

    var helper_cost_c =0
    var total = 0
    var cost= 0
    var yom_cost = 0
    var vc_cost = 0
    var ndc_cost = 0
    var ed_cost = 0
    var dd_cost = 0
    var rsd_cost = 0
    var seat_cost = 0
    // Set sum_insured_percentage
    var new_sum_insured = 0
    var third_party_discount = 0
    var rsd_helper = 0
    

    if(ty == "Electric Vehicle"){
        if(valBikeC == '1000'){
            cost = 2000

        }
        else if(valBikeC== '1000-1600'){
            cost = 3000

        }
        else{
            cost = 0
        }
        var new_sum_insured = 1.25/100*sumInsured
     
    }
    else if(ty == "Vehicle CC"){
        
        if(valBikeC == '1000'){
            cost = 2000
          
        }
        else if(valBikeC== '1000-1600'){
            cost = 3000
          

        }
        else{
            cost = 0
        }
        var new_sum_insured = 1.25/100*sumInsured
        console.log('Third Party Premium', cost)
    }
    else{
        if(valBikeC == '1000'){
            cost = 1500
 
        }
        else if(valBikeC== '1000-1600'){
            cost = 2500
           
        }
       
        else{
            cost = 0
        }
        var new_sum_insured = 0.75/100*sumInsured
        
    }
    console.log('basic premium', new_sum_insured)
    console.log('Third Party Premium', cost)
    total = new_sum_insured
    // set yom percentage
    if(yom== 'Less than or equal to 10 years'){
        yom_cost = 0

    }else if(yom == 'Above 10 years'){
        yom_cost = 15/100 * new_sum_insured
        console.log('Yom cost', yom_cost)
    }
    else{
        yom_cost = 0 
    }
    console.log('Yom cost', yom_cost)
    total = total+yom_cost
    console.log('With year of manufacurting charge',  total)
    // Set Private Rent
    if(helperC== 'Yes'){
        helper_cost_c = 700
        rsd_helper = 125
    }else{
        helper_cost_c = 0
    }

    total = total+helper_cost_c
    // set voluntary Excess
    if(voluntary_excess== '0'){
        vc_cost = 0
    }else if(voluntary_excess== '1000'){
        vc_cost = 10/100*total
    }else if(voluntary_excess== '3000'){
        vc_cost = 15/100*total
    }else if(voluntary_excess== '5000'){
        vc_cost = 20/100*total
    }
    else if(voluntary_excess== '10000'){
        vc_cost = 25/100*total
    }
    else{
        vc_cost = 0
    }
    
    console.log('voluntary Excess', vc_cost)
    total = total-vc_cost
    console.log('With year of manufacurting charge',  total)

    // set NCD YEARS
    if(ncd_years == '0 year @0%'){
        ndc_cost = 0
        third_party_discount =0
    }else if(ncd_years == '1 year @20%'){
        ndc_cost = 15/100 *total
        third_party_discount = 15/100 *cost
    }else if(ncd_years == '2 years @30%'){
        ndc_cost = 25/100 *total
        third_party_discount = 25/100 *cost
    }else if(ncd_years == '3years @40%'){
        ndc_cost = 30/100 *total
        third_party_discount = 25/100 *cost
    }
    else{
        ndc_cost = 0
    }
    console.log('No claim Discount', vc_cost)
    total = total-ndc_cost
    console.log('Total with NCD',  total)

    // set electric discount
    if(electric_discount== 'Yes'){
        ed_cost = 200
    }else{
        ed_cost = 0
    }
    console.log('Towing charge', ed_cost)
    total = total-ed_cost
    console.log('Total with Towing Charge',  total)
    console.log('discount on thirdparty',third_party_discount)
    console.log('Third Party Cost', cost)
    total = total+cost-third_party_discount
    // Setting direct discount 
    if(ty == "Electric Vehicle" || ty == "Vehicle CC | KW"){
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
        rsd_cost = 125
        rsd_cost_sum = 0.15/100*new_sum_insured
        rsd_passenger = (seat-1)*125
        rsd_seat_cost = rsd_cost +rsd_cost_sum+rsd_passenger
    }else{
        rsd_cost = 0
        rsd_cost_sum = 0
        rsd_passenger = 0
        rsd_seat_cost = rsd_cost +rsd_cost_sum+rsd_passenger
    }

    console.log('RSD Cost', rsd_cost+rsd_cost_sum+rsd_passenger)
    total = total+rsd_seat_cost+rsd_helper
    console.log("Total with RSD", total)
    // Setting Seat 
    driver = 700
    passenger = parseInt(seat-1) * 125
    seat_cost = driver+passenger

    total = total+ seat_cost
    console.log("Total with third party premium", total)
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
    document.getElementById('seat_c').innerHTML ="Rs." + parseInt(seat_cost)
    document.getElementById('helper_c').innerHTML ="Rs." + parseInt(helper_cost_c)
    document.getElementById('ncd').innerHTML ="Rs." + parseInt(ndc_cost)
    document.getElementById('ed').innerHTML ="Rs." + parseInt(ed_cost)
    document.getElementById('direct_d').innerHTML ="Rs." + parseInt(dd_cost)
    document.getElementById('tp_p').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('rsd').innerHTML ="Rs." +parseInt(rsd_seat_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)

}
  