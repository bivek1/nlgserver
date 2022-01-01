function calculateCarTP(){
    intcc = $("#ccCar").val();
    trailer = $('#cctrailer').val()
    console.log(intcc)
    noSeat = $('#seatTP').val()
    helper = $("#helperTP :selected").val();
    var TPtotal = 0
    var TPstamp = 20
    var TPvat = 0
    var TPcost = 0
    var third_cost = 0
    var helper_cost = 0
    var trailer_cost = 0
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(intcc <= 15){
            TPcost = 1500
        }
        else if(intcc >=16 && intcc <= 20){
            TPcost = 2000
        }
        else{
            TPcost = 5500
        }
        if(helper == 'Yes'){
            helper_cost = 700
        }
        if (trailer == 'Yes'){
            trailer_cost = 1000
        }
        driver_cost = 700
     
        passenger_cost = (parseInt(noSeat)-1) * 700

        third_cost = driver_cost+passenger_cost+TPcost+helper_cost + trailer_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        document.getElementById('seat_tp').innerHTML = driver_cost+passenger_cost

    }
    else{
        driver_cost = 600
        if(intcc <= 15){
            TPcost = 750
        }
        else if(intcc >=16 && intcc <= 20){
            TPcost = 1000
        }
        else{
            TPcost = 2750
        }
        if(helper == 'Yes'){
            helper_cost = 600
        }
        if (trailer == 'Yes'){
            trailer_cost = 1000
        }
        third_cost = driver_cost+passenger_cost+TPcost+helper_cost+trailer_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        passenger_cost = (parseInt(noSeat)-1) * 600
        document.getElementById('seat_tp').innerHTML =  driver_cost+passenger_cost    
    }   
    document.getElementById('basictp').innerHTML ="Rs." + parseInt(TPcost)
    document.getElementById('vat_tp').innerHTML ="Rs." + parseInt(TPvat)
    document.getElementById('helper_tp').innerHTML="Rs. "+parseInt(helper_cost)
    document.getElementById('trailer_tp').innerHTML="Rs. "+parseInt(trailer_cost)
    document.getElementById('stamp_tp').innerHTML ="Rs." + parseInt(TPstamp)
    document.getElementById('total_tp').innerHTML ="Rs." +  parseInt(TPtotal)
}