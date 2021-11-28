function CalculateCarCom(){
    var sumInsured = parseInt($('#bikeSum').val());
    var yom = $('#oldbike :selected').val();
    var voluntary_excess = $('#veBike :selected').val();
    var ncd_years = $('#noclaimebike :selected').val();
    var electric_discount = $('#towingBike :selected').val();
    var direct_discount = $('#DirectDiscountBike :selected').val();
    var valBikeC = $("#cccCar :selected").val();
    var rsd =  $('#rsdbike :selected').val();
    var extra = parseInt($('#eav').val());
    var seat = $('#seatC').val()

    var basic_premium = 0
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
    var ncd_tp_cost = 0 
    var total_sum_insured = extra+sumInsured
    if(valBikeC == '1000'){
        cost = 3500 
        basic_premium = 1000
    }
    else if(valBikeC== '1000-1600'){
        cost = 4500
        basic_premium = 1000
       
    }
    else if(valBikeC == '1600+'){
        cost = 6500
        basic_premium = 500
      
    }
    else{
        cost = 0
    }
    new_sum_insured = 2/100*total_sum_insured
    console.log('New Sum Insured', new_sum_insured)
    total = new_sum_insured
    
    console.log('basic premium', basic_premium)
    total = total+basic_premium
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
        ncd_tp_cost = 0
    }else if(ncd_years == '1 year @20%'){
        ndc_cost = 15/100 *total
        ncd_tp_cost = 15/100 *cost
    }else if(ncd_years == '2 years @30%'){
        ndc_cost = 25/100 *total
        ncd_tp_cost = 25/100 *cost
    }else if(ncd_years == '3years @40%'){
        ndc_cost = 30/100 *total
        ncd_tp_cost = 30/100 *cost
    }
    else{
        ndc_cost = 0
        ncd_tp_cost = 0
    }
    console.log('No claim Discount', vc_cost)
    total = total-ndc_cost
    console.log('Total with NCD',  total)
     // Setting direct discount 
    if(direct_discount == 'Yes'){
        dd_cost = 10/100*total
        console.log('direct discount from the top', dd_cost)
    }
    else{
        dd_cost = 0
    }
    console.log('Direct Discount', dd_cost)
    total = total-dd_cost
    console.log('Total with Direct Discount',  total)
    // set electric discount
    if(electric_discount== 'Yes'){
        ed_cost = 500
    }else{
        ed_cost = 0
    }
    console.log('Towing charge', ed_cost)
    total = total+ed_cost
    console.log('NCD IN TP', ncd_tp_cost)
    console.log('Total with Towing Charge',  total)
    console.log('Third Party Cost', cost)
    total = total+cost-ncd_tp_cost
   
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

    total = total+ seat_cost
    console.log("Total with seat", total)
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
    document.getElementById('basicp').innerHTML ="Rs." + parseInt(basic_premium)
    document.getElementById('total_sum_c').innerHTML ="Rs." + parseInt(new_sum_insured)
    document.getElementById('yom').innerHTML ="Rs." + parseInt(yom_cost)
    document.getElementById('ncd_tp_p').innerHTML ="Rs." + parseInt(ncd_tp_cost)
    document.getElementById('ve').innerHTML ="Rs." + parseInt(vc_cost)
    document.getElementById('seat_c').innerHTML ="Rs." + parseInt(seat_cost)
    document.getElementById('ncd').innerHTML ="Rs." + parseInt(ndc_cost)
    document.getElementById('ed').innerHTML ="Rs." + parseInt(ed_cost)
    document.getElementById('direct_d').innerHTML ="Rs." + parseInt(dd_cost)
    document.getElementById('rsd').innerHTML ="Rs." +parseInt(rsd_seat_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)

}
  