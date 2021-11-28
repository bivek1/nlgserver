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
    var privateRent = $('#privateRent').val()


    var total = 0
    var cost= 0
    var yom_cost = 0
    var vc_cost = 0
    var ndc_cost = 0
    var ed_cost = 0
    var dd_cost = 0
    var rsd_cost = 0
  
    var seat_cost = 0
    var private_cost = 0
    // Set sum_insured_percentage
    var new_sum_insured = 0
    var discount_premium = 0 

    if(ty == "Electric Vehicle"){
        if(valBikeC == '1000'){
            if(sumInsured> 2000000){
                new_sum_insured = 0.84/100*sumInsured
                
            }else{
                new_sum_insured = 0.63/100*sumInsured
            }
            discount_premium = 3000
            
        }
        else if(valBikeC== '1000-1600'){
            cost = 4000
            if(sumInsured> 2000000){
                new_sum_insured = 0.84/100*sumInsured
            }else{
                new_sum_insured = 0.65/100*sumInsured
            }
            discount_premium = 4000
        }
        else if(valBikeC == '1600+'){
            cost = 6000
            if(sumInsured> 2000000){
                new_sum_insured = 0.84/100*sumInsured
            }else{
                new_sum_insured = 0.90/100*sumInsured
            }
            discount_premium = 6000
        }
        else{
            new_sum_insured = 0
        }
     
    }
    else if(ty == "Vehicle CC"){
        cost = 3000
        if(valBikeC == '1000'){
            cost = 3000
            if(sumInsured> 2000000){
                new_sum_insured = 1.12/100*sumInsured
                
            }else{
                new_sum_insured = 0.84/100*sumInsured
            }
            discount_premium = 3000
            
        }
        else if(valBikeC== '1000-1600'){
            cost = 4000
            if(sumInsured> 2000000){
                new_sum_insured = 1.12/100*sumInsured
            }else{
                new_sum_insured = 0.87/100*sumInsured
            }
            discount_premium = 4000
        }
        else if(valBikeC == '1600+'){
            cost = 6000
            if(sumInsured> 2000000){
                new_sum_insured = 1.12/100*sumInsured
            }else{
                new_sum_insured = 0.90/100*sumInsured
            }
            discount_premium = 6000
        }
        else{
            cost = 0
        }
        console.log('Third Party Premium', cost)
    }
    else{
        if(valBikeC == '1000'){
            cost = 3000
            if(sumInsured> 2000000){
                new_sum_insured = 0.62/100*sumInsured
                
            }else{
                new_sum_insured = 0.44/100*sumInsured
            }
            discount_premium = 1000
            
        }
        else if(valBikeC== '1000-1600'){
            cost = 4000
            if(sumInsured> 2000000){
                new_sum_insured = 0.62/100*sumInsured
            }else{
                new_sum_insured = 0.48/100*sumInsured
            }
            discount_premium = 1500
        }
        else if(valBikeC == '1600+'){
            cost = 6000
            if(sumInsured> 2000000){
                new_sum_insured = 0.62/100*sumInsured
            }else{
                new_sum_insured = 0.51/100*sumInsured
            }
            discount_premium = 2750
        }
        else{
            cost = 0
        }
        console.log('Third Party Premium', cost)
    }
    console.log('basic premium', new_sum_insured)
    total = new_sum_insured-discount_premium
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
    if(privateRent== 'Yes'){
        private_cost = 10/100*total
    }else{
        private_cost = 0
    }
    console.log('private rent', private_cost)
    // set voluntary Excess
    if(voluntary_excess== '0'){
        vc_cost = 0
    }else if(voluntary_excess== '1000'){
        vc_cost = 10/100*total
    }else if(voluntary_excess== '2000'){
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
    }else if(ncd_years == '1 year @20%'){
        ndc_cost = 20/100 *total
    }else if(ncd_years == '2 years @30%'){
        ndc_cost = 30/100 *total
    }else if(ncd_years == '3years @40%'){
        ndc_cost = 40/100 *total
    }
    else if(ncd_years == '4years @45%'){
        ndc_cost = 45/100 *total
    }
    else if(ncd_years == 'Above 4 year'){
        ndc_cost = 50/100 *total
    }else{
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
    console.log('Third Party Cost', discount_premium)
    total = total+discount_premium
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
    total = total+rsd_seat_cost
    console.log("Total with RSD", total)
    // Setting Seat 
    driver = 700
    passenger = parseInt(seat-1) * 125
    seat_cost = driver+passenger

    total = total+ seat_cost+discount_premium
    console.log("Total with seat", total)
    console.log('Third Party Premium', discount_premium)
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
    document.getElementById('eav_c').innerHTML ="Rs." + parseInt(discount_premium)
    document.getElementById('seat_c').innerHTML ="Rs." + parseInt(seat_cost)
    document.getElementById('privateC').innerHTML ="Rs." + parseInt(private_cost)
    document.getElementById('ncd').innerHTML ="Rs." + parseInt(ndc_cost)
    document.getElementById('ed').innerHTML ="Rs." + parseInt(ed_cost)
    document.getElementById('direct_d').innerHTML ="Rs." + parseInt(dd_cost)
    document.getElementById('tp_p').innerHTML ="Rs." + parseInt(discount_premium)
    document.getElementById('rsd').innerHTML ="Rs." +parseInt(rsd_seat_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)

}
  