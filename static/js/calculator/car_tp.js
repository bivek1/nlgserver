function calculateCarTP(){
    intcc = $("#ccCar :selected").val();
    console.log(intcc)
    noSeat = $('#seatTP').val()
    var TPtotal = 0
    var TPstamp = 20
    var TPvat = 0
    var TPcost = 0
    var third_cost =0
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(intcc == 'Less than 1000 CC'){
            TPcost = 3000
            console.log('3000')
        }
        else if(intcc == '1000 to 1600 CC'){
            TPcost = 4000
            console.log('4000')
          
        }
        else if(intcc == 'Above 1600 CC'){
            TPcost = 6000
            console.log('6000')
           
        }
        else{
            TPcost = 0
            console.log('6000') 
        }
        driver_cost = 700
     
        passenger_cost = (parseInt(noSeat)-1) * 700

        third_cost = driver_cost+passenger_cost+TPcost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        document.getElementById('seat_tp').innerHTML = "Driver: " +700 +" "+ noSeat +"-1 * 700: "+ driver_cost+passenger_cost

    }
    else{
        if(intcc == 'Less than 1000 CC'){
            TPcost = 1000
        }
        else if(intcc == '1000 to 1600 CC'){
            TPcost = 1500
        }
        else if(intcc == 'Above 1600 CC'){
            TPcost = 2750 
        }
        else{
            TPcost = 0
            console.log('6000') 
        }
        third_cost = driver_cost+passenger_cost+TPcost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
        passenger_cost = (parseInt(noSeat)-1) * 600
        document.getElementById('seat_tp').innerHTML = "Driver: " +600 +" "+ noSeat +"-1 * 600: "+ driver_cost+passenger_cost    
    }   
    document.getElementById('basictp').innerHTML ="Rs." + parseInt(TPcost)
    document.getElementById('vat_tp').innerHTML ="Rs." + parseInt(TPvat)
  
    document.getElementById('stamp_tp').innerHTML ="Rs." + parseInt(TPstamp)
    document.getElementById('total_tp').innerHTML ="Rs." +  parseInt(TPtotal)
}