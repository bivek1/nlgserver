function calculateCarTP(){
    intcc = $("#ccCar").val();
    console.log(intcc)
    noSeat = $('#seatTP').val()
    helper = $("#helperTP :selected").val();
    var TPtotal = 0
    var TPstamp = 20
    var TPvat = 0
    var TPcost = 0
    var third_cost = 0
    var helper_cost = 0
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(intcc <= 3){
            TPcost = 6750
        }
        else{
            TPcost = 10500
        }
        if(helper == 'Yes'){
            helper_cost = 700
        }
        driver_cost = 700
     
        passenger_cost = (parseInt(noSeat)-1) * 700

        third_cost = driver_cost+passenger_cost+TPcost+helper_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        document.getElementById('seat_tp').innerHTML = "Driver: " +700 +" "+ noSeat +"-1 * 700: "+ driver_cost+passenger_cost

    }
    else{
        driver_cost = 600
        if(intcc <= 3){
            TPcost = 5500
        }
        else{
            TPcost = 8500
           
        }
        if(helper == 'Yes'){
            helper_cost = 600
        }
        third_cost = driver_cost+passenger_cost+TPcost+helper_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        passenger_cost = (parseInt(noSeat)-1) * 600
        document.getElementById('seat_tp').innerHTML = "Driver: " +600 +" "+ noSeat +"-1 * 600: "+ driver_cost+passenger_cost    
    }   
    document.getElementById('basictp').innerHTML ="Rs." + parseInt(TPcost)
    document.getElementById('vat_tp').innerHTML ="Rs." + parseInt(TPvat)
    document.getElementById('helper_tp').innerHTML="Rs. "+parseInt(helper_cost)
    document.getElementById('stamp_tp').innerHTML ="Rs." + parseInt(TPstamp)
    document.getElementById('total_tp').innerHTML ="Rs." +  parseInt(TPtotal)
}