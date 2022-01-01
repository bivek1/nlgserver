function calculateCarTP(){
    intcc = $("#ccCar").val();
    noSeat = $('#seatTP').val()
    helper = $("#helperTP :selected").val();
    conductor = $("#conductorTP :selected").val();
    var TPtotal = 0
    var TPstamp = 20
    var TPvat = 0
    var TPcost = 0
    var third_cost = 0
    var helper_cost = 0
    var conductor_cost = 0
    if(ty == "Electric Vehicle" ){
        if(intcc <= 14){
            TPcost = 6500
        }
        else if(intcc <= 15 && intcc <=18){
            TPcost = 7500
        }
        else if (intcc <= 19 && intcc <=35){
            TPcost = 9000
        }
        else{
            TPcost = 10000
        }
        if(helper == 'Yes'){
            helper_cost = 700
        }
    
        if (conductor == 'Yes'){
            conductor_cost=700
        }

        passenger_cost = (parseInt(noSeat)-1) * 700
        alert(passenger_cost)
        third_cost = passenger_cost+TPcost+helper_cost+conductor_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20

    }
    else if(ty == "Vehicle CC"){
        if(intcc <= 14){
            TPcost = 6500
        }
        else if(intcc <= 15 && intcc <=18){
            TPcost = 7500
        }
        else if (intcc <= 19 && intcc <=35){
            TPcost = 9000
        }
        else{
            TPcost = 10000
        }
        if(helper == 'Yes'){
            helper_cost = 700
        }
   
        if (conductor == 'Yes'){
            conductor_cost=700
        }
        passenger_cost = (parseInt(noSeat)-1) * 700
        third_cost = passenger_cost+TPcost+helper_cost+conductor_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
     
    }
    else{
        driver_cost = 600
        if(intcc <= 20){
            TPcost = 5500
        }
    
        else{
            TPcost = 8500
        }
        if(helper == 'Yes'){
            helper_cost = 600
        }
        
        if (conductor == 'Yes'){
            conductor_cost=600
        }
        passenger_cost = (parseInt(noSeat)-1) * 600
        third_cost = passenger_cost+TPcost+helper_cost+conductor_cost
        TPvat = 13/100 * third_cost
        TPtotal = third_cost+TPvat+20
  
     
    }  
    
    document.getElementById('basictp').innerHTML ="Rs." + parseInt(TPcost) 
    document.getElementById('seat_tp').innerHTML ="Rs." + parseInt(passenger_cost)
    document.getElementById('vat_tp').innerHTML ="Rs." + parseInt(TPvat)
    document.getElementById('helper_tp').innerHTML="Rs. "+parseInt(helper_cost)
    document.getElementById('conductor_tps').innerHTML="Rs. "+parseInt(conductor_cost)
    document.getElementById('stamp_tp').innerHTML ="Rs." + parseInt(TPstamp)
    document.getElementById('total_tp').innerHTML ="Rs." +  parseInt(TPtotal)
}