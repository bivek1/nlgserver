function calculateTP(){
    intcc = $("#cc :selected").val();
    var TPtotal = 0
    var TPstamp = 20
    var TPvat = 0
    var TPcost = 0
    if(ty == "Electric Vehicle" || ty == "Vehicle CC"){
        if(intcc == 'Less than 150 CC'){
            var TPcost = 1500
            TPvat = 13/100 * TPcost
            TPtotal = 1500+TPvat+20
            // alert("Your Total Cost is"+total)
        }
        if(intcc == '150 to 250 CC'){
            var TPcost = 1700
            TPvat = 13/100 * TPcost
            TPtotal = 1700+TPvat+20
        
        }
        if(intcc == 'Above 250 CC'){
            var TPcost = 1900
            TPvat = 13/100 * TPcost
            TPtotal = 1900+TPvat+20
        }

    }
    if(ty == "Government Vehicle"){
        if(intcc == 'Less than 150 CC'){
        console.log("less than 150 CC")
        var TPcost = 1250
        TPvat = 13/100 * TPcost
        TPtotal = 1250+TPvat+20
      
        
        }
        if(intcc == '150 to 250 CC'){
            console.log("More than 150 CC Less than 250 CC")
            var TPcost = 1500
            TPvat = 13/100 * TPcost
            TPtotal = 1500+TPvat+20
         
        }
        if(intcc == 'Above 250 CC'){
            var TPcost = 1500
            TPvat = 13/100 * TPcost
            TPtotal = 1500+TPvat+20
          
        
        }
    }   
    document.getElementById('basictp').innerHTML ="Rs." + parseInt(TPcost)
    document.getElementById('vat_tp').innerHTML ="Rs." + parseInt(TPvat)
    document.getElementById('stamp_tp').innerHTML ="Rs." + parseInt(TPstamp)
    document.getElementById('total_tp').innerHTML ="Rs." +  parseInt(TPtotal)
}