function CalculateCarCom(){
    var sumInsured = parseInt($('#bikeSum').val());
    var yom = $('#oldbike :selected').val();
    var voluntary_excess = $('#veBike :selected').val();
    var ncd_years = $('#noclaimebike :selected').val();
    var electric_discount = $('#towingBike :selected').val();
    var direct_discount = $('#DirectDiscountBike :selected').val();
    var helper = $('#helper :selected').val()
    var valBikeC = $("#cccCar").val();
    var rsd =  $('#rsdbike :selected').val();
    var extra = parseInt($('#eav').val())
    var seat = $('#seatC').val()
    var privateRent = $('#ownCC').val()
    
    var total = 0
    var helper_cost  = 0
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
    var total_sum_insured = 0
    var new_sum_insured = 0
    var discount_premium = 0 
    total_sum_insured = sumInsured+extra
    if(ty == "Electric Vehicle"){
        helper_cost = 700
        if(valBikeC <= 3){
            cost = 6750
            discount_premium = 3000
            new_sum_insured = 1.25/100*total_sum_insured
        }
        else if(valBikeC > 3){
            cost = 10500
            discount_premium = 2500
            no_of_p = (valBikeC-3)*500 
            new_sum_insured = 1.25/100*total_sum_insured + no_of_p
        }
        
        else{
            cost = 0
            new_sum_insured = 0
        }
     
    }
    else if(ty == "Vehicle CC"){
        helper_cost = 700
        if(valBikeC <= 3){
            cost = 6750
            discount_premium = 3000
            new_sum_insured = 1.25/100*total_sum_insured
        }
        else if(valBikeC > 3){
            cost = 10500
            no_of_p = (valBikeC-3)*500 
            new_sum_insured = 1.25/100*total_sum_insured + no_of_p
            discount_premium = 2500
        }
    
        else{
            cost = 0
            new_sum_insured = 0
        }

    }
    else{
        helper_cost = 600
        if(valBikeC <= 3){
            cost = 5700
            discount_premium = 3000
            new_sum_insured = 0.75/100*total_sum_insured
            
        }
        else if(valBikeC > 3){
            cost = 9000
            discount_premium = 2500
            no_of_p = (valBikeC-3)*500 
            new_sum_insured = 0.87/100*total_sum_insured + no_of_p
        }
        else{
            cost = 0
            new_sum_insured = 0
        }
        console.log('Third Party Premium', cost)
    }
    
    console.log('basic premium', new_sum_insured)
    total = new_sum_insured-discount_premium+helper_cost
    // set yom percentage
    if(yom== 'Less than 5 Years'){
        yom_cost = 0

    }else if(yom == '5 to 10 Years'){
        yom_cost = 10/100 * new_sum_insured
        console.log('Yom cost', yom_cost)
    }
    else if(yom == "Above 10 years"){
        yom_cost = 20/100 * new_sum_insured
        console.log('Yom cost', yom_cost)
    }
    else{
        yom_cost = 0
    }
    console.log('Yom cost', yom_cost)
    total = total+yom_cost
    console.log('With year of manufacurting charge',  total)
    // Set Private Rent

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
    if(privateRent== 'Yes'){
        private_cost = 25/100*total
    }else{
        private_cost = 0
    }
    total = total+private_cost
    console.log('Own Carrying private rent', private_cost)
    // set NCD YEARS
    if(ncd_years == '0 year @0%'){
        ndc_cost = 0
        ncd_tp = 0
    }else if(ncd_years == '1 year @20%'){
        ndc_cost = 15/100 *total
        ncd_tp = 15/100 *cost
    }else if(ncd_years == '2 years @30%'){
        ndc_cost = 25/100 *total
        ncd_tp = 25/100 *cost
    }else if(ncd_years == '3years @40%'){
        ndc_cost = 30/100 *total
        ncd_tp = 30/100 *cost
    }
    else{
        ndc_cost = 0
        ncd_tp = 0
    }
    console.log('No claim Discount', vc_cost)
    total = total-ndc_cost
    console.log('Total with NCD',  total)

    // set electric discount
    if(electric_discount== 'Yes'){
        ed_cost = 500
    }else{
        ed_cost = 0
    }
    console.log('Towing charge', ed_cost)
    total = total+ed_cost
    console.log('Total with Towing Charge',  total)
    console.log('Third Party Cost', cost)

    total = total+cost-discount_premium-ncd_tp
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
        if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
            rsd_cost = 125
            rsd_cost_sum = 0.2/100*new_sum_insured
            rsd_passenger = (seat-1)*125
           
            if (helper == "Yes"){
                var rsd_helper = 126
            }
            rsd_seat_cost = rsd_cost +rsd_cost_sum+rsd_passenger+rsd_helper
        }else{
            rsd_cost = 126
            rsd_cost_sum = 0.2/100*new_sum_insured
            rsd_passenger = (seat-1)*126
            if (helper == "Yes"){
                var rsd_helper = 126
            }
            rsd_seat_cost = rsd_cost +rsd_cost_sum+rsd_passenger+rsd_helper
        }
      
       
    }else{
        rsd_cost = 0
        rsd_cost_sum = 0
        rsd_passenger = 0
        rsd_seat_cost = rsd_cost +rsd_cost_sum+rsd_passenger
    }

    console.log('RSD Cost', rsd_cost+rsd_cost_sum+rsd_passenger)
    total = total+rsd_seat_cost
    console.log("Total with RSD", total)
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
         // Setting Seat 
        driver = 700
        passenger = parseInt(seat-1) * 700
        seat_cost = driver+passenger

    }
    else{
         // Setting Seat 
         driver = 600
         passenger = parseInt(seat-1) * 600
         seat_cost = driver+passenger
    }
   
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
    document.getElementById('discount_c').innerHTML ="Rs." + parseInt(discount_premium)
    document.getElementById('seat_c').innerHTML ="Rs." + parseInt(seat_cost)
    document.getElementById('own_c').innerHTML ="Rs." + parseInt(private_cost)
    document.getElementById('ncd').innerHTML ="Rs." + parseInt(ndc_cost)
    document.getElementById('ed').innerHTML ="Rs." + parseInt(ed_cost)
    document.getElementById('direct_d').innerHTML ="Rs." + parseInt(dd_cost)
    document.getElementById('tp_p').innerHTML ="Rs." + parseInt(cost)
    document.getElementById('d_tp_p').innerHTML ="Rs." + parseInt(ncd_tp)
    document.getElementById('rsd').innerHTML ="Rs." +parseInt(rsd_seat_cost)
    document.getElementById('net_premium').innerHTML ="Rs." + parseInt(net_premium)
    document.getElementById('vat_c').innerHTML ="Rs." + parseInt(vat)
    document.getElementById('stamp_c').innerHTML ="Rs." + parseInt(stamp)
    document.getElementById('total_c').innerHTML ="Rs." +  parseInt(total)
}
  